# ===> PROGRAMME 4 <===

def trouver(liste, element):
    ''' Renvoie True si element est dans liste, False sinon.
    :param liste: (list) Une liste d'entiers
    :param element: (int) Un entier à chercher dans la liste
    :return: (bool) True si l'élément est trouvé, False sinon
    
    :Exemples:
    >>> trouver([2,5,3,1,8,9], 4)
    False
    >>> trouver([2,5,3,1,8,9], 8)
    True
    '''
    
    ...
    
def dichotomie(liste, element):
    ''' Renvoie True si element est dans la liste triée, False sinon.
    :param liste: (list) Une liste d'entiers triée
    :param element: (int) Un entier à chercher dans la liste
    :return: (bool) True si l'élément est trouvé, False sinon
    :CU: La liste 'liste' est triée
    
    :Exemples:
    >>> dichotomie([1,3,5,6,7,9], 5)
    True
    >>> dichotomie([1,3,5,6,7,9], 4)
    False
    '''
    debut = 0  # Indice du début de la liste
    fin = ...  # Indice de fin de la liste
    while debut <= fin:  # Tant qu'il reste des éléments dans la partie de la liste entre debut et fin
        m = ...  # Indice de l'élément du milieu entre debut et fin
        if liste[m] == ...:
            # On a trouvé element
            return ...
        elif ...:  # v se situe après l'élément du milieu
            debut = m + 1  # On change le début de la partie de la liste sur laquelle on cherche
        else:  # v se situe avant l'élément du milieu
            fin = m - 1  # On change la fin de la partie de la liste sur laquelle on cherche
    # on a debut > fin
    return False


# Les lignes suivantes permettent d'activer les tests des fonctions.
if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    