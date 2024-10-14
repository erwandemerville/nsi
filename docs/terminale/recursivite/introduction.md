# Introduction à la récursivité

Pour présenter la notion de **récursivité**, prenons un exemple.  
On souhaite écrire une **fonction** `somme(n)` qui prend en **entrée** un *nombre entier positif* `n` et qui **renvoie** la **somme des entiers** de `1` à `n`.

Mathématiquement, on peut écrire cette somme ainsi :

$$
\sum{n} = 1 + 2 + \cdots + (n - 1) + n
$$

Par exemple :

$$
\sum{5} = 1 + 2 + 3 + 4 + 5 = 15
$$

$$
\sum{10} = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
$$

## Une première approche

Avec nos connaissances actuelle, une manière d'écrire cette **fonction** serait de le faire à l'aide d'une **boucle** `for`.

```python
def somme(n):
    ''' Renvoie la somme des entiers positifs de 1 à n.
    :param n: (int) un entier positif >= 1
    :return: (int) la somme des entiers de 1 à n '''

    somme = 0
    for i in range(1, n+1):
        somme += i
    return somme
```

On a ici utilisé la **programmation** dite **impérative** (ou *itérative*).  
Il s'agit d'un **paradigme de programmation** qui repose sur une **série d'instructions exécutées** de façon **séquentielle** par l'ordinateur. Ces instructions viennent modifier étape par étape les **valeurs** des **variables** pour finalement aboutir au **résultat** souhaité.

## Approche récursive

Dans cette nouvelle approche, raisonnons d'abord de manière **mathématique**.

Comment peut-on ré-exprimer la fonction **somme** en fonction de **cette même fonction** ?

!!! abstract "Une définition récursive"
    Mathématiquement, on peut exprimer la **somme** de la manière suivante :

    $$
    \sum{n} =
        \begin{array}{ll}
            1 & \mbox{si } n = 1\\
            n+\sum{(n-1)} & \mbox{si } n > 1
        \end{array}
    $$

    Il s'agit d'une définition **récursive**.  
    Pour calculer la **somme** de `n`, on a besoin de calculer la **somme** de `n - 1`.  
    De même, pour calculer la **somme** de `n - 1`, il faut calculer la **somme** de `n - 2`.
    Et ainsi de suite...

Ainsi, si l'on retranscrit cette définition en *Python*, on obtient :

```python
def somme(n):
    ''' Renvoie la somme des entiers positifs de 1 à n.
    Définition récursive.
    :param n: (int) un entier positif >= 1
    :return: (int) la somme des entiers de 1 à n '''

    if n == 1:  # cas de base (non récursif)
        return 1
    else:  # cas général (récursif)
        return n + somme(n - 1)
```

On constate que l'on a utilisé deux `return` dans notre nouvelle fonction.
On distingue **deux cas** :

- le **cas de base** lorsque `n == 1`, dans ce cas il n'y a pas de récursivité,
- le **cas général** lorsque `n > 1`, dans ce cas on effectue un **appel récursif**.

## Aller plus loin

Dans notre **fonction récursive** précédente, on ne distingue qu'**un seul cas de base** et **un seul cas récursif**. Mais on peut très bien avoir **plusieurs cas de base** et/ou **plusieurs cas récursifs**.

Voici un petit exercice :

!!! note "Exercice *(à faire sur feuille)*"
    On souhaite définir une **fonction** `pairs(n)` qui renvoie la **somme** de **tous** les **nombres pairs** compris entre `2` et `n`. On peut définir cette **fonction** mathématiquement de la manière suivante :

    $$
    pairs{(n)} =
        \begin{array}{ll}
            2 & \mbox{si } n = 2\\
            n+pairs{(n-1)} & \mbox{si } n~pair\\
            pairs{(n-1)} & \mbox{si } n~impair
        \end{array}
    $$

    Essayez d'écrire une fonction `pairs` **récursive** en suivant cette définition.  
    Voici l'en-tête de cette fonction :

    ```python
    def pairs(n):
        ''' Fonction récursive qui renvoie la somme des entiers pairs de 2 à n.
        :param n: (int) un entier positif >= 2
        :return: (int) un entier positif '''

        ...
    ```

    Voici un exemple d'utilisation :

    ```python
    >>> pairs(10)
    30
    >>> pairs(15)
    56
    ```