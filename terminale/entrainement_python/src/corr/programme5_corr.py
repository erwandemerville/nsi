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
    
    res = 0
    for l in mot :
        if l == lettre:
            res += 1
    return res

def compter_version2(mot, lettre):
    ''' Avec la fonction count. '''
    return mot.count(lettre)
    
def supprimer(mot, lettre):
    ''' Renvoie un mot en lui retirant une lettre spécifiée.
    :param mot: (str) Un mot
    :param lettre: (str) La lettre à supprimer du mot
    :return: (str) Le mot initial sans la lettre spécifiée
    
    :Exemple:
    >>> supprimer('bonjour', 'o')
    'bnjur'
    '''
    
    res = ''
    for l in mot:
        if l != lettre:
            res += l
    return res
    
def recherche(chaine, sequence):
    ''' Recherche une séquence dans une chaîne, renvoie True si elle est trouvée,
    False si elle ne l'est pas.
    :param chaine: (str) Une chaîne de caractères
    :param sequence: (str) La séquence à chercher dans la chaîne
    :return: (bool) True ou False selon si la séquence est trouvée ou non
    
    :Exemple:
    >>> recherche('abaabcbbca', 'baab')
    True
    >>> recherche('abccbca', 'bbc')
    False
    '''
    
    n = len(chaine)  # n prend la valeur de la taille de la chaine
    g = len(sequence)  # g prend la valeur de la taille de la séquence à chercher dans la chaîne
    i = 0  # L'indice i correspond à la position dans la séquence (initialement 0)
    trouve = False
    while i < n - g and trouve == False :  # Voir la note 1 en dessous
        j = 0  # L'indice j correspond à la position dans le gène, initialisée à 0
        while j < g and sequence[j] == chaine[i+j]:  # Tant que l'élément de la séquence correspond à l'élément du gène
            j += 1  # On incrémente j
        if j == g:  # Si j a la valeur de la taille du gène (ce qui signifie qu'on a trouvé tout le gène)
            trouve = True  # On passe "trouve" à True (vrai)
        i += 1  # On incrémente i
    return trouve  # On retourne le booléen trouve (qui vaut True ou False)

# Note 1 : La boucle continue tant que l'on a pas trouvé toute la séquence,
# et s'arrête à n - g car si on s'arrête à n (au bout de la chaîne),
# on peut avoir une erreur si par exemple on fait recherche("gccd", "gtacaaatcttgcc")
# car lors de la comparaison de la chaîne et de la séquence, on dépassera la taille de la chaîne.

# Les lignes suivantes permettent d'activer les tests des fonctions.
if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
