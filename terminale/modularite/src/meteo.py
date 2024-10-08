#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# Variables globales
API_KEY = "d9555c03135810f8d2155d7ae0ee4835"  # API Key utilisée
PAYS = 'FR'  # Code de la France

def get_weather(ville: str) -> dict:
    ''' Renvoie un dictionnaire contenant les données sur la météo actuelle de la ville entrée. '''
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ville},{PAYS}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    return r.json()

def temperature_ressentie(ville: str) -> None:
    ''' Affiche la température ressentie (en degrés) dans la ville spécifiée. '''
    
    pass

def get_temp_from_lat_long(lat: float, long: float) -> None:
    ''' Affiche la température (en degrés) d'une ville dont on fournit la latitude et la longitude. '''
    
    pass

def compare_two_cities(ville1: str, ville2: str) -> None:
    ''' Affiche la courbe d'évolution de la température de deux villes spécifiées en entrée. '''
    
    url1 = f"https://api.openweathermap.org/data/2.5/forecast?q={ville1},{PAYS}&appid={API_KEY}&units=metric"
    url2 = f"https://api.openweathermap.org/data/2.5/forecast?q={ville2},{PAYS}&appid={API_KEY}&units=metric"
    r1 = requests.get(url1).json()  # r1 contient le dictionnaire contenant les données sur la ville 1
    r2 = requests.get(url2).json()  # r2 contient le dictionnaire contenant les données sur la ville 2
    
    # À COMPLÉTER...
    
if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    pass