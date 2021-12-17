# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:11:30 2021

"""

import requests

URL = 'https://swapi.dev/api/planets/'

data = requests.get(URL)
data = data.json()
Resultados_Planetas = []

for i in range(1,61):
    URL=URL + str(i)
    data = requests.get(URL)
    data = data.json()
    Info = (data['climate'],data['films'])
    Resultados_Planetas.append(Info)
    URL = 'https://swapi.dev/api/planets/'

Peliculas_Planetas_Aridos = []

for element in Resultados_Planetas:
    if ('arid' in element[0]) == True:
        Peliculas_Planetas_Aridos.append(element[1])

Lista_Peliculas_Planetas_Aridos = []
for element in Peliculas_Planetas_Aridos:
    for peliculas in element:
        if (peliculas not in Lista_Peliculas_Planetas_Aridos) == True:
            Lista_Peliculas_Planetas_Aridos.append(peliculas)
#Respuesta

print('Existen',len(Lista_Peliculas_Planetas_Aridos),'peliculas donde aparecen planetas áridos')


## Aeronave

URL = 'https://swapi.dev/api/vehicles/4'
data = requests.get(URL)
data = data.json()
Aeronaves = []
for i in range(1,40):
    try:
        URL = 'https://swapi.dev/api/vehicles/'
        URL=URL + str(i)
        dataV = requests.get(URL)
        dataV = dataV.json()
        Info = (dataV['name'],dataV['length'])
        Aeronaves.append(Info)
    except:
        print('No se han encontrado')



