import requests
import urllib
from bs4 import BeautifulSoup



def getCSV(url):
  response = requests.get(url)
  edukia=response.content
  soup = BeautifulSoup(edukia, 'html.parser')
  item_results = soup.find_all('a')
  for each in item_results:
    if each['href'].find(".csv") != -1:
      download(each['href'])

def download(url):
  print(url)
  pdfname = url.replace('http:://', '')
  pdfname = pdfname.replace('https://', '')
  pdfname = pdfname.replace('/', '-')
  r = requests.get(url, allow_redirects=True)
  open('./dataCSV/'+pdfname, 'wb').write(r.content)


url='https://cnecovid.isciii.es/covid19/#documentaci%C3%B3n-y-datos'
print('Datuak lortu')
print(url)
getCSV(url)
