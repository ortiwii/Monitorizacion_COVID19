import urllib
from datetime import date, timedelta
from google.cloud import storage
import pandas as pd
from google.cloud import bigquery
from datetime import datetime
import os

def upload_to_bucket(blob_name, path_to_file, bucket_name):
    """ Upload data to a bucket"""

    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(
        'credentials.json')

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)

    return blob.public_url

def bigqueryExequte(rows_to_insert):
    client = bigquery.Client.from_service_account_json(
        'credentials.json')

    table_id = "covid-336715.datoscovid.datos"

    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.

    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))
    client.close()
if __name__ == "__main__":

    yesterday = (date.today() - timedelta(days=1)).strftime('%m-%d-%Y')
    day = datetime.today() - timedelta(days=1)
    yesterdayOK = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    days_28 = (date.today() - timedelta(days=29)).strftime('%Y-%m-%d')
    days_14 = (date.today() - timedelta(days=15)).strftime('%Y-%m-%d')
    days_7 = (date.today() - timedelta(days=8)).strftime('%Y-%m-%d')
    nombre = str(yesterday)+'.csv'
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+nombre
    df = pd.read_csv(url)

    try:
        df = df.rename({'Incidence_Rate': 'Incident_Rate', 'Case-Fatality_Ratio':'Case_Fatality_Ratio'}, axis=1)
    except:
        pass
    try:
        df['Incident_Rate'] = df['Incident_Rate'].round(7)
    except:
        pass
    try:
        df['Case_Fatality_Ratio'] = df['Case_Fatality_Ratio'].round(7)
    except:
        pass
    try:
        df.dropna(subset=["Lat"], inplace=True)
    except:
        pass
    try:
        df = df.drop(columns=['Recovered', 'Lat', 'Long'])
    except:
        pass
    try:
        df = df.rename({'Province/State': 'Province_State', 'Country/Region': 'Country_Region',
                        'Last Update': 'Last_Update'}, axis=1)
    except:
        pass

    df['Fecha'] = str(day)
    for act in df: print(act)
    df = df.where(pd.notnull(df), None)
    rows_to_insert = df.to_dict('records')
    df.to_csv(nombre, index = False)




    u = upload_to_bucket('CSV/'+nombre, nombre, "covidinfo-bucket")
    jsonString = '{"arguments" : [{"name": "filename", "value": "gs://covidinfo-bucket/'+nombre+'"}, {"name": "day", "value": "'+str(yesterdayOK)+'"}, {"name": "day28", "value": "'+str(days_28)+'"}, {"name": "day14", "value": "'+str(days_14)+'"}, {"name": "day7", "value": "'+str(days_7)+'"}]}'
    jsonFile = open("args.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

    u = upload_to_bucket("args.json", "args.json", "covidinfo-bucket")

    bigqueryExequte(rows_to_insert)

    os.remove(nombre)
