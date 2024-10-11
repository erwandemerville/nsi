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

!!! note "Exercice 2"
    Dans un nouveau **script Python**, écrire une fonction `compter_voyelles` qui reçoit une **chaîne de caractères** `mot` en entrée et **renvoie** le **nombre de voyelles** ("a", "e", "i", "o", "u", "y") présentes dans ce mot.

    Exemple :

    ```python
    print(compter_voyelles("python"))  # 2
    print(compter_voyelles("ananas"))  # 3
    ```

    Ensuite, **en-dessous de la fonction**, écrire un **programme** qui demande à l'utilisateur de saisir un **mot**, puis afficher le **nombre de voyelles** de ce mot en faisant appel à `compter_voyelles`.