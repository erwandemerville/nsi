# Exercices

!!! note "Exercice 1"
    Dans l'**interpréteur Python**, saisissez **une à une** les **instructions** suivantes :
    ```python
    >>> a = 2
    >>> b = 6
    >>> b = b + 8
    >>> b = a
    >>> c = a + b
    ```

    Saurez-vous deviner la valeur de `c` après exécution de ces **instructions** ?  
    (Vérifiez dans la **console de Thonny**.)

!!! note "Exercice 2"
    Dans l'**interpréteur Python**, saisissez le calcul mathématique suivant et déterminez le **résultat** :

    $$ \frac{8 \times 7}{2^{4} + 16} $$

{% if exercices.premiere.bases_python.introduction.exo2 %}
??? tip "Correction exercice 2"
    ```python
    (8 * 7) / (2**4 + 16)
    ```
{% endif %}

!!! note "Exercice 3"
    Copiez-collez le **code suivant** dans un nouveau **programme Python** :

    ```python
    a = ...
    b = ...
    c = ...
    if a < b and c < b and c < a:
        print("OK")
    else:
        print("PAS OK")
    ```

    Remplacez les `...` par des **nombres entiers**, de manière à ce que le programme **affiche** `"OK"`.

{% if exercices.premiere.bases_python.introduction.exo3 %}
??? tip "Correction exercice 3"
    Par exemple :

    ```python
    a = 2
    b = 5
    c = 1
    if a < b and c < b and c < a:
        print("OK")
    else:
        print("PAS OK")
    ```
{% endif %}

!!! note "Exercice 4"
    Dans un **nouveau programme** :

    - **créer une variable** `nombre` et affectez-lui un **nombre entier** entre `1` et `100` (celui que vous voulez),
    - écrire une **structure de branchement** telle que :
        - SI `nombre` est **égal à** `50`, on affiche `"Bingo"`,
        - SINON SI `nombre` est **plus petit** que `50`, on affiche `"Trop petit..."`,
        - SINON, on affiche `"Trop grand..."`.

{% if exercices.premiere.bases_python.introduction.exo4 %}
??? tip "Correction exercice 4"

    ```python
    nombre = 25
    if nombre == 50:
        print("Bingo")
    elif nombre < 50:
        print("Trop petit...")
    else:
        print("Trop grand...")
    ```
{% endif %}

Pour les 3 exercices suivants, on utilisera la fonction `input()` pour demander une saisie à l'utilisateur.

!!! note "Exercice 5"
    Écrire un **programme** qui **demande à l'utilisateur** de saisir un **premier nombre entier**, puis un **deuxième nombre entier**, et qui **affiche** le **produit** de **ces deux nombres**.

{% if exercices.premiere.bases_python.introduction.exo5 %}
??? tip "Correction exercice 5"

    ```python
    nombre1 = int(input("Saisir un premier nombre : "))
    nombre2 = int(input("Saisir un deuxième nombre : "))
    print(nombre1 * nombre2)
    ```
{% endif %}

!!! note "Exercice 6"
    Écrire un **programme** qui **demande à l'utilisateur** de saisir **deux nombres**, et qui **affiche** le **quotient** et le **reste** de la **division euclidienne** entre ces deux nombres.

    On affichera un message de la forme :

    `"Le quotient est <quotient> et le reste est <reste>."`  
    en remplaçant `<quotient>` par le quotient obtenu, et `<reste>` par le reste obtenu.

{% if exercices.premiere.bases_python.introduction.exo6 %}
??? tip "Correction exercice 6"

    ```python
    nombre1 = int(input("Saisir un premier nombre : "))
    nombre2 = int(input("Saisir un deuxième nombre : "))
    print("Quotient :", nombre1 // nombre2, "- Reste :", nombre1 % nombre2)
    ```
{% endif %}

!!! note "Exercice 7"
    Écrire un **programme** qui **demande à l'utilisateur** de saisir **deux nombres entiers** ainsi qu'un **opérateur** (`+`, `*`, `-`, `/`) et qui effectue le **calcul** entre les **deux nombres donnés** avec **l'opérateur donné**.  
    En cas de **division par zéro**, on **affichera** un **message d'erreur**.

{% if exercices.premiere.bases_python.introduction.exo7 %}
??? tip "Correction exercice 7"

    ```python
    nombre1 = int(input("Saisir un premier nombre : "))
    nombre2 = int(input("Saisir un deuxième nombre : "))
    operateur = input("Saisir un opérateur : ")
    if operateur == '+':
        print("Résultat :", nombre1 + nombre2)
    elif operateur == '-':
        print("Résultat :", nombre1 - nombre2)
    elif operateur == '*':
        print("Résultat :", nombre1 * nombre2)
    else:
        if nombre2 == 0:
            print("Erreur : Division par zéro")
        else:
            print("Résultat :", nombre1 / nombre2)
    ```
{% endif %}

# Exercices sur les boucles bornées `for`

!!! note "Exercice 8"
    Écrire un **programme** qui **affiche 20 fois** le message `"HELLO"`.

{% if exercices.premiere.bases_python.introduction.exo8 %}
??? tip "Correction exercice 8"

    ```python
    for i in range(20):
        print("HELLO")
    ```
{% endif %}

!!! note "Exercice 9"
    Écrire un **programme** qui **affiche tous les nombres** de **1** à **50**.

{% if exercices.premiere.bases_python.introduction.exo9 %}
??? tip "Correction exercice 9"

    ```python
    for i in range(1, 51):
        print(i)
    ```
{% endif %}

!!! note "Exercice 10"
    Écrire un **programme** qui **affiche tous les nombres pairs** de **2** à **98**.

{% if exercices.premiere.bases_python.introduction.exo10 %}
??? tip "Correction exercice 10"

    ```python
    for i in range(2, 99, 2):
        print(i)
    ```
{% endif %}

!!! note "Exercice 11"
    Écrire un **programme** qui **demande à l'utilisateur** de saisir :

    - un **message** (`str`)
    - un **nombre de répétitions** (`int`)

    et qui **affiche** le **message saisi** répété le **nombre de fois saisi**.

{% if exercices.premiere.bases_python.introduction.exo11 %}
??? tip "Correction exercice 11"

    ```python
    message = input("Saisissez un message : ")
    nb = int(input("Nombre de répétitions : "))
    while i in range(nb):  # itérer nb fois
        print(message)  # afficher le message
    ```
{% endif %}

!!! note "Exercice 12"
    Écrire un **programme** qui **demande à l'utilisateur** de saisir **2 nombres entiers**, et qui calcule et affiche le **produit** des **deux nombres** ==SANS UTILISER== le symbole `*`.

{% if exercices.premiere.bases_python.introduction.exo12 %}
??? tip "Correction exercice 12"

    ```python
    nombre1 = int(input("Saisir un premier nombre : "))
    nombre2 = int(input("Saisir un deuxième nombre : "))
    resultat = 0  # initialiser le résultat à 0
    for i in range(nombre1):  # itérer 'nombre1' fois
        resultat = resultat + nombre2  # ajouter le nombre2 au résultat
        # on pourrait aussi écrire "total += nombre 2"
    print("Résultat : ", resultat)
    ```
{% endif %}

# Exercices sur les boucles non-bornées `while`

Si besoin, vous pouvez consulter [cette partie du cours](https://nsi.erwandemerville.fr/premiere/bases_python/introduction/#les-boucles-non-bornees-while).

!!! note "Exercice 13"
    Écrire un **programme** qui répète **15 fois** le message `"COUCOU"` à l'aide d'une boucle `while`.

??? tip "Aide exercice 13 - Code à trous"
    ```python
    i = ...         # initialiser variable utilisée dans la boucle
    while i < ...:  # TANT QUE (compléter la condition d'entrée dans la boucle)
        print(...)  # afficher "COUCOU"
        ...         # incrémenter i
    ```

!!! note "Exercice 14"
    Écrire un **programme** qui **affiche** tous les **entiers impairs** de `1` à `97` à l'aide d'une **boucle** `while`.

??? tip "Aide exercice 14 - Code à trous"
    ```python
    i = ...         # initialiser variable utilisée dans la boucle
    while ...:      # TANT QUE (compléter la condition d'entrée dans la boucle)
        print(...)
        ...         # incrémenter la variable de boucle
    ```

!!! note "Exercice 15"
    Écrivez un **programme** en Python qui **demande à l'utilisateur** d'entrer un **nombre entier positif** `n`. Ensuite, utilisez une boucle `while` pour calculer la **somme** de **tous les entiers pairs** de `2` à `n`. **Affichez** ensuite le résultat.

??? tip "Aide exercice 15 - Code à trous"
    ```python
    n = ...         # demander la saisie d'un nombre entier positif
    somme = ...     # initialiser une variable 'somme'
    i = ...         # initialiser variable utilisée dans la boucle
    while ...:      # TANT QUE (compléter la condition d'entrée dans la boucle)
        somme = ... + ...
        ...         # incrémenter la variable de boucle
    print("Résultat : ", ...)  # afficher le résultat
    ```

!!! note "Exercice 16"
    On souhaite écrire un programme permettant de restreindre l'accès à une plateforme aux visiteurs adultes.

    Écrire un **programme** qui :

    - demande à l'utilisateur son **âge**,
    - **tant que** l'**âge** est **inférieur** à **18** ans, on redemande l'âge.
    - Si l'âge est d'au moins **18** ans, on affiche "Vous pouvez entrer".

??? tip "Aide exercice 16 - Code à trous"
    ```python
    age = ...       # demander à l'utilisateur son âge
    while ...:      # TANT QUE l'âge est inférieur à 18 ans
        ...         # on redemande son âge à l'utilisateur
    # On sort de la boucle lorsque l'utilisateur a indiqué avoir au moins 18 ans
    ...             # afficher le message "Vous pouvez entrer"
    ```

!!! note "Exercice 17"
    On veut écrire une **simulation du jeu de Monopoly**.  
    Un joueur peut rejouer s'il fait un **double**.

    Mais attention ! S'il fait **trois doubles de suite**, il doit aller en **prison**.

    Le **programme** à concevoir doit :

    - **Simuler le lancer** aléatoire de deux dés à 6 faces (vous utiliserez la fonction `randint` du module `random`.);
    - **Afficher la valeur** de chaque face ainsi que le nombre de cases à parcourir ;
    - **Relancer les dés** dans le cas d'un double ;
    - **Recommencer**... et envoyer le joueur en prison s'il y a **trois doubles de suite**.

    Un exemple d'affichage avec envoi en prison :

    ```python
    Les faces sont 5 et 5 : Avancez de 10 cases.
    Il y a un double, rejouez.
    Les faces sont 2 et 2 : Avancez de 4 cases.
    Il y a un double, rejouez.
    Les faces sont 6 et 6 : Avancez de 12 cases.
    Oups ! Encore un double, allez en prison !
    ```

??? tip "Aide exercice 17 - Code à trous"
    ```python
    from random import randint
    
    de1 = randint(1, 6)  # simuler un premier lancer de dé
    de2 = ...            # simuler un second lancer de dé
    compteur = 0         # compteur du nombre de doubles, initialisé à 0
    print(...)           # afficher valeurs des dés et nombre de cases à parcourir
    while ... and ...:   # TANT QUE (indiquer les deux conditions à vérifier)
        ...              # afficher le message "Il y a un double, rejouez."
        de1 = ...        # re-simuler un premier lancer de dé
        de2 = ...        # re-simuler un second lancer de dé
    # On sort de la boucle
    if ...:              # s'il y a eu 3 doubles
        ...              # afficher le message "Vous allez en prison !"
    ```