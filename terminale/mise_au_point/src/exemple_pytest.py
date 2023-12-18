import pytest

''' Quelques fonctions pour présenter le module pytest '''

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
    [4, 10, 18]
    '''
    
    res = []
    for i in range(len(l1)):
        res.append(produit(l1[i], l2[i]))
    return res

def test_produit():
    assert produit(3,5) == 15
    assert produit(6,6) == 36
    
def test_prod_liste():
    assert prod_liste([2,3,4], [3,4,5]) == [6, 12, 20]

if __name__ == '__main__':
    pytest.main()