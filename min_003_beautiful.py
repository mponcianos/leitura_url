from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

url = 'http://estudante.ufpe.br/'

values = {'s':'curso'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = urllib.request.Request(url,data)

resp = urllib.request.urlopen(req)

respData = resp.read()

soup = BeautifulSoup(respData, 'html.parser')

print(soup.prettify())
print(soup.title)



