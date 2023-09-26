# Correction du DM 1

!!! success "Télécharger le DM"
    - [DM1.pdf](dm1/DM1.pdf){ target="_blank" } - Énoncé du DM 1.

## Correction partie papier

!!! tip "Exercice 1 - Vrai ou Faux ?"
    1. Après les instructions `x = 3`, `y = 5`, `x = y`, `y = x`, la valeur de x est 5 et la valeur de y est 3.  
    <span style="color:green">C'est ***faux***. Pour inverser les valeurs de `x` et de `y`, on a besoin d'une **troisième variable temporaire** pour y stocker l'une des deux valeurs. Sinon, la valeur de `x` est perdue car la variable prend la valeur de `y`. Une solution :
    ```python
    x = 3
    y = 5
    temp = x
    x = y
    y = temp
    ```
    </span>
    2. Après les instructions `x = 3`, `y = 5`, `y == x`, `x = y`, la valeur de `x` est `5` et la valeur de `y` est `5`.  
    <span style="color:green">C'est ***vrai***. Ici, la troisième instruction effectue une **comparaison** (il y a deux `=` et pas un), et non pas une **affectation**. Cette expression booléenne renvoie `True` ou `False`, mais la valeur n'est stockée nul part. La variable `x` prend ensuite la valeur de `y`, donc `5`.</span>

    3. L’instruction `print(bonjour)` va afficher `"bonjour"`.  
    <span style="color:green">C'est ***faux***. La fonction `print` permet d'**afficher** une **chaîne de caractères**. Ici, `bonjour` n'est pas entouré de **guillemets**, et est donc considéré comme **une variable**. Une erreur indiquant que la variable `bonjour` n'existe pas sera donc levée.</span>

    4. La fonction `input` renvoie une chaîne de caractères.  
    <span style="color:green">C'est ***vrai***. La fonction `input` renvoie une **chaîne de caractères**. Ainsi, si l'on a besoin de transformer la valeur renvoyée par un `input` en un **nombre entier** par exemple, notamment pour utiliser la valeur dans un `range` (qui ne prend que des entiers), on peut convertir cette valeur avec la fonction `int`. Par exemple :
    ```python
    nb = int(input("Saisissez un nombre : "))
    ```
    Ici, la valeur retour de l'`input` sera convertie en **nombre entier**. ```

    5. L’instruction `if ...` est une instruction conditionnelle.  
    <span style="color:green">C'est ***vrai***. Les **instructions conditionnelles** permettent d'exécuter des blocs de code seulement **lorsqu'une condition est remplie**. Voir [cette partie du cours](cours.md#les-instructions-de-branchement){ target="_blank" }.</span>

    6. Avec `for i in range(10)`, la variable `i` prend **9 valeurs**, puisque la dernière est `9`.  
    <span style="color:green">C'est ***faux***. Une boucle `for ... in range(...)`, lorsque le `range` ne prend qu'une seule valeur, commence à l'indice `0` et se termine à l'indice indiqué dans le `range` **moins 1**. Ici, il y a donc **10 valeurs**, de **0** à **9**.</span>

    7. Avec `for i in range(9, 0, -3)`, les valeurs successives prises par la variable `i` sont `9`, `6`, `3`, `0`.  
    <span style="color:green">C'est ***faux***. Ici, le `range` contient **trois valeurs**, ce qui signifie que l'on commence à la valeur `9`, jusqu'à la valeur `0` **EXCLUE**, avec un pas de `-3`. Le `0` n'est pas pris, car on s'arrête toujours un cran avant. Ici, `i` ne prendra que les valeurs `9`, `6` et `3`.</span>

    8. Si l’on exécuté l’instruction âge = int(input("Veuillez entrer votre âge ! ")), la variable âge créée est de type str (chaîne de caractères).  
    <span style="color:green">C'est ***vrai***. `input` renvoie une valeur de type `str`, c'est-à-dire une **chaîne de caractères**.</span>

    9.  Une variable booléenne ne peut prendre que deux valeurs.  
    <span style="color:green">C'est ***vrai***. Une variable booléenne peut prendre soit la valeur `True`, soit la valeur `False`.</span>

    10. Si a = True et b = False, alors le test `b or a and b` renvoie True.  
    <span style="color:green">C'est ***faux***. Lorsque l'on effectue le test `b or a and b`, on teste d'abord `b or a`, qui ici vaut `True`, puisque `True or False = True`, puis on teste enfin `True and b`, qui vaut `False`, puise `True and False = False` (avec l'opérateur `and`, les deux variables doivent être à `True` pour obtenir `True`).</span>

!!! tip "Exercice 2"
    1. En **quelle année** le **langage Python** a t-il été créé ?  
    <span style="color:green">Le langage Python a été créé en **1991** par *Guido Van Rossum*, un informaticien néerlandais.</span>

    2. Voici 4 propositions, entourez celles qui sont **des expressions** (ici <span style="color:blue">en bleu</span>) et soulignez celles qui sont **des affectations** (ici <span style="color:green">en vert</span>) :
          1. <span style="color:green">a < b</span>
          2. <span style="color:green">a != b</span>
          3. <span style="color:blue">a = b</span>
          4. <span style="color:green">a >= b</span>

    3. On considère les **instructions** suivantes exécutées dans l’ordre : `a=8`, `b=5`, `a==b+1`, `b=b +1`, `a==b+1`, `b=b+1`, `print(a==b+1)`. Quel est le **résultat** affiché à l’issue de la dernière instruction ?  
    <span style="color:green">Le résultat obtenu à l'issue de la dernière instruction est `True`. `a` prend la valeur `8`, `b` prend la valeur `5`, ensuite, on fait une comparaison `a == b+1` qui est évaluée à `False` (car `8 != 6`), mais cette valeur `False` n'est stockée nulle part. Ensuite, on affecte à `b` la valeur `b + 1`, c'est-à-dire `6`. Donc `a = 8` et `b = 6`. On fait de nouveau une comparaison `a == b+1`, qui est évalue à `False` (car `8 != 7`). Cette valeur `False` n'est encore une fois pas stockée. On continue en affectant de nouveau à `b` la valeur `b + 1`, c'est-à-dire `7`. Finalement, on **affiche** (avec la fonction `print`) la valeur obtenue suite à l'évaluation de la comparaison `a == b + 1`, qui vaut `True` car `a = 8` et `b + 1 = 7 + 1 = 8`.</span>

    4. Voici une séquence d’instructions :  
    ```python
    n = 7
    for i in range (2 , n):
        print (i)
    ```  
    Combien de fois la fonction `print` à l'intérieur du `for` est-elle exécutée ?  
    <span style="color:green">La fonction `print` est ici exécutée **5 fois**. En effet, lorsque le `range` contient **2 valeurs**, on commence à la **première valeur** indiquée, et on s'arrête un cran avant la **deuxième valeur**. Ici, `i` prend donc les valeurs `2`, `3`, `4`, `5` et `6.`</span>

    5. Voici une séquence d’instructions :  
    ```python
    x = 4
    while x > 0:
        y = 0
        while y < x:
            y = y + 1
            x = x - 1
    ```  
    Quelles seront les **valeurs finales** de `x` et de `y` ?  
    <span style="color:green">Après exécution, `x = 0` et `y = 1`. Pour voir le déroulement complet de ce programme, vous pouvez dérouler le bloc suivant.</span>
    
    ??? quote "Déroulement du programme - Question 5"
        ```python
        Début du programme :
        x = 4
        Comparaison du premier while : x > 0
        4 > 0 ? OUI, donc on rentre dans la première boucle.
            y = 0
            Comparaison du deuxième while : y < x
            0 < 4 ? OUI, donc on rentre dans la deuxième boucle.
                y = y + 1 = 0 + 1 = 1
                x = x - 1 = 4 - 1 = 3
                Comparaison du deuxième while : y < x
                1 < 3 ? OUI, donc on reste dans la deuxième boucle.
                y = y + 1 = 1 + 1 = 2
                x = x - 1 = 3 - 1 = 2
                Comparaison du deuxième while : y < x
                2 < 2 ? NON, donc on ne reste pas dans la deuxième boucle.
            Comparaison du premier while : x > 0
            2 > 0 ? OUI, donc on reste dans la première boucle.
            y = 0
            Comparaison du deuxième while : y < x
            0 < 2 ? OUI, donc on rentre dans la deuxième boucle.
                y = y + 1 = 0 + 1 = 1
                x = x - 1 = 2 - 1 = 1
                Comparaison du deuxième while : y < x
                1 < 1 ? NON, donc on ne reste pas dans la deuxième boucle.
            Comparaison du premier while : x > 0
            1 > 0 ? OUI, donc on reste dans la première boucle.
            y = 0
            Comparaison du deuxième while : y < x
            0 < 1 ? OUI, donc on rentre dans la deuxième boucle.
                y = y + 1 = 0 + 1 = 1
                x = x - 1 = 1 - 1 = 0
                Comparaison du deuxième while : y < x
                1 < 0 ? NON, donc on ne reste pas dans la deuxième boucle.
            Comparaison du premier while : x > 0
            0 > 0 ? NON, donc on ne reste pas dans la première boucle.
        Fin du programme.
        ```

!!! tip "Exercice 3"
    Écrire une fonction `plus_grand` qui prend en paramètres **trois nombres entiers** et renvoie **le plus grand** des trois nombres.

    ```python
    def plus_grand(a, b, c):
        ''' Renvoie le plus grand des trois entiers.
        :param a: (int) Un entier.
        :param b: (int) Un autre entier.
        :param c: (int) Encore un autre entier.
        :return (int): La plus grande valeur entre a, b et c. '''

        if a > b and a > c:
            return a
        elif b > a and b > c:
            return b
        else:
            return c
    ```

!!! tip "Exercice 4"
    Écrire une fonction `temps` qui prend en paramètres **un nombre entier de secondes** et **affiche le nombre d'heures, de minutes et de secondes** qui correspond.

    ```python
    def temps(nbs):
    ''' Renvoie le temps en heures, minutes et secondes.
    :param nbs: (int) Le temps en secondes.
    :return (None): On ne renvoie rien, on affiche avec print. '''
    
    heures = nbs // 3600  # 3600 secondes dans 1 heure
    nbs = nbs % 3600  # On récupère le nombre de secondes restantes et on le restocke dans nbs
    minutes = nbs // 60  # 60 secondes dans 1 minutes
    secondes = nbs % 60  # On récupère le nombre de secodes restantes
    print(f'{heures}h {minutes}min {secondes}s')
    ```

!!! tip "Exercice 5"
    Écrire une fonction qui prend en arguments **deux mots** (type `str`) et renvoie `True` si les deux mots **commencent par la même lettre** et **se terminent par la même lettre** et `False` sinon.

    ```python
    def jeu(mot1, mot2):
    ''' Renvoie True si les deux mots commencent et finissent par la même lettre.
    Renvoie False sinon.
    :param mot1: (str) Un mot.
    :param mot2: (str) Un autre mot.
    :return (bool): Un booléen, c'est-à-dire soit True, soit False. '''
    
    return mot1[0] == mot2[0] and mot1[len(mot1) - 1] == mot2[len(mot2) - 1]
    ```
    
    L'**indice** de la **première lettre** est `0`. La fonction `len` permet de récupérer le **nombre de caractères** dans une **chaîne de caractères**. On trouve donc l'**indice** de la **dernière lettre** du mot en retirant 1 à sa longueur.

    Plutôt que d'écrire `mot1[len(mot1) - 1]` et `mot2[len(mot2) - 1]`, on peut également plus simplement écrire `mot1[-1]` et `mot2[-1]`. Attention toutefois, cela fonctionne en **Python**, mais pas dans tous les langages. Retenez donc aussi la première méthode.

!!! tip "Exercice 6"
    Écrire une fonction `jeu` qui prend en paramètre un **nombre entier** `n` **strictement positif**, simule **n fois** le tirage d’un nombre choisi au hasard parmi les nombres `1`, `2`, `3`, `4`, `5`, `6`, et **renvoie le pourcentage** de **6** obtenus. On utilisera la fonction `randint` du module `random`.

    ```python
    def jeu(n):
        ''' Renvoie le pourcentage du nombre de 6 obtenus sur n tirages aléatoires.
        :param n: (int) Un nombre entier de tirages.
        :return (float): Le pourcentage de 6 obtenus. '''
        
        compteur = 0  # Compteur pour le nombre de 6 obtenus
        for _ in range(n):
            tirage = randint(1, 6)  # Récupérer une valeur aléatoire entre 1 et 6
            if tirage == 6:
                compteur = compteur + 1  # On peut aussi écrire compteur += 1
        return compteur * 100 / n  # On calcule et on renvoie le pourcentage
    ```

    Le pourcentage se calcule avec un simple **produit en croix** : les `n` tirages correspondent à **100%** des tirages, et on cherche le pourcentage pour le nombre `compteur` de tirages (`compteur` contient le nombre de fois où l'on a tiré la valeur `6`).

## Correction partie ordinateur

!!! tip "Exercice 1"
    Écrire un **programme** qui **trace** la **figure** ci-dessous en utilisant **deux boucles imbriquées**. Vous utiliserez le **module Python** *Turtle*. Vous pouvez **importer toutes les fonctions** du module en plaçant cette ligne au début de votre programme : `from turtle import *`.

    ```python
    from turtle import *

    penup()
    goto(-240,0)
    pendown()
    for i in range(9):
        côté = 10 * (i + 1)
        for j in range(4):
            forward(côté)
            left(90)
        penup()
        forward(côté + 10)
        pendown()
    done()
    ```

!!! tip "Exercice 2"
    Écrire un **programme** qui **demande à l’utilisateur** de **saisir un entier naturel** `n` et qui **calcule** la **somme des carrés** des **entiers** de **1** à `n`.  
    Afin de vérifier votre programme, voici un exemple : 1² + 2² + 3² + ... + 10² = 385

    ```python
    n = int(input("Veuillez saisir un entier naturel : "))
    somme = 0
    for i in range(1,n+1):
        somme = somme + i * i   # ou somme += i*i
    print(somme)
    ```

!!! tip "Exercice 3"
    Au jeu de ***Mölkky***, chaque joueur marque à son tour de jeu entre **0** et **12 points**, qui viennent s’ajouter à son **score** précédent. Mais gare ! Quiconque **dépasse** le score cible de **51 points** revient immédiatement à **25 points**.  
    Écrire un **programme** qui **demande un score** et un **nombre de points marqués**, et qui **affiche** le **nouveau score** ou **signale** une éventuelle **victoire**.  
    *Sources : Numérique et Sciences Informatiques 1ère, Balabonski et al., Ed. Ellipses.*

    ```python
    score = int(input("Quel est votre score ? "))
    nbPoints = int(input("Combien de points avez-vous marqué (entre 0 et 12) ? "))
    score = score + nbPoints
    if score > 51:
        score = 25
    print("Votre nouveau score est",score)
    if score == 51:
        print("Bravo, vous avez gagné!")
    ```

!!! tip "Exercice 4"
    Écrire un **programme** qui **demande à l’utilisateur** de **saisir** un **entier naturel** `n` et qui **affiche** tous ses **diviseurs** les uns après les autres. Les **diviseurs** devront être tous **écrits sur une même ligne et séparés par un tiret**.  
    *Exemple avec les diviseurs de 15 : 1-3-5-15.*

    ```python
    n = int(input("Veuillez saisir un entier naturel : "))
    for i in range(1,n):
        if n % i == 0:
            print(i,end="-")
    print(n)
    ```