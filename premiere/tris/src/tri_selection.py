#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

''' Implémentation du tri par sélection du minimum. '''

def tests():
    ''' Fonction servant uniquement à effectuer des tests avec le module doctest.
    Les exemples ci-dessous sont automatiquement exécutés par le module doctest lors de
    l'exécution de ce programme. S'il ne se passe rien, cela signifie que les tests fonctionnent.

    >>> l = [9, 1, 7, 3, 5, 2, 6]
    >>> est_trie(l)
    False
    >>> tri_selection(l)
    >>> est_trie(l)
    True
    >>> l = [randint(0, 100) for _ in range(20)]
    >>> tri_selection(l)
    >>> est_trie(l)
    True
    '''

    pass

# ==> QUESTION 1 <==

def minimum(tableau: 'list[int]', debut: int) -> int:
    ''' Renvoie l'indice de la valeur minimale du tableau dans l'intervalle [debut, len(tableau) - 1].
    :param tableau: (list[int]) un tableau d'entiers
    :param debut: (int) l'indice à partir duquel on recherche le minimum
    :return: (int) l'indice du minimum '''

    pass

def echanger(tableau: 'list[int]', i: int, j: int) -> None:
    ''' Echanger deux éléments d'un tableau
    :param tableau: (list[int]) un tableau d'entiers
    :param i: (int) l'indice d'un élément du tableau
    :param j: (int) l'indice d'un élément du tableau '''

    pass

def tri_selection(tableau: 'list[int]') -> None:
    ''' Effectue le tri par sélection en place des éléments d'un tableau donné.
    :param tableau: (list[int]) un tableau d'entiers à trier '''

    pass

# ==> QUESTION 2 <==

def tri_selection_tout_en_un(tableau: 'list[int]') -> None:
    ''' Effectue le tri par sélection en place des éléments d'un tableau donné.
    
    :param tableau: (list[int]) un tableau d'entiers à trier '''

    pass

# ==> QUESTION 3 <==

def tri_selection_decroissant(tableau: 'list[int]') -> None:
    ''' Effectue le tri par sélection dans l'ordre décroissant des éléments d'un tableau donné.
    :param tableau: (list[int]) un tableau d'entiers à trier '''

    pass

# Fonctions utiles (ne pas modifier)

def est_trie(tableau: 'list[int]', fin: int = None) -> bool:
    ''' Renvoie True si les éléments du tableau dans [0, fin] sont triés, False sinon.
    Si pas d'indice de fin donné, vérifier tout le tableau.
    :param tableau: (list[int]) tableau d'entiers à vérifier
    :param debut: (int) indice jusqu'auquel vérifier les éléments
    :return: (bool) True ou False selon si les éléments sont triés ou non. '''

    if fin == None: fin = len(tableau) - 1
    return all(tableau[i - 1] <= tableau[i] for i in range(1, fin + 1))

if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    import doctest
    doctest.testmod(verbose=False)
