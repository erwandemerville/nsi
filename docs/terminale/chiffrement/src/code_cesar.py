ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N' \
            ,'O','P','Q','R','S','T','U','V','W','X','Y','Z']

def obtenir_indice(lettre):
    ''' Prend une lettre de l'alphabet, et renvoie son indice.
    :param lettre: (str) une lettre de l'alphabet
    :return: (int) l'indice de la lettre dans ALPHABET '''
    
    for i in range(len(ALPHABET)):
        if ALPHABET[i] == lettre:
            return i
    return -1

def chiffrer_message(m, d):
    """Chiffre un message en utilisant le chiffrement de César.
    :param m: (str) Le message à chiffrer.
    :param d: (int) Le nombre de décalages à effectuer.
    :return: (str) Le message chiffré
    :CU: all([c in ALPHABET + [' '] for c in m])"""
    
    resultat = ''
    for el in m:
        if el in ALPHABET:
            resultat += ALPHABET[(obtenir_indice(el) + d) % 26]
        else:
            resultat += ' '
    return resultat
    

def dechiffrer_message(m, d):
    """Chiffre un message en utilisant le chiffrement de César.
    :param m: (str) Le message à chiffrer.
    :param d: (int) Le nombre de décalages à effectuer.
    :return: (str) Le message chiffré
    :CU: all([c in ALPHABET + [' '] for c in m])"""
    
    resultat = ''
    for el in m:
        if el in ALPHABET:
            resultat += ALPHABET[(obtenir_indice(el) - d) % 26]
        else:
            resultat += ' '
    return resultat

def bruteforce(message):
    ''' Déchiffre le message sans connaître sa clé de chiffrement
    avec un test de force brute. '''
    
    for cle in range(0, 26):
        print(dechiffrer_message(message, cle))
