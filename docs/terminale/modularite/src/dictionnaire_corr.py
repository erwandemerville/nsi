#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module permettant de créer et manipuler des dictionnaires.
"""

def cree():
    ''' Renvoie un nouveau dictionnaire vide.
    :return: (dict) un dictionnaire vide '''

    return {}

def cle(d, k):
    ''' Renvoie True si et seulement si le dictionnaire d contient la clé k.
    :param d: (dict) un dictionnaire
    :param k: (str) une clé du dictionnaire
    :return: (bool) True ou False '''

    return k in d

def lit(d, k):
    ''' Renvoie la valeur associée à la clé k dans le dictionnaire d,
    et None si la clé k n'apparait pas.
    :param d: (dict) un dictionnaire
    :param k: (str) une clé du dictionnaire
    :return: (*) valeur associée à la clé k ou None '''

    if cle(d, k):
        return d[k]

def ecrit(d, k, v):
    ''' Ajoute au dictionnaire d l'association entre la clé k et la valeur v,
    en remplaçant une éventuelle association déjà présente pour k. 
    :param d: (dict) un dictionnaire
    :param k: (str) une clé du dictionnaire
    :param v: (*) une valeur à ajouter au dictionnaire
    :return: (None) rien '''

    d[k] = v

if __name__ == '__main__':

    # Exemple d'utilisation et test de ce module avec des assertions
    dico = cree()
    assert type(dico) == dict
    assert cle(dico, 'a') == False
    ecrit(dico, 'a', 42)
    assert cle(dico, 'a') == True
    assert lit(dico, 'a') == 42
    ecrit(dico, 'a', 45)
    assert lit(dico, 'a') == 45