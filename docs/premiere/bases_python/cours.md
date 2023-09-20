??? quote "Source"
    - Inspiré du *Balabonski Première*.

!!! warning "En construction"   
    Ce cours est encore en construction, de nouvelles informations y seront prochainement ajoutées.

# Introduction à la programmation avec Python

## Vous avez dit "programme" ?

Un **programme** est la description d’un **algorithme** dans un **langage** compréhensible par un **humain** et par une **machine**, qui l’exécute afin de traiter des **données**. 

Il existe de nombreux **langages de programmation**, dont certains sont plus proches du **langage naturel** (on parle de langages de *haut niveau*), tandis que d’autres sont plus proches de celui de la **machine** (on parle de langages de *bas niveau*), on rappelle que la machine ne comprend que le **binaire**, c'est-à-dire une suite de **bits** `0` ou `1` (nous reviendrons sur cela dans le cadre d'un autre chapitre).

On peut citer, parmi les langages :

* de **haut niveau** : **Python**, *JavaScript*, *Java*, *C#*,
* de **bas niveau** : *C*, *Assembleur*, *langage machine* (le plus bas niveau possible).

Le langage de programmation **Python**, que l'on utilisera dans le cadre de cet enseignement, est déjà utilisé au lycée en **mathématiques**, et est également présent dans d’autres disciplines et dans le nouvel enseignement de **sciences numériques et Technologie** (SNT) en seconde.  
Au-delà du cadre de l'enseignement, c'est un langage **extrêmement populaire**, car l’un des plus **versatiles** et **généralistes**. Il est utilisé aussi bien par des développeurs débutants que par des développeurs d’applications web et mobile, des ingénieurs logiciels, des Data Scientists...

<figure markdown>
  ![Guido Van Rossum](images/guido_van_rossum.jpg){ width="500px" }
  <figcaption>Guido Van Rossum, créateur de Python<br />Source : <a href="https://fr.wikipedia.org/wiki/Guido_van_Rossum#/media/Fichier:Guido-portrait-2014-drc.jpg" target="_blank">Wikipédia</a></figcaption>
</figure>

Le langage Python a été créé par un **ingénieur informaticien néerlandais** du nom de **Guido Van Rossum**.

La première version publique date de *1991*. Van Rossum a ensuite poursuivi son travail sur le projet et a travaillé entre autres pour Google puis Dropbox. La version de Python que nous utiliserons est la **version 3**, disponible depuis *2008* avec des mises à jour régulières. La dernière version en date lors de l'écriture de cet article est la version **3.11.5**.

Le langage Python est **multiplateforme**, vous pouvez donc l'installer sur les systèmes d’exploitation **Linux**, **MacOs**, **Windows**, et même sur des smartphones dotés du système **Android** ou d'**iOS**. Il est **gratuit** et placé sous **licence libre**, la *Python Software Foundation License* (PSFL) .

Les **constructions élémentaires** propes au langage Python sont communes à de nombreux autres langages de programmation.

Un programme est ainsi composé :

* de **séquences**, (des instructions exécutées l’une après l’autre dans l’ordre où elles sont écrites),
* de définitions de **variables** et de **fonctions**,
* d’**affectations**,
* d’**instructions conditionnelles**,
* de **boucles** (bornées et non-bornées),
* d'**expressions** et d'**appels de fonctions**.

## Un IDE pour débuter

Il existe de nombreux **environnements de développement** (*EDI*, ou *IDE* en anglais) permettant de développer en Python. Celui que je vous conseille pour débuter est **<u>Thonny</u>**, [cliquez-ici pour découvrir l'IDE Thonny](thonny.md){ target="_blank" }.

## Expressions arithmétiques, variables et instructions

Le langage de programmation <u>**Python**</u> permet d'interagir avec la **machine** à l'aide d'un **programme** appelé **interpréteur Python**. On peut l'utiliser de deux manières différentes :

- en **<u>mode interactif</u>**, qui consiste à **dialoguer directement** avec l'**interpréteur**,
- en **<u>mode programme</u>**, qui consiste à **écrire un programme dans un fichier** et à le faire **exécuter par l'interpréteur**.

### Mode interactif

Le mode interactif s'apparente à une **calculatrice**.  
Les **trois chevrons** `>>>` indiquent que l'interpréteur **attend vos instructions**.

Par exemple, si vous saisissez `1 + 2` après les **chevrons** et que vous appuyez sur la touche **Entrée**, l'**interpréteur** effectuera le calcul et affichera le résultat :

```python
>>> 1 + 2
3
```

!!! note "À vous de jouer !"
    Saisissez dans l'interpréteur **Python** ci-dessous plusieurs expressions en utilisant les opérateurs `+` (*addition*), `-` (*soustraction*), `*` (*multiplication*) et `/` (*division*).

    {{ terminal() }}

#### Arithmétique

En Python, on peut saisir des **combinaisons** d'**opérations arithmétiques**.

Par exemple :

```python
>>> 2 + 5 * (10 - 1 / 2)
49.5
```

À noter que les espaces sont **purement décoratifs**, on aurait pu écrire :

```python
>>> 2+6*(10-1/2)
49.5
```

!!! warning "Erreur de syntaxe"
    L'interpréteur n'accepte que les **expressions arithmétiques bien formées**. Autrement, une `SyntaxError` indiquant une **erreur de syntaxe** sera levée, par exemple :

    ```python
    >>> 1 + * 2
        File "<stdin>", line 1
        1 + * 2
            ^
    SyntaxError: invalid syntax
    ```

    `<stdin>` signifie *standard input* (entrée standard), on reviendra sur les notions d'entrée standard et de sortie standard plus loin dans ce cours lorsque l'on présentera les fonctions `input` et `print`.

!!! warning "Erreur division par zéro"
    Un autre type d'erreur qui peut être levée par l'interpréteur Python est une `zeroDivisionError`, indiquant que l'expression contient **une division par zéro**. Par exemple :

    ```python
    >>> 2 / (3 - 3)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero
    ```

Les **nombres de Python** peuvent être **des nombres entiers relatifs**, de type `int`, et des **nombres décimaux**, que l'on appelle **flottants**, de type `float`.

Les nombres **entiers** peuvent être **de taille arbitraire**, et ne sont limités que par la **mémoire disponible** de la machine pour les stocker.  
Les **nombres flottants** quant à eux ont **une capacité limitée**, et les nombres décimaux très grands et très petits ne sont **pas représentables**. (On reviendra plus tard sur la **représentation des nombres réels en machine**).

**<u>Important</u>** : En **Python**, la virgule séparant la partie **entière** de la partie **décimale** doit être représentée par **un point**, auquel cas vous pourrez observer des comportements étranges de l'interpréteur.

!!! abstract "Différentes façons de diviser"

    Lorsque l'on utilise l'opérateur de division classique de Python `/`, on obtient un **nombre flottant** (type `float`) :

    ```python
    >>> 7 / 2
    3.5
    >>> type(7 / 2)
    <class 'float'>
    ```

    !!! tip "Les types de base"
        Vous pouvez voir ci-dessus apparaître le mot-clé `class`. Les **classes** sont une notion qui n'est abordée qu'en **terminale**, mais en gros, il faut comprendre que tout ce qui est manipulé en Python est **objet**. Il y a des objets de type `int` (les **nombres entiers**), des objets de type `float` (les **nombres flottants**), des objets de type `str` (les **chaînes de caractères**, etc.)

        Ici, on a utilisé une **fonction** appelée `type` afin de voir de **quel type** est l'objet qui résulte de l'opération `7 / 2`. (On a ici la confirmation que l'on obtient bien un **flottant**.)

    Il existe **deux autres opérateurs** bien utiles :

    - `//` permettant d'obtenir le **quotient** de la **division euclidienne** de deux opérandes,
    - `%` permettant d'obtenir le **reste** de la **division euclidienne** de deux opérandes.

    Par exemple :

    ```python
    >>> 7 // 2
    3
    >>> 7 % 2
    1
    >>> type(7 // 2)
    <class 'int'>
    >>> type(7 % 2)
    <class 'int'>
    ```

    Ces deux opérateurs renvoient donc **des entiers**. On rappelle que pour deux nombres entiers $a$ et $b$, $a = q \times b + r$, avec $q~=~a~//~b$ le **quotient** et $r~=~a~\%~b$ le **reste**.

#### Variables

Saisir des expressions arithmétiques, c'est bien. Mais une calculatrice sait déjà le faire !

Nous allons maintenant introduire la notion de **variable**. Une **variable** permet de **stocker une donnée** utilisée par un **programme**.

Cela se fait par une **affectation** qui associe une **donnée**, représentée par une **valeur** ou une **expression**, avec un **nom**.  
Une **expression** stockée dans une variable peut elle-même contenir d'**autres variables**.

Une **variable** peut s'apparenter à une "boîte" sur laquelle est écrit un **nom** et dans laquelle on place des **informations** diverses (même si dans la réalité, ce n'est pas tout à fait ça). Un **nom** peut être n’importe quelle **chaîne alphanumérique**, à l'exception de certains mots réserés, et ne doit pas commencer par un chiffre.

L’opérateur d’affectation est noté `=`.  
Par exemple, l’instruction `x = 4` associe la valeur 4 au **nom** `x` :

```python
>>> x = 4
>>>
```

Si l'on saisit une **instruction** d'**affectation** dans l'**interpréteur Python**, aucun résultat n'est affiché. Si l'on souhaite accéder à la valeur **mémorisée** dans `a`, il suffit de saisir :

```python
>>> a
4
```

L’instruction `y = 3 + 5` associe la valeur de l’expression située à droite du signe `=`, ici **8**, au nom `y`.  
L’instruction `z = x + y` associe la valeur de l’expression située à droite du signe `=`, ici **12** (la somme des valeurs contenues dans les variables `x` et `y`), au nom `z`.

**Python** permet par ailleurs d'effectuer des **affectations multiples**, par exemple `x, y, z = 1, 3, 5`, qui associe les valeurs **1**, **3** et **5** respectivement aux noms `x`, `y` et `z`. Ceci est équivalent à écrire `x=1; y=3; z=5` sur une ligne ou à effectuer les 3 affectations sur 3 lignes successives.

!!! info "À retenir"
    * Une **variable** est composée d’un **nom** (ou identificateur), d’une **adresse en mémoire** où est enregistrée une **valeur** (ou un **ensemble de valeurs**), et d’un **type** qui **définit ses propriétés**.
    * Une **expression** a une **valeur** qui est le **résultat** d’une **combinaison de variables ou d’objets**, de **constantes** et d’**opérateurs**.
    * Une **instruction** est une commande qui doit être **exécutée** par la machine.
    * Une **affectation** est une **instruction** qui commande à la machine de créer une **variable** en lui précisant son **nom** et la **valeur** qui lui est associée.

    Il est important de bien distinguer une <u>**expression**</u>, qui se **calcule** et a une **valeur**, d'une <u>**instruction**</u>, qui est **exécutée** par la machine.

!!! note "À vous de jouer !"
    Voici une suite d'instructions :

    {{ IDEv('scripts/01') }}

    Quelle sera la valeur contenue dans la variable `c` après avoir saisi ces instructions ?   
    Vérifiez en **exécutant** le programme.

    **Même question avec la suite d'instructions suivante :**

    {{ IDEv('scripts/02') }}

!!! note "À vous de jouer 2 !"
    Voici une suite d'instructions :

    ```python
    x = 3
    y = 6
    z = 4 + x * y
    x = z / 2
    ```

    Quelle sera la valeur contenue dans la variable `x` après avoir saisi ces instructions ?  
    Vérifier en utilisant la console de Thonny.  
    Que constatez-vous de particulier sur la valeur contenue dans `x` ?

??? tip "Réponse - À vous de jouer 2 !"
    Normalement, la console devrait afficher la valeur `11.0`. On constate que l'on obtient ici un nombre **décimal**, et non pas un nombre **entier**. En fait, il existe plusieurs **types de données** que peuvent contenir les variables : les **entiers**, les **flottants** (nombres décimaux), mais également d'autres types de données que l'on verra plus tard, comme les **chaînes de caractères**, les **booléens**...

    Si l'on avait utilisé l'opérateur `//`, c'est-à-dire si l'on avait saisi `z // 2`, on aurait obtenu le **quotient de la division euclidienne** entre les opérandes `z` et `2`, c'est-à-dire l'entier `11`. L'opérateur permettant d'obtenir le **reste d'une division euclidienne** est `%`.

### Mode programme

## Les boucles bornées `for`

## Comparaisons, booléens, tests

## Les fonctions