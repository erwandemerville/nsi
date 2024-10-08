# ===> PROGRAMME 8 <===

def factorielle(n):
    ''' Renvoie la factorielle du nombre n.
    :param n: (int) Un nombre entier
    :return: (int) La factorielle du nombre spécifié
    :CU: n >= 1
    
    :Exemple:
    >>> factorielle(4)
    24
    '''
    
    ...
    
def fibonacci(n):
    ''' Renvoie le terme de la suite de Fibonacci d'indice n.
    :param n: (int) L'indice du terme que l'on souhaite obtenir
    :return: (int) Un entier, le terme d'indice n de la suite
    
    :Exemple:
    >>> fibonacci(4)
    3
    >>> fibonacci(8)
    21
    '''
    
    ...

# TRI FUSION

def fusion(t1,t2):
    ''' Effectue la fusion de deux listes triées.
    :param gauche: (list) Une liste d'entiers triée
    :param droite: (list) Une liste d'entiers triée
    :return: (list) Fusion des deux listes
    
    :Exemple:
    >>> fusion([1, 3, 5], [2, 4, 7])
    [1, 2, 3, 4, 5, 7]
    '''
    
    if t1 == []:
        return t2
    elif t2 == []:
        return t1
    else:
        if t1[0] < t2[0]:
            return [t1[0]] + fusion(t1[1:], t2)
        else:
            return [t2[0]] + fusion(t1, t2[1:])
 
def tri_fusion(liste):
    ''' Effectue le tri fusion d'une liste.
    :param liste: (list) Une liste d'entiers
    :return: (list) Une liste triée
    
    :Exemple:
    >>> tri_fusion([2, 1, 6, 4, 7])
    [1, 2, 4, 6, 7]
    '''
    
    ...


# Les lignes suivantes permettent d'activer les tests des fonctions.
if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
