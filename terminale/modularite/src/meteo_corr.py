#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from matplotlib import pyplot

API_KEY = "d9555c03135810f8d2155d7ae0ee4835"  # API Key utilisée
PAYS = 'FR'  # Code de la France

def get_weather(ville: str) -> dict:
    ''' Renvoie un dictionnaire contenant les données sur la météo actuelle de la ville entrée. '''
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ville},{PAYS}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    return r.json()

def temperature_ressentie(ville: str) -> None:
    ''' Affiche la température ressentie (en degrés) dans la ville spécifiée. '''
    
    donnees = get_weather(ville)
    print(f"Température ressentie à {ville} : {donnees['main']['feels_like']} °C.")

def get_temp_from_lat_long(lat: float, long: float) -> None:
    ''' Affiche la température (en degrés) d'une ville dont on fournit la latitude et la longitude. '''
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    donnees = r.json()

    print(f"Température : {donnees['main']['temp']} °C.")

def compare_two_cities(ville1: str, ville2: str) -> None:
    ''' Affiche la courbe d'évolution de la température de deux villes spécifiées en entrée. '''
    
    url1 = f"https://api.openweathermap.org/data/2.5/forecast?q={ville1},{PAYS}&appid={API_KEY}&units=metric"
    url2 = f"https://api.openweathermap.org/data/2.5/forecast?q={ville2},{PAYS}&appid={API_KEY}&units=metric"
    r1 = requests.get(url1)
    r2 = requests.get(url2)
    
    tab1 = [mesure['main']['temp'] for mesure in r1.json()['list']]
    tab2 = [mesure['main']['temp'] for mesure in r2.json()['list']]
    
    pyplot.plot(tab1, 'r', label=f'{ville1}')
    pyplot.plot(tab2, 'b', label=f'{ville2}')
    pyplot.legend()
    pyplot.title(f"Comparaison températures de {ville1} et {ville2}")
    pyplot.show()
        
if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    compare_two_cities('Paris', 'Méru')
