# ===> PROGRAMME 3 <===

def concatener(l1, l2):
    ''' Concaténation de deux listes.
    :param l1: (list) Une liste d'entiers
    :param l2: (list) Une autre liste d'entiers
    :return: (list) Concaténation des listes l1 et l2.
    
    :Exemple:
    >>> concatener([2, 3], [4, 8, 6])
    [2, 3, 4, 8, 6]
    '''
    
    ...

def inverser(liste):
    ''' Renvoie l'inverse d'une liste.
    :param liste: (list) Une liste d'entiers
    :return: (list) La liste inversée
    
    :Exemple:
    >>> inverser([2, 4, 6, 9])
    [9, 6, 4, 2]
    '''
    
    ...
    
def somme_li(liste):
    ''' Renvoie la somme des éléments la liste avec ceux de son inverse.
    :param liste: (list) Une liste d'entiers
    :return: (list) Liste contenant la somme des éléments de la liste avec ceux de son inverse
    
    :Exemple:
    >>> somme_li([2, 3, 6, 5])
    [7, 9, 9, 7]
    '''
    
    ...
    
def somme_lignes(tableau):
    ''' Retourne une liste contenant la somme de chaque ligne du tableau.
    :param tableau: (list of list) Un tableau à 2 dimensions
    :return: (list) Une liste contenant la somme de chaque ligne
    
    :Exemple:
    >>> somme_lignes([[1,5,2,3], [4,2,3,1], [6,3,4,4]])
    [11, 10, 17]
    '''
    
    ...
    
def somme_colonnes(tableau):
    ''' Retourne une liste contenant la somme de chaque ligne du tableau.
    :param tableau: (list of list) Un tableau à 2 dimensions
    :return: (list) Une liste contenant la somme de chaque ligne
    :CU: Les lignes du tableau font toutes la même taille.
    
    :Exemple:
    >>> somme_colonnes([[1,5,2,3], [4,2,3,1], [6,3,4,4]])
    [11, 10, 9, 8]
    '''
    nb_colonnes = ...
    somme = [0] * nb_colonnes  # Créer une liste dont la taille correspond au nb de colonnes, avec que des 0.
    for i in range(len(nb_colonnes)):
        for j in range(...):
            somme[...] += ...
    return ...


# Les lignes suivantes permettent d'activer les tests des fonctions.
if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    