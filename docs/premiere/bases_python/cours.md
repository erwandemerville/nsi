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

Le **mode programme** de **Python** consiste à écrire une **suite d’instructions** dans un **fichier** et à les faire **exécuter** par l’**interpréteur Python**. Cette suite d’instructions s’appelle un **programme** (ou **code source**). Cela permet d'éviter d'avoir à ressaisir à chaque fois les instructions dans le mode interactif. Cela permet de faire la distinction entre le rôle de **programmeur** et celui d’**utilisateur** d’un programme.

### Affichage sur la sortie standard

Contrairement au **mode interactif**, en **mode programme**, les résultats des expressions calculées ne sont plus affichés à l’écran. Il faut utiliser pour ceci une instruction explicite d’affi- chage. En Python, elle s’appelle `print`. Par exemple :

{{ IDEv('scripts/03.py') }}

On peut également fournir à `print` une **expression**, qui sera **calculée** puis **affichée** :

{{ IDEv('scripts/04.py') }}

`print` est également capable d'**afficher du texte**, qui doit être mis entre guillemets `"` ou apostrophes `'`, par exemple :

{{ IDEv('scripts/05.py') }}

On peut également afficher **la valeur d'une variable**, exemple :

{{ IDEv('scripts/07.py') }}

Si l'on souhaite inclure **la valeur d'une variable** dans un **texte affiché** par `print`, on peut procéder de différentes façons :

- **avec la concaténation** : on peut inclure notre **variable** dans une **chaîne de caractères** en utilisant la **concaténation de chaînes de caractères**. Pour cela, on transforme notre variable de type `int` en type `str` (c'est-à-dire en chaîne de caractères) avec la fonction `str()`, et on effectue la concaténation en utilisant un `+`.
- avec des **f-strings** (pas au programme) : si on ajoute un `f` devant notre chaîne de caractères, on peut inclure nos variables **entre accolades**, et elles seront remplacées par leur valeur. Il n'y a, dans ce cas, pas besoin de convertir le type de nos variables en `str`.
- en donnant **plusieurs valeurs** (plusieurs *arguments*) à notre fonction `print` : dans ce cas, `print` affichera chaque valeur les unes à la suite des autres, que cela soit des chaînes de caractères ou non.

{{ IDE('scripts/06.py') }}

La fonction `print` effectue par défaut un **retour à la ligne** après avoir affiché les valeurs que vous lui avez donné. Pour changer ce comportement, on peut ajouter le paramètre `end` :

{{ IDE('scripts/09.py') }}

## Interaction avec l'utilisateur, lire sur l'entrée standard

Pour demander à l'utilisateur de **saisir une valeur**, de manière à pouvoir la **stocker dans une variable** et en faire quelque chose, on utilise la fonction `input`.

{{ IDEv('scripts/08.py') }}

!!! warning "Attention au type"
    La valeur renvoyée par la fonction `input` est de type `str` (chaîne de caractères). Si vous voulez utiliser cette valeur dans une **opération arithmétique** par exemple, il faut donc la convertir en `int` (nombre entier), d'où l'utilisation de la fonction `int` ci-dessus.

L'instruction `input` ne s'arrête que **lorsque l'utilisateur a appuyé sur la touche `Entrée`**.

## Les boucles bornées `for`

Répéter plusieurs fois les mêmes instructions est assez rébarbatif. C'est pour cela qu'il existe une instruction appelée **boucle bornée**, utilisant le mot-clé `for`, qui permet de répéter plusieurs fois un bloc d'instructions. Par exemple :

{{ IDEv('scripts/10.py') }}

Dans la fonction `range`, on indique **le nombre de fois** que l'on souhaite **afficher l'instruction** `print`. Ici, on l'affiche **10 fois**.

En réalité, ce qu'il se passe, c'est que la boucle va **itérer** de la valeur `i = 0` à la valeur `i = 9` (la valeur indiquée dans le `range` moins 1), la variable `i` fournie à notre boucle étant ce l'on appelle l'**indice de boucle**. On dit que `i` **incrémente** (augmente de **1**) à chaque **itération** de la boucle.

En **pseudo-langage**, on pourrait traduire ce programme de la manière suivante :  
```
POUR i ALLANT DE 0 à 9 :
    AFFICHER "Je ne dois pas bavarder en cours"
```

Si l'on affiche ce que contient notre **variable** `i` à chaque fois :

{{ IDEv('scripts/11.py') }}

On peut utiliser le `range` de plusieurs manière différentes :

- `range(valeur)` : avec **une seule valeur** entière, la boucle va itérer de `0` à `valeur - 1`,
- `range(min, max)` : avec **deux valeurs** entières, la boucle va itérer de `min` à `max - 1`,
- `range(min, max, pas)` : avec **trois valeurs** entières, la boucle va itérer de `min` à `max - 1` avec un **pas** de `pas`. Si l'on n'indique pas ce **pas**, il est de **1** par défaut.

Par exemple, si l'on souhaite afficher tous les nombres **pairs** de **2** à **98** :

{{ IDEv('scripts/12.py') }}

Ici, on a appelé l'**indice de boucle** `nb`. On peut l'appeller comme on veut, mais on utilise souvent des noms à une lettre comme `i`, `j` et `k`.

On peut également passer la valeur de retour d'un `input` à l'intérieur d'un `range`, par exemple :

{{ IDEv('scripts/13.py') }}

!!! warning "Attention au type"
    Le `range` ne prend que des **entiers**. Si vous souhaitez lui passer la valeur de retour d'un `input`, il faut donc convertir cette valeur en valeur entière avec la fonction `int`.

## Comparaisons, booléens, tests

Une part importante de la conception d’un programme consiste à imaginer les différents **cas de figure possibles**, notamment selon les **entrées fournies** par l’utilisateur ou les **valeurs** des différentes **variables**, de manière à adapter le programme à chacun des cas. Pour traduire cela dans l’écriture du programme, on peut utiliser des instructions de **branchement** (`if`, `elif`, `else`) qui rassemblent **plusieurs blocs de code alternatifs**, chacun associé à une **condition logique**, et qui à chaque exécution sélectionne au plus l’un de ces blocs.

### Les instructions de branchement

Les instructions `if` (*si*), `elif` (*sinon si*) et `else` (*sinon*) permettent d'exécuter des blocs de code uniquement lorsqu'une **condition** est remplie. Par exemple, voici un programme qui demande à l'utilisateur de saisir un nombre et affiche un message différent selon le nombre saisi :

{{ IDEv('scripts/17.py') }}

Le programme est executé **séquentiellement**, autrement dit, on vérifie d'abord la première condition, si elle est vraie, alors on affiche le message indiqué, sinon on passe à la deuxième condition, et ainsi de suite...

Le comportement de ce programme est donc le suivant :

- **si** `nb` est inférieur à `5` (donc compris entre `0` et `4` inclus), on affiche `"Vous êtes un bébé."`,
- **sinon si** `nb` est inférieur à `12` (donc compris entre `5` et `11` inclus), on affiche `"Vous êtes un enfant."`,
- **sinon si** `nb` est inférieur à `18` (donc compris entre `12` et `17` inclus), on affiche `"Vous êtes un ado."`,
- **sinon si** `nb` est inférieur à `40` (donc compris entre `18` et `39` inclus), on affiche `"Vous êtes un adulte."`,
- **sinon si** `nb` est inférieur à `60` (donc compris entre `40` et `59` inclus), on affiche `"Vous êtes un vieil adulte."`,
- **sinon**, (donc si l'âge est au moins de `60`), on affiche `"Vous êtes un vieillard."`.

**Une seule branche** est donc choisie en fonction de la valeur de `nb`, et **un seul message** sera donc affiché.

Voici les symboles permettant d'effectuer des **comparaisons** :

| >    | plus grand que | >=   | supérieur ou égal à | ==   | égal à       |
| ---- | -------------- | ---- | ------------------- | ---- | ------------ |
| <    | plus petit que | <=   | inférieur ou égal à | !=   | différent de |

!!! warning "Homogénéité des valeurs comparées"
    Lorsque vous effectuez une **comparaison** (utilisant l'un des symboles ci-dessus), il faut vous assurer que vous compariez bien ce qui est comparable. Vous pouvez comparer des entiers entre eux, des flottants entre eux, des chaînes de caractères entre eux, ou encore comparer un entier avec un flottant... Mais vous ne pouvez pas, par exemple, comparer un **entier** avec une **chaîne de caractères**, ou vous obtiendrez une erreur.

    ```python
    >>> 1 < "123"
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: '<' not supported between instances of 'int' and 'str'
    ```

## Les fonctions

Vous avez jusqu'ici utilisé plusieurs **fonctions natives de Python**, comme `print`, `input`, `int` (la fonction, pas le type), `range`...

Les **fonctions** permettent de créer des **fragments de code réutilisables**. Cela va nous permettre d'aller beaucoup plus loin dans la conception de nos programmes, en créant des fonctions pour effectuer certaines tâches autant de fois qu'on le souhaite, et pour différentes valeurs d'entrée.

Pour définir une fonction, on utilise le **mot-clé** `def`, suivi du **nom de la fonction**, suivi de `:`, puis vient ensuite (à la ligne, avec une **identation**) le bloc d'instructions à exécuter dans la fonction.

!!! note "Une fonction = une tâche"
    Il est fortement conseillé, pour la clarté du code, de faire en sorte qu'**une fonction représente une seule tâche**.

Par exemple, voici une fonction qui **prend deux nombres entiers** et **renvoie la somme de ces deux nombres** :

{{ IDEv('scripts/14.py') }}

Pour **tester cette fonction**, vous pouvez l'**appeler dans l'interpréteur**  (en saisissant l'instruction d'appel après les trois chevrons `>>>` et en appuyant sur la touche `Entrée`) après avoir exécuté le programme. Par exemple, **entrez l'instruction** `somme(3,5)` dans l'interpréteur ci-dessus après exécution du programme pour observer le résultat.

Vous pouvez également appeller cette fonction directement dans le programme, mais pour afficher la valeur renvoyée, il faudra ajouter un `print` :

{{ IDEv('scripts/16.py') }}

La **valeur renvoyée par la fonction** est indiquée avec le **mot-clé** `return`. Lorsque le `return` est rencontré, on sort de la fonction. Ainsi, si vous rajoutez des instructions **après** ce `return`, elles ne seront pas exécutées, exemple :

{{ IDEv('scripts/15.py') }}

### Fonctions sans paramètres

Une fonction peut **ne pas avoir de paramètres**. Par exemple, voici une fonction qui renvoie une valeur aléatoire entre 1 et 100, en appelant la fonction `randint` du module `random` :

{{ IDEv('scripts/18.py') }}

Ici, on appelle la fonction sans lui fournir de valeurs, mais la fonction appelée renvoie bien une valeur (le mot-clé `return` est bien présent).

### Fonctions sans valeur de retour : procédures

Il est également possible de créer une **fonction** qui ne contient **pas de valeur de retour** (pas de `return`). Par exemple :

{{ IDEv('scripts/19.py') }}

On crée ici une fonction qui contient un paramètre `message`, et qui **affiche** avec `print` ce message, mais ne **renvoie** rien. La fonction est ensuite appelée, avec le message `"HOURAAAAAAAAAAA !!!"` qui est donc affiché.

Les fonctions qui ne **renvoient rien** peuvent être appelées **procédures**. Toutefois, en **Python**, il n'y a techniquement pas de distinction entre les fonctions et les procédures, contrairement à d'autres langages comme le **Java** par exemple.

### Variables locales et globales

Lorsque vous définissez une **variable à l'intérieur** d'une **fonction**, cette variable n'existe **qu'à l'intérieur de la fonction**.

Par exemple, dans la fonction ci-dessous, on a créé une variable `resultat`. Cette variable n'existe qu'à l'intérieur de la fonction, vous pourriez donc avoir une autre variable `resultat` à l'extérieur de la fonction, qui contiendrait une autre valeur.

{{ IDEv('scripts/20.py') }}

## Les boucles non bornées `while`

Nous avons vu qu'il était possible de créer des **boucles bornées** à l'aide d'instructions utilisant le **mot-clé** `for`. Nous allons voir ici que l'on peut également créer des boucles **non bornées** à l'aide du **mot-clé** `while` (qui signifie *TANT QUE* en français).

Une **boucle non bornée** permet d'exécuter un **bloc d'instructions** plusieurs fois, et de continuer **TANT QUE** une **condition donnée** est **vérifiée**.

La **structure** d'une boucle `while` en Python est la suivante :

```python
while condition:
    # Bloc d'instructions à répéter tant que la condition est vraie
```

La boucle `while` commence par **évaluer la condition** :

- **Si** la **condition** est **vraie**, le **bloc d'instructions** à l'intérieur de la boucle est **exécuté**.
- Après chaque exécution du bloc, la **condition** est à nouveau **évaluée** :
    - **Tant que** la **condition** reste **vraie**, la boucle **continue de s'exécuter**.
    - Dès que la **condition** devient **fausse**, la boucle **s'arrête**.

Voici un premier <u>exemple</u> d'utilisation d'une boucle `while` (cliquez sur le premier bouton, *Lancer*, pour exécuter le programme):

{{ IDEv('scripts/21.py') }}

Dans cet exemple, la boucle `while` est utilisée pour **afficher les nombres de `1` à `5`**.  
La variable `i` est initialisée à `1`, et la boucle continue **TANT QUE** `i` est **inférieur ou égal** à `5`. À **chaque itération de la boucle**, la valeur de `i` est ici **affichée** (à l'aide du `print`), puis est **incrémentée de `1`** à l'aide de l'instruction `i += 1`. La boucle **s'arrête** lorsque `i` atteint `6`, car **la condition devient fausse**.

Voici un autre <u>exemple</u> un peu plus concret de l'utilisation d'une boucle `while` :

{{ IDE('scripts/22.py') }}

Dans cet exemple, une boucle `while` est utilisée pour **demander à l'utilisateur** (à l'aide de la fonction `input`) de **saisir un mot de passe** jusqu'à **trois essais**.  
La boucle **continue tant qu'il reste des essais** (tant que `essais_restants > 0`) :

- Si **l'utilisateur saisit le mot de passe correct** (c'est-à-dire lorsque `tentative == mot_de_passe`), la boucle **s'arrête** à l'aide de l'instruction `break`. L'instruction `break` permet de **sortir directement** de la boucle, et évite donc de ré-évaluer sa condition.
- Sinon, le **nombre d'essais restants** est **décrémenté** (cela signifie que l'on **soustrait 1** à `essais_restants`), et un message est **affiché** (à l'aide de la fonction `print`) pour informer l'utilisateur du **nombre d'essais restants**.

Une fois que l'on est **sorti de la boucle** (ce qui se produit soit si on a rencontré l'instruction `break`, soit si la **condition** de la boucle est **fausse**), on **affiche** un message d'accès refusé si le nombre maximal d'essais a été atteint.

!!! warning "Attention aux boucles infinies !"
    Dans une boucle non bornée `while`, contrairement à une boucle bornée `for`, il y a un risque de créer **boucle infinie**, c'est-à-dire une boucle dont la **condition n'est jamais évaluée à `False`**. Par exemple :

    ```python
    i = 1
    while i < 5:
        print(i)
    ```

    Ici, on n'a pas écrit d'instruction permettant d'**incrémenter** la variable `i`, donc la **condition** `i < 5` sera **toujours vraie**. Le programme ne s'arrêtera donc **jamais**.

!!! note "À vous de jouer !"
    Écrivez un **programme** en Python qui **demande à l'utilisateur** d'entrer un **nombre entier positif `n`**. Ensuite, utilisez une **boucle** `while` pour **calculer** la **somme de tous les entiers de `1` à `n`**. **Affichez** ensuite le **résultat**.

    Voici un exemple d'exécution du programme :

    ```yaml
    Entrez un nombre entier positif : 5
    La somme des entiers de 1 à 5 est : 15
    ```

    ??? tip "Cliquez ici pour afficher l'aide"
        Voici comment procéder pour réaliser ce programme :

        1. Utilisez la fonction `input` pour demander à l'utilisateur de **saisir** un **nombre entier positif**, vous stockerez la valeur saisie dans une **variable** que vous pourrez appeler `n`. N'oubliez de **convertir** cette valeur en **entier** à l'aide de la fonction `int`.
        2. Créez une **variable** pour **accumuler la somme totale**, que vous **initialiserez** à `0` avant d'entrer dans la boucle.
        3. Créez une **variable** que vous appelerez `i` par exemple, qui prendra chaque valeur de 1 à `n`.
        4. Utilisez une boucle `while` qui continue **tant que** `i` est **inférieur ou égal à** `n`, pour **ajouter les entiers** de `1` à `n` à la **somme totale**.
        5. N'oubliez pas d'**incrémenter la valeur de** `i` à **chaque itération de la boucle**.
        6. Enfin, après la boucle, **affichez le résultat** à l'aide de la fonction `print`.

    Vous pouvez réaliser ce programme sur ***Thonny*** ou dans l'**IDE ci-dessous** (vous pourrez *télécharger* votre programme en cliquant sur le *deuxième bouton* pour le conserver.)

    {{ IDE() }}

## Les listes

En programmation en langage **Python**, les **listes** sont l'une des **structures de données** les plus couramment utilisées. Une **liste** (**objet** de type `list`) est une **collection ordonnée d'éléments** pouvant être de différents **types** (*nombres entiers*, *flottants*, *chaînes de caractères*, *objets*, etc.). Les listes sont extrêmement flexibles et permettent de stocker et de manipuler des données de manière efficace.

### Création d'une liste

Pour **créer une liste** en Python, vous pouvez utiliser des crochets `[]` et séparer les éléments par des **virgules**. Voici comment créer une liste simple :

```python
ma_liste = [1, 2, 3, 4, 5]
```

Une liste peut contenir **n'importe quel type d'élément**, y compris **d'autres listes**. Par exemple :

```python
liste_mixte = [1, "texte", 3.14, [10, 20, 30]]
```

### Accès aux éléments d'une liste

Vous pouvez **accéder** aux **éléments individuels d'une liste** en utilisant leur **indice** (*position*) dans la **liste**. L'indice **commence à `0`** pour le **premier élément**. Voici comment accéder aux éléments d'une liste :

```python
ma_liste = [10, 20, 30, 40, 50]

# Accès au premier élément (indice 0)
premier_element = ma_liste[0]  # premier_element contient maintenant 10

# Accès au troisième élément (indice 2)
troisieme_element = ma_liste[2]  # troisieme_element contient maintenant 30
```

### Modification des éléments d'une liste

Les éléments d'une liste peuvent être **modifiés** en **utilisant leur indice**. Par exemple :

```python
ma_liste = [10, 20, 30, 40, 50]

# Modification du deuxième élément (indice 1)
ma_liste[1] = 25  # La liste devient maintenant [10, 25, 30, 40, 50]
```

### Ajout et suppression d'éléments

Pour **ajouter un élément à la fin d'une liste**, vous pouvez utiliser la **méthode** `append()` :

```python
ma_liste = [1, 2, 3]
ma_liste.append(4)  # La liste devient maintenant [1, 2, 3, 4]
```

Pour **supprimer un élément** en fonction de **sa valeur**, vous pouvez utiliser la **méthode** `remove()` :

```python
ma_liste = [1, 2, 3, 4, 5]
ma_liste.remove(3)  # La liste devient maintenant [1, 2, 4, 5]
```

Pour **supprimer un élément** en fonction de **son indice**, vous pouvez utiliser le **mot-clé** `del` :

```python
ma_liste = [1, 2, 3, 4, 5]
del ma_liste[2]  # La liste devient maintenant [1, 2, 4, 5]
```

À noter que la **suppression d'éléments dans une liste** n'est pas au programme de *première*, ni même de *terminale*. Vous ne serez donc pas interrogés dessus, mais cela peut s'avérer bien utile tout de même.

### Parcours d'une liste avec des boucles

Les **listes** sont souvent parcourues à l'aide de **boucles bornées** `for`. Voici comment **parcourir une liste** et **afficher ses éléments** :

{{ IDE('scripts/25.py') }}

Ce code affichera chaque élément de la liste sur une ligne différente.

Une **autre méthode** pour **parcourir une liste** et **afficher ses éléments** consiste à utiliser **l'indice de ses éléments** : On souhaite maintenant **parcourir**, à l'aide d'une boucle `for`, chaque élément à partir de l'**indice** `0` (indice du **premier élément**), et jusqu'à l'**indice du dernier élément**.

On peut faire cela en utilisant une boucle `for` avec la fonction `range()` pour **générer des indices**, puis en **accédant aux éléments de la liste** à l'aide de ces **indices**. Voici comment cela fonctionne :

{{ IDE('scripts/23.py') }}

Dans cet exemple, nous avons utilisé la fonction `len` sur `ma_liste` pour **obtenir la longueur de la liste**, c'est-à-dire **son nombre d'éléments**. Ensuite, nous avons utilisé `range(longueur)` pour générer une **séquence d'indices** de `0` à `longueur - 1`. À **chaque itération de la boucle**, nous avons **accédé** à **l'élément d'indice** `i` à l'aide de `ma_liste[i]`, puis nous l'avons **affiché**.

On aurait pu écrire ce programme de manière plus simple, comme ceci :

{{ IDE('scripts/24.py') }}

Ici, on a mis directement `len(ma_liste)` à l'intérieur du `range`, ce qui évite de créer une **variable** supplémentaire.

### À vous de jouer !

!!! note "Exercice : Manipulation de listes"
    Créez un **programme** en réalisant les tâches suivantes :

    1. **Créez une liste** appelée `nombres` contenant les **entiers** de `1` à `5`.
    2. Utilisez une **boucle** `for` pour **parcourir la liste** `nombres` et **afficher** chaque élément.
    3. **Modifiez la liste** `nombres` pour qu'elle contienne **les carrés des nombres de** `1` **à** `5`. Cela signifie que la liste doit maintenant contenir `[1, 4, 9, 16, 25]`.
    4. Utilisez à nouveau une **boucle** `for` pour **parcourir la liste mise à jour** et **afficher chaque élément**.

    ??? tip "Aide - Code à trous"
        Pour vous aider, vous pouvez réutiliser ce programme à trous :

        ```python
        # Créer une liste contenant les entiers de 1 à 5
        nombres = .......

        # Parcourir la liste et afficher chaque élément
        print("Liste d'origine :")
        for nombre in .......:
            print(.......)

        # Modifier la liste pour qu'elle contienne les carrés des nombres de 1 à 5
        for ... in range(.......):
            nombres[i] = ....... ** 2

        # Parcourir la liste mise à jour et afficher chaque élément
        print("\nListe mise à jour :")
        for nombre in .......:
            print(.......)
        ```
    
    Vous pouvez réaliser ce programme sur ***Thonny*** ou dans l'**IDE ci-dessous** (vous pourrez *télécharger* votre programme en cliquant sur le *deuxième bouton* pour le conserver.)

    {{ IDE() }}