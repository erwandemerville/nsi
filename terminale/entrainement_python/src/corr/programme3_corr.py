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
    
    return l1 + l2

def inverser(liste):
    ''' Renvoie l'inverse d'une liste (en utilisant liste PAR COMPRÉHENSION).
    :param liste: (list) Une liste d'entiers
    :return: (list) La liste inversée
    
    :Exemple:
    >>> inverser([2, 4, 6, 9])
    [9, 6, 4, 2]
    '''
    
    return liste[::-1]

def inverser_v2(liste):
    
    res = []
    for i in range(len(liste) - 1, -1, -1):
        res.append(liste[i])
    return res

def inverser_v3(liste):
    ''' Avec une liste PAR COMPRÉHENSION.'''
    
    return [liste[i] for i in range(len(liste) - 1, -1, -1)]

def inverser_v4(liste):
    ''' En utilisant un insert.'''
    
    res = []
    for i in range(len(liste)):
        res.insert(0, liste[i])
    return res
    
def somme_li(liste):
    ''' Renvoie la somme des éléments de la liste avec ceux de son inverse.
    :param liste: (list) Une liste d'entiers
    :return: (list) Liste contenant la somme des éléments de la liste avec ceux de son inverse
    
    :Exemple:
    >>> somme_li([2, 3, 6, 5])
    [7, 9, 9, 7]
    '''

    inverse = inverser(liste)  # Inverse de la liste obtenue avec la fonction précédente
    return [liste[i] + inverse[i] for i in range(len(liste))]

def somme_lignes(tableau):
    ''' Retourne une liste contenant la somme de chaque ligne du tableau.
    :param tableau: (list of list) Un tableau à 2 dimensions
    :return: (list) Une liste contenant la somme de chaque ligne
    
    :Exemple:
    >>> somme_lignes([[1,5,2,3], [4,2,3,1], [6,3,4,4]])
    [11, 10, 17]
    '''
    
    res = []
    for el in tableau:
        res.append(sum(el))  # en utilisant la fonction sum (HORS PROGRAMME)
    return res

def somme_lignes_v2(tableau):
    
    nb_lignes, nb_colonnes = len(tableau), len(tableau[0])
    res = [0] * nb_lignes
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            res[i] += tableau[i][j]
    return res
    
def somme_colonnes(tableau):
    ''' Retourne une liste contenant la somme de chaque ligne du tableau.
    :param tableau: (list of list) Un tableau à 2 dimensions
    :return: (list) Une liste contenant la somme de chaque ligne
    :CU: Les lignes du tableau font toutes la même taille.
    
    :Exemple:
    >>> somme_colonnes([[1,5,2,3], [4,2,3,1], [6,3,4,4]])
    [11, 10, 9, 8]
    '''
    nb_colonnes, nb_lignes = len(tableau[0]), len(tableau)
    somme = [0] * nb_colonnes  # Créer une liste dont la taille correspond au nb de colonnes, avec que des 0.
    for i in range(nb_colonnes):
        for j in range(nb_lignes):
            somme[i] += tableau[j][i]
    return somme


# Les lignes suivantes permettent d'activer les tests des fonctions.
if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    