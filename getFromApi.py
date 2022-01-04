import requests
import urllib

# Eskaerak 4 atal ditu: metodoa, uria, goiburuak eta edukia
# metodoa = 'GET'
# uri = "https://services7.arcgis.com/lTrEzFGSU2ayogtj/arcgis/rest/services/COMPLETA_Afectados_por_coronavirus_por_provincia_en_Espa%C3%B1a_Vista_Solo_lectura/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
# goiburuak = {'Host': 'covid19.secuoyas.com',
#              'Content-Type' : 'application/json'}
#
# # datuak = {'nan' : '79138851'}
# # Baina datuak nan=79138851 formatuan bidali behar dira
# # edukia = urllib.parse.urlencode(datuak)
# # goiburuak['Content-Length'] = str(len(edukia))
#
# erantzuna = requests.request(metodoa, uri, headers=goiburuak, allow_redirects=False)
#
# kodea = erantzuna.status_code
# deskribapena = erantzuna.reason
# print(str(kodea) + " " + deskribapena)
# edukia = erantzuna.content
# print(edukia)

# GET POBLACIÓN DE ESPAÑA

# res = requests.get('https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176951&menu=ultiDatos&idp=1254735572981')
# stri = str(res.content)
# poblacionStr = stri.split('Poblaci\\xc3\\xb3n total. Valor"} -->', 1)[1].split('\\n',1)[0]
# poblacion = int(poblacionStr.replace(".",""))
#
# casos21 = 682441
# casos14 = 489537
#
# incidenciaTotal = casos14/(poblacion-(casos21-casos14))
# incidencia100k = 100000*casos14/poblacion
#
# print(incidenciaTotal)
# print(incidencia100k)

res = requests.get('https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/12-20-2021.csv')
stri = str(res.content)
print(stri)