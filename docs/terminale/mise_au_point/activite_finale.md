# Activité finale

!!! info "Modalités de rendu"
    Vous réaliserez ce travail dans un fichier nommé `<VOTRE_NOM>_activite_sousmax.py`, que vous téléverserez depuis la [page de rendu des travaux](../../rendus.md){ target="_blank" }.

On veut définir une **fonction** qui **renvoie** le **deuxième plus grand élément** d’un **tableau** de **nombres entiers**. Par exemple dans le tableau `[4, 2, 7, 5, 9, 1, 5, 3]`, la valeur cherchée est `7`. On veut s’assurer que la fonction est codée correctement en **créant un jeu de tests**.

Concernant les tests, vous êtes libre d'utiliser **des assertions** ou **un module de votre choix** parmi *doctest*, *pytest* et *unittest*.

!!! note "Exercice 1"
    Écrire l'en-tête de la fonction finale, que l'on nommera `sousmax`, incluant une **spécification** sous la forme d'une **docstring**. Cette **spécification** doit contenir :

    - une explication de **ce que fait la fonction**,
    - les **paramètres d'entrée** et leurs **types**,
    - les **conditions d'utilisation** (**préconditions**),
    - le **type** de la **valeur de retour**.

    Vous devez également décrire le comportement de la fonction **lorsqu'il existe plusieurs éléments maximums** dans le tableau.

!!! note "Exercice 2 - Tests « boîte noire »"
    Écrire un ensemble de tests unitaires de cette fonction. Ces tests ne prennent pas en compte l'implémentation de la fonction, et doivent uniquement être liés à la **spécification**.

    Vous pouvez inclure :

    - des tests avec des tableaux de **moins de deux éléments**,
    - des tests avec **des éléments tous différents**,
    - des tests avec **plusieurs éléments de même valeur maximale**,
    - des tests avec **plusieurs éléments sous-maximums**,
    - un test avec **des éléments tous égaux**.

    Vous pouvez utiliser la fonction `shuffle` du module `random` pour effectuer des tests plus exhaustifs (des points bonus seront accordés le cas échéant).

!!! note "Exercice 3 - Implémentation"
    On propose **deux approches** pour coder la **fonction demandée** :

    a. écrire d’abord une **fonction** qui **calcule la valeur maximale** d’un tableau, puis une fonction qui **calcule la plus grande valeur** d’un **tableau inférieure à une valeur donnée**, et enfin **utiliser ces deux fonctions** pour écrire une **troisième fonction** qui **calcule la valeur demandée** ;
    
    b. écrire une **fonction** qui **calcule directement la valeur demandée**.

    **Implémentez la fonction `sousmax` en utilisant une des approches ci-dessus.**

!!! note "Exercice 4"
    Enfin, lancez les tests que vous avez écrits à l'exercice 2 et corrigez les erreurs éventuelles de votre code.