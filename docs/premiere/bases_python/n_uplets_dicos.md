# Préliminaire : Les n-uplets et dictionnaires

Jusqu'à maintenant, on a vu comment utiliser les **listes Python** permettant de **stocker** des **séquences d'éléments** (de même nature ou non).

!!! quote ""
    Imaginons que nous souhaitions écrire un **programme** pour déterminer quel est le **mois** de l’**année** où **le plus d’élèves du lycée sont nés**. On suppose donnés, pour chaque élève, son **nom**, sous la forme d’une **chaîne de caractères**, et sa **date de naissance**, sous la forme de **trois entiers**. À l'aide des **listes**, on pourrait stocker ces informations de la manière suivante :

    ```python
    nom = [ "Alice", "Bob", "Charles", "Delphine", ... ]
    jour = [ 7, 9, 14, 11, ... ]
    mois = [ 1, 12, 12, 1, ... ]
    annee = [ 1941, 1909, 1965, 1938, ... ]
    ```

    Mais cette **représentation** n'est pas idéale. Si par exemple on souhaite trier les individus par **année de naissance**, on sera obligé de réorganiser les éléments dans les **quatre listes**, ce qui n'est pas le plus intuitif et le moins coûteux.

## Les n-uplets

Une première manière de répondre à cette problématique est de créer **une liste unique** dans lequel **chaque élément** contiendra **toutes les informations** sur la personne.

On pourrait faire ceci en utilisant des **listes de listes**, ce qui donnerait :

```python
individus = [["Alice", 7, 1, 1941], ["Bob", 9, 12, 1909], ["Charles", 14, 12, 1965], ["Delphine", 11, 1, 1938]]
```

Mais ce n'est pas l'idéal non plus car il est préférable qu'une **liste Python** contienne des **éléments homogènes** (c'est-à-dire de même type), ce qui n'est pas le cas ici.

!!! success "n-uplets en Python *(tuples)*"
    Une meilleure solution ici sera donc d'utiliser les **n-uplets** fournis par Python. Comme en **mathématiques**, un **n-uplet** est un **ensemble de valeurs** écrites entre **parenthèses** et **séparées par des virgules**. On peut, par exemple, affecter à une variable `x` un quadruplet de la manière suivante :

    ```python
    x = ("Alice", 7, 1, 1941)
    ```

    **<u>Opérations sur les n-uplets</u>** :

    Les opérations sont similaires à celles sur les listes :

    - `len(x)` renvoit la **longueur du tuple** stocké dans `x`, ici `4`,
    - `x[0]` renvoit le **premier élément du tuple** stocké dans `x`, ici `"Alice"`,
    - on peut **parcourir un tuple** avec une **boucle** :
        - `for i in range(len(x))` pour parcourir par **indice**,
        - `for element in x` pour parcourir directement les **éléments**.

    Par contre, <span style="color:rgb(200,0,0)">on ne peut pas **modifier un élément** d'un **tuple**</span>.

    Si on essaie, on obtient une **erreur** de type `TypeError` (erreur de **type**) :

    ```python
    >>> x[1] = 8
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment
    ```

Ainsi, si on reprend nos données précédentes, on peut écrire, en utilisant des **tuples** :

```python
individus = [("Alice", 7, 1, 1941), ("Bob", 9, 12, 1909), ("Charles", 14, 12, 1965), ("Delphine", 11, 1, 1938)]
```

On peut maintenant **parcourir cette liste de tuples** de différentes manières :

{{ IDE('scripts/33.py') }}

## Les dictionnaires

La **représentation** précédente n'est très pratique, car on doit retenir la nature de chaque information.

C'est pourquoi, une autre manière de représenter ces **données** est d'utiliser des **n-uplets nommés**, à l'aide d'une autre **structure de données** du langage **Python** appelé **<u>dictionnaire</u>**.

Un **dictionnaire** est une **structure** qui associe des **<u>valeurs</u>** à des **<u>clés</u>**. Ainsi, le dictionnaire

```python
{"nom":"Alice", "jour":7, "mois":1, "annee":1941}
```

contient **quatre clés**, ici les **chaînes de caractères** `"nom"`, `"jour"`, `"mois"` et `"année"`, auxquelles sont respectivement associées les **valeurs** `"Alice"`, `7`, `1` et `1941`.

!!! abstract ""
    Si l'on souhaite représenter les données de `individus` dans un **dictionnaire**, on peut écrire :

    ```python
    individus = [{'nom': "Alice", 'jour': 7, 'mois': 1, 'annee': 1941},
                {'nom': "Bob", 'jour': 9, 'mois': 12, 'annee': 1909},
                {'nom': "Charles", 'jour': 14, 'mois': 12, 'annee': 1965},
                {'nom': "Delphine", 'jour': 11, 'mois': 1, 'annee': 1938}]
    ```

Contrairement à un **tableau** (représenté avec une **liste** en *Python*), les **clés** d’un **dictionnaire** ne sont pas limitées à un ensemble d’entiers de la forme `0`, `1`, . . . , `n − 1`.

Un dictionnaire peut être construit en donnant explicitement toutes ses **entrées**, comme c'est le cas pour le **dictionnaire** précédent représentant l’élève `Alice`.  
On peut également en construire un à partir du **dictionnaire vide**, noté `{}`, en y ajoutant peu à peu des **entrées** avec des **affectations** de la forme `d[clé] = valeur`.

```python
>>> d = {}
>>> d["Homer"] = "le mari de Marge"
>>> d["Marge"] = "la femme d’Homer"
>>> d["Lisa"] = "la fille de Marge et Homer"
>>> d
{'Homer': 'le mari de Marge', 'Marge': 'la femme d’Homer', 'Lisa': 'la fille de Marge et Homer'}
>>> len(d)
3
```
L'ordre d'insertion **n'a pas d'importance**, puisque contrairement à une **liste** ou à un **tuple**, les **éléments** d'un **dictionnaire** ne sont **pas ordonnés**, ils sont affichés dans un **ordre arbitraire**.

On peut **accéder** à la **valeur associée** à une **clé** avec la construction `d[clé]` et on peut **tester** si le **dictionnaire possède une entrée** pour une certaine **clé** avec la construction `clé in d`.

```python
>>> d["Lisa"]
’la fille de Marge et Homer’
>>> "Lisa" in d
True
>>> "Bart" in d
False
```

!!! success ""
    Tester si un **dictionnaire** possède une **clé** donnée se fait de manière **quasiment instantanée** (en *temps constant*), ce qui est donc **moins coûteux** que de **chercher un élément dans une liste**, où la complexité est **linéaire** dans le *pire des cas* (puisqu'il faut parcourir chaque élément jusqu'à trouver le bon).

    Sans rentrer dans les détails, cela s'explique parce que les **dictionnaires**, tout comme les **ensembles** en *Python* (une autre structure qui n'est pas au programme) sont, en *interne*, implémentés à l'aide d'une *table de hachage*, une structure de données très efficace pour la **recherche** et l'**insertion** d'éléments.

Si on tente d’obtenir la **valeur associée** à une **clé** qui **n’est pas dans le dictionnaire**, cela lève une **erreur**. Par exemple :

```python
>>> d["Bart"]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: ’Bart’
```

Comme pour une **liste**, le contenu d’un dictionnaire peut être **modifié** après sa création, en remplaçant la **valeur associée à une clé** par une **autre valeur**, par exemple :

```python
>>> d["Lisa"] = "modèle de La Joconde"
>>> len(d)
3
>>> d["Lisa"]
’modèle de La Joconde’
```

Il est également possible de **supprimer une entrée du dictionnaire** avec l’instruction `del`.

```python
>>> del d["Lisa"]
>>> "Lisa" in d
False
>>> len(d)
2
```

### Parcourir un dictionnaire

Le **parcours des éléments** d'un dictionnaire peut se faire de **différentes façons**.

Si l'on prend le dictionnaire suivant :

```python
d = {"nom":"Alice", "jour":7, "mois":1, "annee":1941}
```

On peut parcourir les **clés** de la façon suivante :

{{ IDE('scripts/34.py') }}

On peut également **parcourir les clés** d'un **dictionnaire** avec la construction `d.keys()` :

{{ IDE('scripts/35.py') }}

Si l'on souhaite faire la même chose avec les **valeurs** associées aux **clés** du dictionnaire, le principe est le même mais avec la construction `d.values()` :

{{ IDE('scripts/36.py') }}

On peut également parcourir **à la fois les clés et les valeurs** avec la construction `d.items()`. Dans ce cas là, chaque élément sera un **tuple** de type `(clé, valeur)` :

{{ IDE('scripts/37.py') }}

### Dictionnaires par compréhension

Enfin, tout comme pour les **listes**, il est possible de **construire un dictionnaire par compréhension**, par exemple :

```python
>>> { x*x : x for x in range(10) }
{0: 0, 1: 1, 4: 2, 16: 4, 9: 3}
```

## Exercices - Tuples

!!! note "Exercice 1"
    Écrire une fonction `afficher(liste)` qui prend en entrée une **liste de tuples** représentant des données sur des élèves, de la forme :

    ```python
    [("Bastien", "Dubois", 15), ("Stéphane", "Carlier", 16), ("Vincent", "Duboeuf", 15)]
    ```

    Et qui effectue un **affichage** comme suit (en prenant l'exemple de la liste ci-dessus) :

    ```python
    Bastien Dubois - 15 ans
    Stéphane Carlier - 16 ans
    Vincent Duboeuf - 15 ans
    ```

??? tip "Correction exercice 1"
    Il y a plusieurs solutions pour écrire cette fonction.  
    On peut faire un **parcours** en récupérant **chaque tuple** contenu dans la **liste** :

    ```python
    def afficher(liste):
        for infos in liste:
            print(f"{infos[0]} {infos[1]} - {infos[2]} ans")
    ```

    On peut également récupérer directement **chaque information** des tuples (*prénom*, *nom* et *âge*) dans des **variables différentes** :

    ```python
    def afficher(liste):
        for prenom, nom, age in liste:
            print(f"{prenom} {nom} - {age} ans")
    ```

    On a ici utilisé des *f-strings* pour gérer les **affichages**.

    Pour des rappels concernant les différentes façons d'utiliser la fonction `print`, vous pouvez [consulter cette page de cours](../bases_python/cours.md#affichage-sur-la-sortie-standard).

## Exercices - Dictionnaires

!!! note "Notebooks"
    Voici un *notebook Capytale* d'introduction sur les **dictionnaires** :

    <center style="font-size:1.3em">
    [:octicons-link-external-16: Activité - Les dictionnaires en Python](https://capytale2.ac-paris.fr/web/c/833e-5256221)
    </center>

    D'autres exercices sur les dictionnaires et tuples :
    
    <center style="font-size:1.3em">
    [:octicons-link-external-16: D'autres exercices](https://capytale2.ac-paris.fr/web/c/c194-5253109)
    </center>