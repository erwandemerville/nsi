# ===> PROGRAMME 2 <===

def minimum(liste):
    ''' Renvoie l'élément le plus petit d'une liste d'entiers.
    :param liste: (list) Une liste d'entiers.
    :return: (int) L'entier minimum de la liste.
    
    :Exemple:
    >>> minimum([2,1,5,7])
    1
    '''
    
    minimum = None
    for element in ...:
        if minimum == None or element < ...:
            minimum = element
    return ...
    
def maximum(liste):
    ''' Renvoie l'élément le plus grand d'une liste d'entiers.
    :param liste: (list) Une liste d'entiers.
    :return: (int) L'entier maximum de la liste.
    
    :Exemple:
    >>> maximum([2,1,5,7])
    7
    '''
    
    ...
    
def indice_min(liste):
    ''' Renvoie l'indice du plus petit élément de la liste.
    :param liste: (list) Une liste d'entiers.
    :return: (int) L'indice du plus petit élément
    
    :Exemple:
    >>> indice_min([4, 2, 3, 7])
    1
    '''
    
    minimum = None
    indice = None
    taille_liste = ...
    for i in range(taille_liste):
        if minimum == None or liste[...] < ...:
            minimum = ...
            indice = ...
    return indice

def tri_selection(liste):
    ''' Tri par sélection d'une liste.
    :param liste: (list) Une liste d'entiers.
    :return: (list) Une liste d'entiers triée.
    
    :Exemple:
    >>> tri_selection([4, 2, 3, 7, 9])
    [2, 3, 4, 7, 9]
    '''
    
    for i in range(len(...)):
        
       # Déterminer le minimum
       min = i + indice_min(liste[i:])
       
       # Permuter l'élément i avec l'élément min
       tmp = liste[i]
       liste[i] = ...
       liste[min] = ...
       
    return liste

# Les lignes suivantes permettent d'activer les tests des fonctions.
if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)

