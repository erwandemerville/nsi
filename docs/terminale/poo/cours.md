??? quote "Sources"
    - [courspython](https://courspython.com/classes-et-objets.html){ target="_blank" }

# Programmation orientée objet

## Introduction

Vous avez vu en première différentes manières du **structurer des données** : avec des **listes**, des **tuples**, des **dictionnaires**... Tous ces **types de données de base** sont des **types natifs** de *Python*. Il s'agit de **<u>classes</u>** (`int`, `float`, `str`, `NoneType`...) déjà définies dans la **bibliothèque standard** distribuée avec **Python**.

Lorsque vous définissez par un exemple un **entier** `42` :

```python
nombre = 42
```

Vous créez ici ce que l'on appelle une **<u>instance</u>** de la **classe** `int`, que l'on appelle également un **<u>objet</u>**. **Un objet est une instance d'une classe**.

De même, lorsque vous définissez une **liste** :

```python
lst = [1,3,5]
```

Vous créez ici une **instance** de la **classe** `list` de **Python**.

La **programmation orientée objet** (ou *POO*) est le **paradigme de programmation** le **plus utilisé** du monde moderne. Des **smartphones** aux **superordinateurs**, des applications **de toutes tailles** utilisent ce **paradigme de programmation**. À l'issu de ce cours, vous serez capable d'aller beaucoup plus loin dans la conception de vos programmes !

## Créer une classe

Imaginons que l'on souhaite créer une **application numérique** demandant l’utilisation de **points repérés** par des **coordonnées dans un repère géométrique** à deux dimensions. Nous avons pour cela besoin d'au minimum **2 informations** : les coordonnées `x` et `y` de ce **point**.

En utilisant les **types de base** inclus avec le langage Python, on pourrait **représenter** ce point par un **tuple** `(x, y)`, une **liste** `[x, y]`, ou enocre un **dictionnaire** `{'x': x , 'y': y}`.'

Grâce à la **programmation orientée objet** (*POO*), nous allons **créer** une **nouvelle structure de données** à l'aide d'une **nouvelle classe** que l'on appellera `Point` :

```python
class Point:
    ''' Définition d'un point géométrique. '''
    pass
```

!!! tip "Convention en Python"
    Par convention, le **nom** identifiant une classe (qu’on appelle aussi son **identifiant**) débute par une **majuscule**. Ici `Point` débute par un **P** majuscule.

Une **classe** définit des <u>**attributs**</u> et des <u>**méthodes**</u> :

- Les **attributs** sont les **propriétés** qui caractériseront nos objets de type `Point`. Ici par exemple, on pourra créer **deux attributs** :
  - Un attribut `x` : La coordonnée en **abscisse** du point.
  - Un attribut `y` : La coordonnée en **ordonnée** du point.
- Les **méthodes** sont des **fonctions** définies à l'intérieur de notre classe et qui permettront d'effectuer des **actions** sur nos **objets** de type `Point`.

### Affectation à une variable de la référence à un objet

Nous avons défini notre classe `Point`. Pour créer une **instance** de cette **classe**, c'est-à-dire un **objet** de type `Point`, il suffit de saisir :

```python
Point()
```

Nous pouvons dès maintenant utiliser la classe `Point` pour **créer des objets** de ce **type**, par **instanciation**. Pour **créer** un **nouvel objet** et **stocker la référence à cet objet** dans la variable `p` :

```python
p = Point()
```

On peut vérifier à **quelle adresse mémoire** est stocké notre objet :

```python
>>> print(p)
<__main__.Point object at 0x7ff9c2f838d0>
```

Le message renvoyé par Python indique que `p` contient une **référence** à **une instance de la classe** `Point`, qui est définie elle-même au **niveau principal** du programme. Elle est située dans un emplacement bien défini de la mémoire vive, dont l’adresse apparaît ici en **notation hexadécimale**.

On peut créer **plusieurs points** (c'est-à-dire plusieurs **instances** de la classe `Point`) :

```python
p1 = Point()
p2 = Point()
```

Nous avons ici **2 instances** de la classe `Point` (soit **2 objets**) :

- la première à laquelle on fait référence au moyen de la variable `p1`,
- la seconde à laquelle on fait référence au moyen de la variable `p2`.

```python
>>> print(p1)
<__main__.Point object at 0x7ff9c2f83950>
>>> print(p2)
<__main__.Point object at 0x7ff9c2f839d0>
```

Par ailleurs, un **attribut prédéfini** `__doc__` permet de récupérer la **documentation** associée à notre classe :

```python
>>> print(p.__doc__)
Definition d'un point geometrique
```

### Définir les attributs

On peut définir nos attributs de la manière suivante :

```python
class Point:
    "Definition d'un point geometrique"
    pass

p = Point()
p.x = 1
p.y = 2
```

On peut afficher les valeurs de ces attributs :

```python
>>> print("p : x =", p.x, "y =", p.y)
p : x = 1 y = 2
```

Il faut bien faire la distinction entre **variable** et **objet** :

```python
class Point:
    "Definition d'un point geometrique"

a = Point()
a.x = 1
a.y = 2
b = a
print("a : x =", a.x, "y =", a.y)
print("b : x =", b.x, "y =", b.y)
a.x = 3
a.y = 4
print("a : x =", a.x, "y =", a.y)
print("b : x =", b.x, "y =", b.y)
```

[Visualiser sur Python Tutor](https://pythontutor.com/visualize.html#code=class%20Point%3A%0A%20%20%20%20%22Definition%20d'un%20point%20geometrique%22%0A%0Aa%20%3D%20Point%28%29%0Aa.x%20%3D%201%0Aa.y%20%3D%202%0Ab%20%3D%20a%0Aprint%28%22a%20%3A%20x%20%3D%22,%20a.x,%20%22y%20%3D%22,%20a.y%29%0Aprint%28%22b%20%3A%20x%20%3D%22,%20b.x,%20%22y%20%3D%22,%20b.y%29%0Aa.x%20%3D%203%0Aa.y%20%3D%204%0Aprint%28%22a%20%3A%20x%20%3D%22,%20a.x,%20%22y%20%3D%22,%20a.y%29%0Aprint%28%22b%20%3A%20x%20%3D%22,%20b.x,%20%22y%20%3D%22,%20b.y%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false){ .md-button target="_blank" }

Les variables `a` et `b` font ici référence **au même objet**. En effet, lors de l’affectation `b = a`, on met dans la variable `b` **la référence** contenue dans la variable `a`. Donc, toute modification des **valeurs** des **attributs** de l’**objet** dont la référence est contenue dans `a` provoque une modification pour `b`.

## Définir les méthodes

Une **méthode** est une **fonction définie à l'intérieur d'une classe**.

Par exemple, si l'on reprend notre classe `Point`, on peut par exemple créer une **méthode** permettant de **modifier** les **attributs** `x` et `y` en y **ajoutant** respectivement une valeur `dx` et `dy` données.

```python
class Point:
    "Definition d'un point geometrique"
    
    def deplacer(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
```

Si l'on veut **appeler** cette **méthode**, on procédera comme suit :

```python
a = Point()
a.x = 1  # initialiser l'attribut x à 1
a.y = 2  # initialiser l'attribut y à 2
print("a : x =", a.x, "y =", a.y)
a.deplacer(4, 6)  # Appel de la méthode deplacer de la classe Point
print("a : x =", a.x, "y =", a.y)
```

[Visualiser sur Python Tutor](https://pythontutor.com/render.html#code=class%20Point%3A%0A%20%20%20%20%22Definition%20d'un%20point%20geometrique%22%0A%20%20%20%20%0A%20%20%20%20def%20deplacer%28self,%20dx,%20dy%29%3A%0A%20%20%20%20%20%20%20%20self.x%20%3D%20self.x%20%2B%20dx%0A%20%20%20%20%20%20%20%20self.y%20%3D%20self.y%20%2B%20dy%0A%0Aa%20%3D%20Point%28%29%0Aa.x%20%3D%201%20%20%23%20initialiser%20l'attribut%20x%20%C3%A0%201%0Aa.y%20%3D%202%20%20%23%20initialiser%20l'attribut%20y%20%C3%A0%202%0Aa.deplacer%284,%206%29%20%20%23%20Appel%20de%20la%20m%C3%A9thode%20deplacer%20de%20la%20classe%20Point&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false){ .md-button target="_blank" }

Pour définir une méthode, il faut :

- indiquer son nom (ici `deplace()`).
- indiquer les **arguments** entre des **parenthèses**. Le premier argument d’une **méthode** doit être `self`.

Pour accéder aux méthodes d’un objet, on indique :

- le **nom de la variable** qui fait **référence à cet objet**
- un **point**
- le **nom de la méthode**

!!! warning "Le paramètre `self`"
    Lors d'un appel à une **méthode**, on ne passe pas d'**argument** pour le paramètre `self`, car la valeur qu'il prend est **la référence à l’objet**. Lors de l'appel, il y a donc toujours un paramètre de moins que lors de la définition de la méthode.

### Le constructeur

Jusqu'ici, nous avons défini **manuellement** les **attributs** des **instances** de notre classe `Point`. Si l'on crée plusieurs **objets**, nous sommes contraints de définir ces attributs pour chaque objet, ce qui peut être un petit peu rébarbatif.

Il existe une solution bien plus pratique pour automatiquement **définir des attributs** à chaque **création** d'un **nouvel objet** : Le **<u>constructeur</u>**.

Il s'agit d'une **méthode spéciale**, nommée `__init__`, **appelée à chaque création d'un objet**.

!!! info "Les méthodes spéciales"
    Les **méthodes spéciales**, ou **méthodes magiques**, comme `__init__`, possèdent toutes un nom **commençant par deux underscores** et **finissant par deux underscores**. Comme autres méthodes spéciales, on peut citer :

    - `__len__` : La valeur renvoyée par cette méthode peut être obtenue en appelant `len(objet)`, où `objet` est une instance d'une classe contenant la méthode `__len__`. Généralement, `len` fait référence à **une longueur** (si l'on a une classe `Liste` par exemple, cela pourrait permettre d'obtenir la longueur d'une liste.)
    - `__str__` : La valeur renvoyée par cette méthode, généralement une **chaîne de caractères**, sera **affichée** lors d'un appel à `print(objet)`, où `objet` est une instance d'une classe contenant la méthode `__str__`. C'est une méthode permettant de gérer un **affichage textuel** d'un objet.
    - `__eq__` : Cette méthode spéciale est appelée lorsque l'on **compare deux objets** avec un opérateur de comparaison `==`. Il existe également `__ne__` pour l'opérateur `!=`, `__le__` pour `<=`, `__ge__` pour `>=`, etc.
    - Il existe énormément d'autres méthodes spéciales, comme `__hash__`, `__bool__`, `__contains__`...

Voici une nouvelle définition de notre classe `Point` avec notre **constructeur** :

```python
class Point:
    def __init__(self):
        self.x = 0  # initialiser la position en x à 0
        self.y = 0  # initialiser la position en y à 0
```

Ici, le **constructeur** ne prend aucun paramètre en dehors du paramètre `self` (qui est obligatoire pour toutes les méthodes). Lors de la création d'un objet, deux attributs `x` et `y` sont initialisés :

```python
>>> p = Point()
>>> p.x
0
>>> p.y
0
```

On peut **ajouter d'autres paramètres** à notre **constructeur** :

```python
class Point:
    def __init__(self, x, y):
        self.x = x  # initialiser la position en x à 0
        self.y = y  # initialiser la position en y à 0
```

On peut sans problème avoir des paramètres qui portent les mêmes noms que les attributs, car les deux ne sont pas dans le même **espace de nom**. Les paramètres sont des variables locales à la fonction, tandis que les attributs de l'objet appartiennent à l'espace de nom de l'instance.

Il est également possible de faire en sorte que des paramètres soient **optionnels**, en leur attribuant une **valeur par défaut** :

```python
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x  # initialiser la position en x à 0
        self.y = y  # initialiser la position en y à 0
```

!!! warning "Paramètres optionnels"
    Les paramètres optionnels d'une fonction ou d'une méthode doivent toujours être placés en dernier. Par ailleurs, lors de l'appel d'une fonction, on peut nommer les paramètres pour lesquels on souhaite entrer une valeur.

    Par exemple :

    ```python
    def generer_liste(max, min = 0, pas = 1):
        return list(range(min, max + 1, pas))
    ```

    On pourrait appeler cette fonction de plusieurs manières, par exemple :

    ```python
    >>> generer_liste(10)
    >>> generer_liste(15, 5, 3)
    >>> generer_liste(10, pas = 2)
    >>> generer_liste(10, pas = 2, min = 5)
    ```

Voici une nouvelle version de notre classe `Point` incluant le **constructeur** et la **méthode** `deplacer`, n'hésitez pas à exécuter ce code et à le modifier à votre guise :

{{ IDE('scripts/01.py') }}

Il faut bien faire la distinction entre la **définition d'une classe**, et les **instances de cette classe**. Lors de la **création d'un objet** (c'est-à-dire d'une **instance d'une classe**), on passe des **arguments** (un peu comme lorsque l'on appelle une fonction), qui sont automatiquement passés en **entrées** du **constructeur de la classe**. Le constructeur va ensuite **définir les attributs** en utilisant ces valeurs.

### Accesseurs et mutateurs

- les **accesseurs** (ou *getters*) fournissent des informations relatives à l’état d’un objet, c’est-à-dire aux valeurs de certains de ses attributs sans les modifier ;
- les **mutateurs** (ou *setters*) modifient l’état d’un objet, donc les valeurs de certains de ses attributs.

!!! abstract "La notion d'*encapsulation*"
    L'**encapsulation** consiste à **masquer des données** de l'état interne pour **protéger l'intégrité** de l'**objet**.

    L'idée est de faire en sorte qu'un objet laisse les autres objets lire ses données, mais qu'il soit le seul à pouvoir les modifier.

    Concrètement, on fait utilise des **accesseurs** et des **mutateurs** pour **manipuler les attributs**, plutôt que de les modifier directement.

En reprenant notre classe `Point` et en lui ajoutant des **accesseurs** permettant d'**accéder aux attributs** `x` et `y` et des **mutateurs** permettant de **modifier** les attributs `x` et `y`, cela pourrait donner :

{{ IDE('scripts/02.py') }}

Dans notre `print`, nous n'accédons plus directement aux attributs de notre objet, mais l'on appelle cette fois les **accesseurs** qui se chargent de renvoyer la valeur de ces attributs.

!!! abstract "Membres *publiques*, *protégés* et *privés*"
    En **Python**, contrairement à d'autres langages comme le **Java** ou le **C++**, il n'est pas possible de **restreindre techniquement** l'**accès** à des **méthodes** ou des **attributs** d'une classe.

    Toutefois, il existe des **conventions** qui permettent d'indiquer des attributs ou des méthodes comme étant **publiques** (*public*), **protégés** (*protected*) ou **privés** (*private*).

    **Public** : Les attributs et méthodes **publiques** sont accessibles même **en dehors de la classe**.

    **Protected** : Les attributs et méthodes **protégés** commencent par **un underscore** et sont accessibles par une **classe** et ses **sous-classes** (les classes-filles, qui héritent de celle-ci).

    **Private** : Les attributs et méthodes **privés** commencent par **deux underscores** et sont **uniquement accessibles dans la classe où ils sont définis**. Si l'on essaie d'**accéder** à un attribut privé ou une méthode privée, une `AttributeError` sera levée. Mais il est facile de contourner cela, raison pour laquelle il ne s'agit pas d'une véritable restriction comme c'est le cas dans d'autres langages.

## Manipulation des objets

Voici quelques caractéristiques supplémentaires sur les classes :

- les **noms des classes** et des **attributs** permettent de **mieux décrire la nature des objets**, d'où l'intérêt de leur utilisation : `p = Point()` est plus explicite que `p = [0,0]` ou `p = (0,0)` par exemple, et `p.y` est plus clair que `p[1]` ;
- les **attributs** des objets peuvent être **d’autres objets**, ce qui permet de créer des **structures complexes** ;
- des **opérations similaires** peuvent être implémentées par des méthodes **de même nom** dans plusieurs classes.
- les **méthodes** étant liées à la **classe de l’objet lui-même** (contrairement à une fonction), cela permert une meilleure lisibilité du programme et évite ainsi certaubes erreurs de programmation.

!!! note "À vous de jouer"
    Écrire une nouvelle classe `Segment` qui **réutilise la classe** `Point` et qui contient :

    - Un **constructeur** qui **initialiser deux attributs**, `p1` et `p2`, deux objets de type `Point` fournis en arguments lors de la création de l'objet,
    - Une méthode `deplacer` qui prend deux paramètres `dx` et `dy` (ne pas oublier également `self`) et qui **déplace le segment** (c'est-à-dire les deux points du segments),
    - une méthode `milieu` qui ne prend pas de paramètres (en dehors de `self` bien sûr) et qui renvoie un **nouveau point** situé **au milieu du segment**.
    - une méthode spéciale `__len__` qui renvoie **la longueur du segment**, on rappelle la formule : si l'on a deux points $P1(X1, Y1)$ et $P2(X2, Y2)$, la longueur est $\sqrt{(X2-X1)² + (Y2-Y1)²}$

    En dessous de la définition des classes, des instructions qui permettent de **créer un nouveau segment** (c'est-à-dire une **instance** de la classe `Segment`) sont présentes. Après avoir exécuté le programme, vous pouvez faire des tests de manipulation de votre **objet** stocké dans `s` dans l'interpréteur Python. Pour appeler une **méthode** de la **classe** `Segment` sur votre objet dont la référence est stockée dans `s`, vous devrez donc saisir `s.nom_de_la_methode(ARGUMENTS ÉVENTUELS)`.

    Vous pouvez réaliser cet exercice directement ci-dessous, ou bien sur l'**IDE** de votre choix.

    {{ IDE('scripts/03.py') }}

## Attributs et méthodes de classes

(en construction...)

### Attributs de classes

(en construction...)

### Méthodes de classes

(en construction...)