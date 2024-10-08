#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module permettant d'effectuer diverses opérations sur des listes Python.
"""

def sum_lst(lst: list) -> int:
    ''' Renvoie le résultat de la somme des éléments d'une liste.

    :Exemples:
    >>> sum_lst([2, 4, 6, 8])
    20
    '''
    
    pass

def min_lst(lst: list) -> int:
    ''' Renvoie la valeur minimale d'une liste.

    :Exemples:
    >>> min_lst([8, 1, 9, 2, 7])
    1
    '''
    
    pass

def max_lst(lst: list) -> int:
    ''' Renvoie la valeur maximale d'une liste.

    :Exemples:
    >>> max_lst([8, 1, 9, 2, 7])
    9
    '''
    
    pass

def ajouter_debut(lst: list, el: int) -> list:
    ''' Renvoie une nouvelle liste contenant les éléments de lst incluant l'élément el en première position.

    :Exemples:
    >>> ajouter_debut([2, 9, 4, 5], 8)
    [8, 2, 9, 4, 5]
    '''
    
    pass

        
if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose = True)

