# ===> PROGRAMME 1 <===

def somme(a, b):
    ''' Fonction qui retourne la somme de a et b.
    :param a: (int) Un entier
    :param b: (int) Un autre entier
    :return: (int) La somme de a et b
    
    :Exemple:
    >>> somme(2, 4)
    6
    '''
    
    ...
    
    
def produit(a, b):
    ''' Fonction qui renvoie le produit de a et b.
    :param a: (int) Un entier
    :param b: (int) Un autre entier
    :return: (int) Le produit de a et b
    
    :Exemple:
    >>> produit(4, 6)
    24
    '''
    
    # COMPLETER LES POINTILLES
    res = 0
    for _ in range(...):
        res = somme(..., ...)
    return ...

def prod_liste(l1, l2):
    ''' Fonction qui renvoie le produit des éléments de deux listes.
    :param l1: (list) Une liste
    :param l2: (list) Une autre liste
    :return: (list) La liste contenant les résultats de ces produits
    
    :Exemple:
    >>> prod_liste([1, 2, 3], [4, 5, 6])
    [4, 10, 18]
    '''
    
    res = []
    for i in range(len(...)):
        res.append(produit(..., ...))
    return ...


# Les lignes suivantes permettent d'activer les tests des fonctions.
if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
