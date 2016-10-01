from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re

def CarregaPagina(url, codin='utf-8'):
    #print(url)
    with urllib.request.urlopen(url) as response:
        html = response.read()
        html = html.lower()
    return BeautifulSoup(html, 'html.parser')


""" PESQUISA URL """

url = input("Digite sua URL para pesquisa: http://")
wor = input("Digite sua PALAVRA para pesquisa: ")
url = url.lower()
wor = wor.lower()

prefixo = "http://"
url = prefixo+url

print()
print("Pesquisando no LINK %s a PALAVRA %s" %(url,wor))
print()

pagina = CarregaPagina(url)

for texto in pagina.find_all(string=re.compile(wor)):
    print(texto)
print("----- fim -----")
