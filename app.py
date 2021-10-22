import json
import requests
from bs4 import BeautifulSoup
import os

#Descarga la pagina "el tiempo"
t = requests.get('https://www.eltiempo.com/')
soup_t = BeautifulSoup(t.text, 'lxml')
#Crea el archivo
archivo = open('eltiempo.html','w')
archivo.write(str(soup_t))
archivo.close()
