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

res = requests.get('https://services7.arcgis.com/lTrEzFGSU2ayogtj/arcgis/rest/services/COMPLETA_Afectados_por_coronavirus_por_provincia_en_Espa%C3%B1a_Vista_Solo_lectura/FeatureServer/0/query?where=1%3D1&outFields=OBJECTID,CodigoProv,FechaNormalizada,CasosConfirmados,Fallecidos,Altas,CCAA,NombreCCAA,Infectados,Hospitalizados,UCI,NuevoCasos,Ingresos,Fecha&outSR=4326&f=json')
print(res.status_code)
print(res.content)