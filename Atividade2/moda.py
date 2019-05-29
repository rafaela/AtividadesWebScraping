#coding: utf-8
from bs4 import BeautifulSoup
import requests
import re
import json

url = 'https://tudoela.com/moda/looks/'
estilos = []
pagina = 1

def requisicao(url):
    res = requests.get(url)
    
    soup = BeautifulSoup(res.text, 'html.parser')

    div = soup.find("div", class_=re.compile('vce-loop-wrap'))
    
    for header in div.find_all('article'):
        estilo = {}
        span = header.find('span')
        h2 = header.find('h2')
        if span.text == 'Looks':
            estilo['Sobre'] = span.text
            estilo['Matéria'] = h2.text
            
            estilos.append(estilo)

while pagina < 22:
    if pagina == 1:
        requisicao(url)
        pagina += 1
    else:
        print(url + 'page/' + str(pagina))
        requisicao(url + 'page/' + str(pagina))
        pagina += 1


with open('moda.json', 'w') as outfile:
    json.dump(estilos, outfile, indent=4, ensure_ascii=False)