#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operations import ajouter_debut, sum_lst

def to_bin(ent: int) -> list:
    ''' Renvoie la représentation binaire de l'entier spécifié, sous la forme d'une liste.
    On utilise la méthode des divisions euclidiennes successives.

    :Exemples:
    >>> to_bin(10)
    [1, 0, 1, 0]
    '''
    
    lst = []
    while ent != 0:
        lst = ajouter_debut(lst, ent%2)
        ent //= 2
    return lst

def moyenne(lst: list) -> float:
    ''' Renvoie la moyenne des éléments d'une liste.

    :Exemples:
    >>> moyenne([12,15,10,20])
    14.25
    '''
    
    return sum_lst(lst) / len(lst)
    
if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose = True)