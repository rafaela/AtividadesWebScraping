#coding: utf-8
from bs4 import BeautifulSoup
import requests
import re
import json

baseURL = 'http://www.henancius.com/henancius/top100.html'

res = requests.get(baseURL)

soup = BeautifulSoup(res.text.encode('iso-8859-1'), 'lxml')

table = soup.find("div", id="conteudo").find("table").find_all("table")[1]

filmes = []
for tr in table.find_all("tr")[1:]:
    fonts = tr.find_all("td")
    if len(fonts) < 4:
        continue
        
    filme = {}
    filme['Colocação'] = fonts[0].text.partition('.')[0]
    filme['Nome'] = ' '.join(fonts[1].text.split())
    filme['Ano'] = fonts[2].text
    filme['Arrecadação'] = fonts[3].text
    
    filmes.append(filme)


with open('filme.json', 'w') as outfile:
    json.dump(filmes, outfile, indent=4, ensure_ascii=False)
