from datetime import date, timedelta
from google.cloud import storage
import pandas as pd
from google.cloud import bigquery
from datetime import datetime
import os

def upload_to_bucket(blob_name, path_to_file, bucket_name):

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
    i = 1
    yesterday = (date.today() - timedelta(days=i)).strftime('%m-%d-%Y')
    print(str(i)+': '+str(yesterday))
    day = datetime.today() - timedelta(days=i)
    nombre = str(yesterday)+'.csv'
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+nombre
    df = pd.read_csv(url)

    try:
        df['Incident_Rate'] = df['Incident_Rate'].round(7)
    except:
        try:
            df = df.rename(columns={'Incidence_Rate':'Incident_Rate'})
        except:
            pass
    try:
        df['Case_Fatality_Ratio'] = df['Case_Fatality_Ratio'].round(7)
    except:
        try:
            df = df.rename(columns={'Case-Fatality_Ratio': 'Case_Fatality_Ratio'})
        except:
            pass
    try:
        df.dropna(subset=["Lat"], inplace=True)
    except:
        pass
    try:
        df = df.drop(columns=['Recovered'])
        df = df.drop(columns=['Admin2', 'Active'])
    except:
        pass
    try:
        df = df.where(pd.notnull(df), None)
    except:
        pass
    try:
        df = df.rename(columns={'Latitude': 'Lat'})
    except:
        pass
    try:
        df = df.rename(columns={'Longitude': 'Long_'})
    except:
        pass
    try:
        df = df.rename(columns={'Country/Region': 'Country_Region'})
    except:
        pass
    try:
        df = df.rename(columns={'Province/State': 'Province_State'})
    except:
        pass
    try:
        df = df.rename(columns={'Last Update': 'Last_Update'})
    except:
        pass

    df['Fecha'] = day.strftime('%Y-%m-%d %H:%M:%S.%S')
    df['Last_Update'] = day.strftime('%Y-%m-%d %H:%M:%S.%S')
    rows_to_insert = df.to_dict('records')
    df.to_csv(nombre, index = False)

    u = upload_to_bucket('CSV/'+nombre, nombre, "covidinfo-bucket")

    bigqueryExequte(rows_to_insert)
    os.remove(nombre)

