#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

def tri_insertion(tableau: 'list[int]') -> None:
    ''' Effectue le tri par insertion en place des éléments d'un tableau donné.
    :param tableau: (list[int]) un tableau d'entiers à trier 
    
    :Exemples:
    >>> l = [randint(0, 99) for _ in range(10)]
    >>> est_trie(l)
    False
    >>> tri_insertion(l)
    >>> est_trie(l)
    True
    '''

    for i in range(1, len(tableau)):
        cle = tableau[i]
        j = i - 1
        while j >= 0 and tableau[j] > cle:
            tableau[j + 1] = tableau[j]
            j = j - 1
        tableau[j + 1] = cle

def tri_insertion_decroissant(tableau: 'list[int]') -> None:
    ''' Effectue le tri par insertion en place des éléments d'un tableau donné dans l'ordre décroissant.
    :param tableau: (list[int]) un tableau d'entiers à trier '''

    for i in range(1, len(tableau)):
        cle = tableau[i]
        j = i - 1
        while j >= 0 and tableau[j] < cle:
            tableau[j + 1] = tableau[j]
            j = j - 1
        tableau[j + 1] = cle

def est_trie(tableau: 'list[int]') -> bool:
    ''' Renvoie True si les éléments du tableau sont triés, False sinon.
    :param tableau: (list[int]) tableau d'entiers à vérifier
    :return: (bool) True ou False selon si les éléments sont triés ou non. '''

    for i in range(1, len(tableau)):
        if tableau[i - 1] > tableau[i]:
            return False
    return True

if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    import doctest
    doctest.testmod(verbose=False)