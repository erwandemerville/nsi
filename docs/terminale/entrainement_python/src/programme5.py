# ===> PROGRAMME 5 <===

def compter(mot, lettre):
    ''' Renvoie le nombre d'occurences de lettre dans mot.
    :param mot: (str) Un mot
    :param lettre: (str) Une lettre
    :return: (int) Le nombre d'occurences de lettre dans mot
    
    :Exemple:
    >>> compter('bonjour', 'o')
    2
    '''
    
    ...
    
def supprimer(mot, lettre):
    ''' Renvoie un mot en lui retirant une lettre spécifiée.
    :param mot: (str) Un mot
    :param lettre: (str) La lettre à supprimer du mot
    :return: (str) Le mot initial sans la lettre spécifiée
    
    :Exemple:
    >>> supprimer('bonjour', 'o')
    'bnjur'
    '''
    
    ...
    
def recherche(chaine, sequence):
    ''' Recherche une séquence dans une chaîne, renvoie True si elle est trouvée,
    False si elle ne l'est pas.
    :param chaine: (str) Une chaîne de caractères
    :param sequence: (str) La séquence à chercher
    :return: (bool) True ou False selon si la séquence est trouvée ou non
    
    :Exemple:
    >>> recherche('abaabcbbca', 'baab')
    True
    >>> recherche('abccbca', 'bbc')
    False
    '''
    
    n = len(chaine)
    g = len(sequence)
    i = ...
    trouve = False
    while i < ... and trouve == ... :
        j = 0
        while j < g and sequence[j] == chaine[i+j]:
            ...
        if j == g:
            trouve = True
        ...
    return trouve


# Les lignes suivantes permettent d'activer les tests des fonctions.
if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
