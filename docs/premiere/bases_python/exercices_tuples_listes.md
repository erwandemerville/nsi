# Exercices - Tuples et listes

!!! tip "Cours sur les tuples et les listes"
    Pensez à consulter le [cours sur les tuples et les listes](tuples_listes.md){ target="_blank" } si vous avez besoin d'aide pour réaliser les exercices suivants.

    Pensez également à consulter le [TD/Cours sur les tuples et listes](pdf/les_tuples_et_les_listes_partie_tuples_corrige.pdf){ target="_blank" } si vous avez besoin d'aide pour réaliser les exercices suivants.

!!! note "TP : exercices sur les tuples et les listes"
    <center style="font-size: 1.3em">
    [Télécharger le document](pdf/tp_exercices_tuples_et_listes.pdf)
    </center>

    Les programmes demandés dans ce document (qui vous a été remis en classe) peuvent être saisis dans un *programme Python* sur **Thonny** de manière à pouvoir les tester et vérifier leur bon fonctionnement.

    Il s'agit simplement d'écrire le *code Python* associé à chaque bloc d'algorithme écrit en *pseudo-code*.

## Autres exercices sur les tuples

!!! note "Exercice 1"
    Écrire une fonction `afficher(tuple)` qui affiche chaque **élément** d'un **tuple donné** en *entrée*.

    Programme à compléter :
    ```python
    def afficher(tuple):
        ''' Affiche chaque élément du tuple donné. '''

        ...
    
    # Programme de test
    tpl = (42, "e", 6.5, True)  # un tuple d'exemple
    afficher(tpl)               # appel de la fonction afficher sur le tuple tpl
    ```

{% if exercices.premiere.bases_python.tuples.exo1 %}
??? tip "Correction exercice 1"
    Voici deux manières différentes d'écrire cette fonction, d'abord en effectuant un **parcours par élément**, puis en effectuant un **parcours par indice**.

    À noter qu'ici **on ne renvoie rien** (équivalent à renvoyer `None`).

    ```python
    def afficher(tuple):
        ''' Affiche chaque élément du tuple donné,
        AVEC UN PARCOURS PAR ÉLÉMENT. '''

        for el in tuple:  # pour chaque élément (stocké dans el) du tuple
            print(el)     # afficher l'élément el

    def afficher(tuple):
        ''' Affiche chaque élément du tuple donné,
        AVEC UN PARCOURS PAR INDICE. '''

        longueur = len(tuple)      # récupérer et stocker la longueur (nombre d'éléments) du tuple
        for i in range(longueur):  # pour i allant de 0 à len(tuple) - 1
            print(tuple[i])        # afficher l'élément de tuple d'indice i
    ```
{% endif %}

!!! note "Exercice 2"
    Écrire une fonction `somme_elements(tuple)` qui **renvoie** la **somme** de **chaque entier** du **tuple d'entiers** donné en *entrée*.

    Programme à compléter :

    ```python
    def somme_elements(tuple):
        ''' Renvoie la somme de tous les entiers contenus dans le tuple donné. '''

        ...
    
    # Programme de test
    tpl = (2, 4, 1, 5, 2)  # un tuple d'exemple
    print(somme_elements(tpl))    # appel de la fonction afficher sur le tuple tpl
    ```

{% if exercices.premiere.bases_python.tuples.exo2 %}
??? tip "Correction exercice 2"
    Ici aussi, on peut écrire cette fonction en effectuant un **parcours par élément**, ou bien un **parcours par indice**. Voici les deux versions :

    ```python
    def somme_elements(tuple):
        ''' Renvoie la somme de tous les entiers contenus dans le tuple donné,
        AVEC UN PARCOURS PAR ÉLÉMENT. '''

        somme = 0         # initialiser une variable somme à 0
        for el in tuple:  # pour chaque élément (stocké dans el) du tuple
            somme += el   # ajouter l'élément el à la somme
        return somme      # renvoyer la somme finale

    def somme_elements(tuple):
        ''' Renvoie la somme de tous les entiers contenus dans le tuple donné,
        AVEC UN PARCOURS PAR INDICE. '''

        somme = 0                  # initialiser une variable somme à 0
        longueur = len(tuple)      # récupérer et stocker la longueur de tuple
        for i in range(longueur):  # pour i allant de 0 à len(tuple) - 1
            somme += tuple[i]      # ajouter l'élément du tuple d'indice i à la somme
        return somme               # renvoyer le somme finale

    ```
{% endif %}

## Autres exercices sur les listes

Voici quelques autres exercices sur **les listes**.

!!! note "Exercice 1"
    Écrire un **programme** qui :

    - crée une **liste** contenant les **entiers** de `1` à `1000` dans l'ordre dans la liste,
    - affiche la liste.

!!! note "Exercice 2"
    Écrire une **fonction** `afficher_sup(liste, element)`, qui prend une **liste** `liste` ainsi qu'un **entier** `element` en **entrée**, et qui **affiche** tous les éléments de la liste supérieurs à `element`.

!!! note "Exercice 3"
    Écrire une **fonction** `generer(a, b)` qui **renvoie** une **nouvelle liste** contenant tous les entiers de `a` jusqu'à `b`.

    *Exemple d'utilisation* :  
    ```python
    >>> generer(5, 11)
    [5, 6, 7, 8, 9, 10]
    ```

!!! note "Exercice 4"
    Écrire une **fonction** `pairs(liste)` qui **affiche** tous les **entiers pairs** d'une **liste d'entiers** `liste` donnée.

    *Exemple d'utilisation* :  
    ```python
    >>> lst = [2, 3, 5, 12, 13, 18, 16, 8]
    >>> pairs(lst)
    2
    12
    18
    16
    8
    ```

!!! note "Exercice 5"
    Écrire une **fonction** `supprimer(liste, element)` qui prend une **liste d'entiers** `liste` et un **entier** `element`, et qui **renvoie** une **nouvelle liste** contenant les éléments de la liste donnée, dans le même ordre, mais sans les occurences de `element`.

    *Exemple d'utilisation* :  
    ```python
    >>> lst = [2, 4, 3, 5, 4, 8, 6, 4, 10]
    >>> supprimer(liste, 4)
    [1, 3, 5, 8, 6, 10]
    ```

!!! note "Exercice 6"
    Écrire une **fonction** `compter(liste, element)` qui prend une **liste d'entiers** `liste` et un **entier** `element`, et qui **renvoie** le **nombre d'occurences** de `element` dans `liste`.

    *Exemple d'utilisation* :  
    ```python
    >>> lst = [1, 2, 4, 2, 3, 5, 3, 2, 6, 1]
    >>> compter(lst, 2)
    3
    ```

!!! note "Exercice 7"
    Écrire une **fonction** `renverser(liste)` qui prend une **liste d'entiers** `liste` et **renvoie** une **nouvelle liste** avec les éléments ordonnés **inversement**.

    *Exemple d'utilisation* :  
    ```python
    >>> lst = [1, 2, 4, 2, 3, 5, 3, 2, 6, 1]
    >>> compter(lst, 2)
    3
    ```

!!! note "Exercice 8"
    Écrire une **fonction** `min_max(liste)` qui prend en entrée une **liste d'entiers** `liste` et qui **renvoie** un **tuple** contenant le **minimum** et le **maximum** de la liste.

    *Exemple d'utilisation* :  
    ```python
    >>> lst = [2, 1, 6, 3, 9, 8]
    >>> min_max(liste)
    (1, 9)
    ```

!!! note "Exercice 9"
    Écrire une **fonction** `moyenne(liste)` qui prend en entrée une **liste d'entiers** `liste` et qui **renvoie** la **moyenne** des éléments de la liste.

!!! note "Exercice 10"
    Écrire une **fonction** `moyenne_ponderee(notes, coeffs)` qui prend en entrée une **liste de flottants** `notes` contenant des notes entre `0` et `20` ainsi qu'une **liste d'entiers** `coeff` contenant les **coefficients** associés à chaque note, et qui **renvoie** la **moyenne pondérée** des **notes** données.