# Cours - Chiffrement et protocole HTTPS

## Introduction

En **première**, vous avez étudié les notions suivantes :

- [Le principe des communications réseau et le modèle OSI](../../premiere/reseau/cours.md)
- [Les interactions client-serveur et les requêtes HTTP](../../premiere/interactions/clientserveur.md)
- [L'envoi de requêtes POST et GET avec des formulaires](../../premiere/interactions/clientserveur.md)

On sait que les données sont découpées en segments **TCP**, encapsulés dans des paquets **IP**.
Ces données sont transmises de **routeurs en routeurs** jusqu'à la destination.

!!! warning "Danger"
    Mais il y a un problème : Les données peuvent être interceptées entre l'**émetteur** et le **récepteur**. On appelle cela une "Attaque par Homme du milieu".  
    Cela représente un **risque pour les données sensibles** (données bancaires, messages privés, etc.)

!!! question ""
    Ainsi, comment peut-on, avec des **communications TCP/IP** :

    - Chiffrer le contenu des communications ?
    - Garantir l'intégrité du serveur auquel on souhaite se connecter ?

## Chiffrement symétrique

### Principe

Le **chiffrement symétrique** consiste en deux fonctions :

- $c(m,k)$ : fonction de *chiffrement*.  
$m$ un message en clair et $k$ une clé de chiffrement.
- $d(s,k)$ : fonction de *déchiffrement*.  
$s$ un message chiffré et $k$ une clé de déchiffrement.

La **même clé** est utilisée pour **chiffrer** et **déchiffrer**. C'est là la particularité du **chiffrement symétrique**.

On a ainsi la relation suivante : $d(c(m,k),k)=m$

### Un exemple : le codage de César

Le **chiffrement de César** ou **Code César** est une méthode de **chiffrement symétrique** par **substitution**.  
La **clé** de **chiffrement/déchiffrement** est ici un **nombre de décalages** tel que :

- On **décale vers la droite** pour *chiffrer*,
- On **décale vers la gauche** pour *déchiffrer*.

Voici une **implémentation Python** de ce chiffrement :

```python
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

```

### Autre exemple : chiffrement de Vernam

Le **chiffrement de Vernam** repose sur l'utilisation de l'opérateur binaire **ou exclusif** (**XOR**).

!!! abstract "Règles de Shannon"
    Shannon a démontré **3 règles** permettant rendre le système **inviolable** :

    1. La **clé** doit être une **chaîne de même longueur** que le **message à chiffrer**.
    2. Les **caractères** composant la **clé** doivent être choisis de manière **aléatoire**.
    3. Chaque **clé** (ou "masque") ne doit être utilisée qu'**une seule fois**.

Un avantage de l'opérateur **XOR** est qu'il est **réversible**.

Ainsi, si on note $M$ un **message** et $S$ la **clé de chiffrement**, on a : $(M⊕S)⊕S=M$

En Python :

```python
from random import choice
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N' \
            ,'O','P','Q','R','S','T','U','V','W','X','Y','Z','$','%' \
            ,'?','!','*',' ']  # 32 lettres = 5 bits

def lettre(n):
    return alphabet[n]
    
def code(l):
    return alphabet.index(l)

def cle_aleatoire(taille):
    return ''.join([choice(alphabet) for _ in range(taille)])

def chiffrer_dechiffrer_vernam(m, cle):
    """Chiffre/déchiffre un message avec le chiffrement de Vernam.
    :param m: (str) Le message à chiffrer.
    :param s: (str) La clé de chiffrement/déchiffrement."""
    
    res = ''
    for i in range(len(m)):
        res += lettre((code(m[i]) ^ code(cle[i])) % len(alphabet))
    return res

message_clair = "BONJOUR A TOUS"
cle = cle_aleatoire(len(message_clair))
message_chiffre = chiffrer_dechiffrer_vernam(message_clair, cle)
'Message : ' + message_chiffre + ' - Clé : ' + cle
```

### Autres chiffrements...

D'autres **méthodes de chiffrement symétrique** très complexes, utilisés dans la vraie vie, existent :

- [AES](https://fr.wikipedia.org/wiki/Advanced_Encryption_Standard) : Advanced Encryption Standard (standard de chiffrement avancé)
- **ChaCha20**

Ils reposent toutefois également sur un chiffrement **XOR**.
