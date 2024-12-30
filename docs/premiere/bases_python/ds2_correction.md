# Correction DS n°2

!!! tip "Énoncé du DS"
    <center style="font-size: 1.3em">
    [Télécharger l'énoncé du DS](ds2/DS2.pdf)
    </center>

## Représentation des données

!!! tip "Exercice 1"
    On écriera chaque **nombre entier** sur **8 bits**.

    $42 = 00101010$  
    $~~~~~~~~~~11010101$ (complément à 1)  
    $~~~~~~~~~~11010110 = -42$ (après complément à 2)

    $120 = 01111000$  
    $~~~~~~~~~~10000111$ (complément à 1)  
    $~~~~~~~~~~10001000 = -120$ (après complément à 2)

!!! tip "Exercice 2"
    $32,375 = 100000,011 = 1,00000011 \times 2^5$

    $s = 1$ (car *négatif*)  
    $e = 5 + 127 = 132_{10} = 10000100_{2}$  
    $f = 00000011000000000000000$

    Donc le résultat est :

    $1~10000100~00000011000000000000000$

!!! tip "Exercice 3"
    $s = 0$ (donc nombre *positif*)  
    $e = 10000101_{2} = 133_{10}$  
    Donc $e' = 133 - 127 = 6$

    $1,0010111 \times 2^6 = 1001011,1_{2} = 75,5_{10}$

!!! tip "Exercice 4"
    Il y a $2^7 = 128$ caractères possibles en **ASCII**.

!!! tip "Exercice 5"
    En **hexadécimal** : 53 61 6C 75 74 20 21  
    En **binaire** : 1010011 1100001 1101100 1110101 1110100 0100000 0100001

!!! tip "Exercice 6"
    Attention, `ord` renvoie une valeur **décimale** (et non *hexadécimale*), et `chr` prend également en entrée une valeur **décimale**.

    ```python
    >>> ord('%')
    37
    >>> chr(64)
    @
    ```

!!! tip "Exercice 7"

    ```python
    def printASCII(s):
        for car in s:  # pour chaque caractère de s
            print(hex(ord(car)))
    ```

## Programmation Python

!!! tip "Exercice 1"
    Il suffit pour cela d'additionner `a` et `b` et de **diviser par 2**, en utilisant l'opérateur `//` afin d'obtenir un entier :

    ```python
    def milieu(a, b):
        ''' Renvoie l'entier du milieu compris entre a et b.
        :param a: (int) un entier
        :param b: (int) un autre entier
        :return: (int) l'entier du milieu compris entre a et b '''

        return a + b // 2
    ```

!!! tip "Exercice 2"
    
    ```python
    def verifier_admission(age, moyenne, formation):
        ``` Renvoie True si les conditions d'admission sont respectées, False sinon.
        :param age: (int) Un âge
        :param moyenne: (float) Une moyenne
        :param formation: (str) Une formation
        :return: (bool) True ou False ```

        if age >= 18 and moyenne >= 12 and (formation == "mathématiques" or formation == "informatique" or formation == "physique"):
            return True
        else:
            return False
    ```

!!! tip "Exercice 3"

    ```python
    def pairs_impairs(nb, choix):
        ''' Affiche les entiers pairs ou impairs de 0 à nb, selon le choix indiqué.
        :param nb: (int) un nombre entier
        :param choix: (str) le choix donné, "pairs" ou "impairs"
        :return: (None) pas de valeur de retour '''

        if choix == "pairs":
            for i in range(nb+1, 2):
                print(i)
        elif choix == "impairs":
            for i in range(1, nb+1, 2):
                print(i)
        else:
            print("Choix incorrect")
    ```

!!! tip "Exercice 4"

    ```python
    from random import randint
    r = randint(1, 100)  # générer une valeur aléatoire
    saisie = input("Saisissez un nombre entre 1 et 100 : ")
    while saisie != r:  # tant que le nombre n'a pas été trouvé
        if r < saisie:
            print("C'est moins")
        else:
            print("C'est plus")
    print("C'est gagné !")
    ```

!!! tip "Exercice 5"

    ```python
    from random import randint

    def atteindre_objectif(objectif):
        compteur = 0
        progression = 0  # initialiser la progression
        print("Progression actuelle : 0")
        while progression < objectif:  # tant que l'on a pas attteint l'objectif
            compteur += 1  # incrémenter le compteur
            ajout = randint(1, 10)  # générer valeur à ajouter aléatoirement
            print("Ajouté :", ajout)  # afficher valeur d'ajout
            progression += ajout  # ajouter valeur à progression
            print("Progression actuelle :", progression)  # afficher la nouvelle progression
        print("Objectif atteint en", compteur, "essais !")
    ```