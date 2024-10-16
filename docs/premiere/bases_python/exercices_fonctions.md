# Exercices sur les fonctions

Voici quelques exercices portant sur les **fonctions** en *Python*.

!!! note "Exercice 1"
    **Téléchargez** le fichier suivant et ouvrez-le dans **Thonny** :

    <center style="font-size: 1.3em">
    [Télécharger `exo1_fonctions.py`](scripts/exo1_fonctions.py)
    </center>

    **Complétez** les **fonctions** `est_pair`, `plus_grand` et `produit` en respectant la **documentation** (voir explications sur les **docstrings** plus bas).

    Voici quelques *exemples* d'appels à ces fonctions dans la **console** :

    ```python
    >>> est_pair(12)
    True
    >>> est_pair(15)
    False
    >>> plus_grand(5, 8, 3)
    8
    >>> plus_grand(7, 7, 7)
    7
    >>> produit(4, 8)
    32
    ```

    !!! tip "Les **docstrings**"
        Pour comprendre ce que doivent **renvoyer** ces fonctions, et quels sont leurs **paramètres**, lisez leurs **documentations**. Les documentations des fonctions sont écrites sous la forme de **commentaires multilignes**, que l'on appelle des **==docstrings==**. Par exemple, voici la **==docstring==** de la fonction `est_pair` :

        ```python
        ''' Renvoie True si l'entier positif n est pair, False sinon.
        :param n: (int) un entier positif
        :return: (bool) True ou False '''
        ```

        Cette **docstring** indique que la **fonction** doit **renvoyer** un *booléen*, `True` ou `False`, selon si la **paramètre** `n` (un *entier*) est **pair** ou non.  
        À noter qu'il n'y a pas vraiment de convention sur la manière d'écrire une **docstring**. Toutefois, il doit au minimum y figurer :

        - ce que fait la fonction,
        - les paramètres d'entrée et leur type,
        - la valeur de retour et son type.

??? tip "Correction - Exercice 1"
    La fonction `est_pair` peut être écrite naïvement de la manière suivante :

    ```python
    def est_pair(n):
    ''' Renvoie True si l'entier positif n est pair, False sinon.
    :param n: (int) un entier positif
    :return: (bool) True ou False '''

    if n % 2 == 0:
        return True
    else:
        return False
    ```

    Cependant, on peut l'écrire plus simplement de la manière suivante :

    ```python
    def est_pair(n):
    ''' Renvoie True si l'entier positif n est pair, False sinon.
    :param n: (int) un entier positif
    :return: (bool) True ou False '''

    return n % 2 == 0
    ```

    En effet, *Python* va d'abord **évaluer** l'expression `n % 2 == 0`, qui sera évaluée à `True` ou à `False`, et cette valeur sera **renvoyée** par le `return`.

    La fonction `plus_grand` peut être écrite avec une suite d'**instructions de branchement** `if... elif... else`, en combinant plusieurs tests à l'aide de l'opérateur `and` :

    ```python
    def plus_grand(a, b, c):
        ''' Renvoie la plus grande valeur parmi les trois entiers donnés en entrée.
        :param a: (int) un entier
        :param b: (int) un entier
        :param c: (int) un entier
        :return: (int) le plus grand des trois entiers '''

        if a >= b and a >= c:  # si a est plus grand que b et plus grand que c
            return a  # renvoyer a
        elif b >= a and b >= c:  # si b est plus grand que a et plus grand que c
            return b  # renvoyer b
        else:  # sinon
            return c  # renvoyer c
    ```

    Enfin, la fonction `produit` peut être écrite en transformant le **produit** en **somme**. On utilisera pour cela une boucle `for` :

    ```python
    def produit(x, y):
        ''' Effectue le produit entre x et y SANS UTILISER LE SYMBOLE *.
        :param x: (int) un entier positif
        :param y: (int) un autre entier positif
        :return: (int) résultat du produit des deux entiers '''

        somme = 0  # initialiser la variable qui contiendra le résultat
        for i in range(y):  # itérer y fois
            somme += x  # ajouter x à la somme
        return somme  # renvoyer la somme des x
    ```

!!! note "Exercice 2"
    Dans un nouveau **script Python**, écrire une fonction `compter_voyelles` qui reçoit une **chaîne de caractères** `mot` en entrée et **renvoie** le **nombre de voyelles** ("a", "e", "i", "o", "u", "y") présentes dans ce mot.

    Exemple :

    ```python
    print(compter_voyelles("python"))  # 2
    print(compter_voyelles("ananas"))  # 3
    ```

    Ensuite, **en-dessous de la fonction**, écrire un **programme** qui demande à l'utilisateur de saisir un **mot**, puis afficher le **nombre de voyelles** de ce mot en faisant appel à `compter_voyelles`.

??? tip "Correction - Exercice 2"
    Pour **compter** le **nombre de voyelles**, il faut **parcourir chaque caractère** du **mot** donné en **entrée** et **incrémenter un compteur** à chaque fois qu'une voyelle est trouvée.

    ```python
    def compter_voyelles(mot):
        ''' Renvoie ne nombre de voyelles du mot donné en entrée.
        :param mot: (str) un mot
        :return: (int) le nombre de voyelles du mot '''

        compteur = 0  # initialiser un compteur à 0
        for lettre in mot:  # pour chaque lettre du mot
            if lettre in "aeiouy":  # si la lettre est dans la chaîne "aeiouy"
                compteur += 1  # incrémenter le compteur (augmenter de 1)
        return compteur  # renvoyer le compteur
    ```

    Ensuite, on crée un **programme** qui demande à l'utilisateur de saisir un **mot** et qui affiche le **nombre de voyelles** de ce mot :

    ```python
    m = input("Saisissez un mot : ")  # demander à l'utilisateur la saisie d'un mot
    nb_voyelles = compter_voyelles(m)  # calculer le nombre de voyelles du mot
    print("Le nombre de voyelles est : ", nb_voyelles)  # afficher le résultat obtenu
    ```

!!! note "Exercice 3"
    Écrire une fonction `factorielle` qui reçoit **un nombre entier** `nombre` en **entrée** et **renvoie** la **factorielle** de ce nombre. [Cliquez ici](https://fr.wikipedia.org/wiki/Factorielle) pour un rappel de ce qu'est une **factorielle**.

    Exemple :

    ```python
    print(factorielle(5))  # Affiche 120
    print(factorielle(7))  # Affiche 5040
    ```

    Ensuite, **en-dessous de la fonction**, écrire un **programme** qui demande à l'utilisateur de saisir un **nombre entier**, puis qui affiche la **factorielle** de ce nombre en appelant `factorielle`.

??? tip "Correction - Exercice 3"
    On peut écrire la **fonction** `factorielle` de la manière suivante :

    ```python
    def factorielle(n):
        ''' Renvoie la factorielle d'un nombre n donné en entrée.
        :param n: (int) un entier positif ou nul
        :return: (int) la factorielle du nombre n '''

        res = 1  # initialiser la variable qui contiendra le résultat
        for i in range(1, n+1):  # i prendra chaque valeur de 1 jusqu'à n
            res = res * i  # ou res *= i, multiplier res par la valeur de i courante
        return res  # renvoyer le résultat
    ```

    Enfin, on écrit un **programme** qui demande à l'utilisateur de saisir un **nombre entier**, et **appelle** `factorielle` pour **calculer la factorielle** de ce nombre.

    ```python
    nb = int(input("Saisissez un nombre entier positif : "))  # demander de saisir un entier positif
    print(factorielle(nb))  # appeler factorielle avec l'argument nb, et afficher la valeur renvoyée
    ```

!!! note "Exercice 4"
    Écrire une fonction `trouver_le_nombre`, qui prend un **entier** `nombre` entre `1` et `100` en **entrée**, et qui :

    - demande à l'utilisateur de **saisir un nombre** entre 1 et 100,
    - si le nombre saisi correspond au nombre généré :
        - on **affiche** `"Gagné !"` et on **renvoie** `True` (et donc la fonction s'arrête),
    - sinon :
        - si le nombre à trouver `nombre` est **plus petit** que le nombre saisi :
            - on **affiche** `"Perdu, c'est moins..."` et on **renvoie** `False`.
        - sinon :
            - on **affiche** `"Perdu, c'est plus..."` et on **renvoie** `False`.

    ---

    On souhaite ensuite écrire un **programme** réutilisant `trouver_le_nombre` qui :

    - génère un **nombre aléatoire** à l'aide de `randint`,
    - initialise une **variable** `trouve` à `False`,
    - effectue une **boucle** de **5 itérations**, dans laquelle :
        - si `trouve` **est égal à** `False`, on appelle `trouver_le_nombre` pour demander à l'utilisateur de saisir un nombre, et :
            - si la **valeur renvoyée** par `trouver_le_nombre` vaut `True`, on affecte `True` à `trouve`.
            - sinon, on ne fait rien.

    Voici le squelette de ce programme, vous pouvez le **copier/coller** et remplacer les *pointillés* par le code approprié :

    ```python
    from random import randint
    nombre_aleatoire = ...
    trouve = ...
    for ... in range(...):
        if ...:
            resultat = ...
            if resultat == ...:
                trouve = ...
            else:
                trouve = ...
    ```