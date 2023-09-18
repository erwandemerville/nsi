??? quote "Sources"
    - [courspython](https://courspython.com/classes-et-objets.html){ target="_blank" }

!!! warning "En construction"
    Ce cours est encore en construction. De nouvelles informations y seront ajoutées prochainement, et des modifications pourront être apportées.

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

- la première à laquelle on fait référence au moyen de la variable `a`,
- la seconde à laquelle on fait référence au moyen de la variable `b`.

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

### Le constructeur

(En construction...)

### Accesseurs et mutateurs

(En construction...)

## Manipulation des objets

(En construction...)