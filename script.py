from datetime import date, timedelta
from google.cloud import storage
import pandas as pd

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

if __name__ == "__main__":

    yesterday = (date.today() - timedelta(days=1)).strftime('%m-%d-%Y')
    yesterdayOK = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    days_28 = (date.today() - timedelta(days=29)).strftime('%Y-%m-%d')
    days_14 = (date.today() - timedelta(days=15)).strftime('%Y-%m-%d')
    days_7 = (date.today() - timedelta(days=8)).strftime('%Y-%m-%d')
    nombre = str(yesterday)+'.csv'
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+nombre
    df = pd.read_csv(url)
    df['Fecha'] = yesterday
    df.to_csv(nombre, index = False)
    u = upload_to_bucket(nombre, nombre, "covidinfo-bucket")

    jsonString = '{"arguments" : [{"name": "filename", "value": "gs://covidinfo-bucket/'+nombre+'"}, {"name": "day", "value": "'+str(yesterdayOK)+'"}, {"name": "day28", "value": "'+str(days_28)+'"}, {"name": "day14", "value": "'+str(days_14)+'"}, {"name": "day7", "value": "'+str(days_7)+'"}]}'
    jsonFile = open("args.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

    u = upload_to_bucket("args.json", "args.json", "covidinfo-bucket")