''' Quelques fonctions pour présenter le module doctest '''

def produit(a, b):
    ''' Fonction qui renvoie le produit de a et b.
    :CU: type(a) == type(b) == int
    :param a: (int) Un entier
    :param b: (int) Un autre entier
    :return: (int) Le produit de a et b
    
    :Exemple:
    >>> produit(4, 6)
    24
    '''
    
    res = 0
    for _ in range(b):
        res += a
    return res

def prod_liste(l1, l2):
    ''' Fonction qui renvoie le produit des éléments de deux listes.
    :CU: all([type(l1) == type(l2) == list[int], len(l1) == len(l2)])
    :param l1: (list) Une liste
    :param l2: (list) Une autre liste
    :return: (list) La liste contenant les résultats de ces produits
    
    :Exemple:
    >>> prod_liste([1, 2, 3], [4, 5, 6])
          [4, 10, ...]
    '''
    
    res = []
    for i in range(len(l1)):
        res.append(produit(l1[i], l2[i]))
    return res


# Les lignes suivantes permettent d'activer les tests des fonctions.
if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
