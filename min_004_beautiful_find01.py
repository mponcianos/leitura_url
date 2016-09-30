from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

def CarregaPagina(url, codin='utf-8'):
    #print(url)
    with urllib.request.urlopen(url) as response:
        html = response.read()
    return BeautifulSoup(html, 'html.parser')


""" PESQUISA URL """
url = input("Digite sua URL para pesquisa: http://")

prefixo = "http://"
url = prefixo+url

print()
print("Pesquisando LINKS em "+url)

pagina = CarregaPagina(url)

for link in pagina.find_all('a'):
    print(link.get('href'))

#print(pagina.title.string)
#print(pagina.prettify())
