# Piles et files

## Présentation

Les **structures de <u>pile</u>** et de **<u>file</u>** permettent de **stocker des ensembles d'éléments** et fournissent des **opérations** permettant d'**ajouter** ou de **retirer** des **éléments** un à un.
Cependant, les **éléments retirés** ne le sont pas dans un **ordre arbitraire** :

- Dans une **pile** (en anglais *stack*), chaque opération de **retrait** retire **l'élément arrivé le plus récemment**. *Par exemple : une **pile d'assiettes**, dans laquelle chaque nouvelle assiette est ajoutée au-dessus des précédentes, et où l'assiette retirée est systématiquement celle du sommet, un peu comme pour les **tours de Hanoï**.*  
On parle de **méthode DEPS** pour *dernier entré, premier sorti*, ou en anglais **LIFO** pour *last in, first out*.  
<figure markdown>
  ![Exemple de pile](images/exemple_pile.png)
  <figcaption>Exemple de pile : une pile d'assiettes.<br />Source : <a href="https://www.zonensi.fr/NSI/Terminale/C03/Piles_et_files/#piles" target="_blank">ZoneNSI</a></figcaption>
</figure>

- Dans une structure de **file** (en anglais *queue*), chaque opération de **retrait** retire **l'élément qui avait été ajouté le premier**. *Par exemple : une file d'attente, dans laquelle des personnes arrivent à tour de rôle, patientent, et sont servies dans leur ordre d'arrivée.*  
On parle ici de **méthode PEPS** pour *premier entré, premier sorti*, ou en anglais **FIFO** pour *first in, first out*.  
<figure markdown>
  ![Exemple de file](images/exemple_file.png)
  <figcaption>Exemple de file : une file d'attente.<br />Source : <a href="https://www.zonensi.fr/NSI/Terminale/C03/Piles_et_files/#files" target="_blank">ZoneNSI</a></figcaption>
</figure>  

Chacune de ces deux **structures** (*pile* et *file*) possède une **interface** proposant **au minimum** les **opérations suivantes** :

- **créer** une **structure initialement vide**,
- **tester** si une **structure est vide**,
- **ajouter un élément** à une **structure**,
- **retirer** et **obtenir un élément** d'une **structure**.
  
Par ailleurs, tout comme dans le cas des **listes chaînées**, il est préférable (pour une question de logique) que les **piles** et les **files** soient des **structures homogènes**, c'est-à-dire que tous les éléments stockés soient de **même type**.

Le plus souvent, les structures de **pile** et de **file** sont considérées **mutables** : chaque opération d'**ajout** ou de **retrait** d'un élément **modifie directement la pile ou la file** sur laquelle elle est appliquée.  
Cela évite, dans le cas d'un **retrait** (*dépilement* pour une *pile* ou *défilement* pour une *file*) notamment, d'avoir à **renvoyer** à la fois l'**élément retiré** et la **pile après dépilement**.

On peut également ajouter des **opérations supplémentaires** à nos **structures**, comme par exemple :

- obtenir le **nombre d'éléments** contenus dans une **structure**,
- **vider** une **structure**,
- **obtenir un élément** d'une structure (celui qu'on aurait obtenu avec l'**opération de retrait**), mais **sans le retirer**,
- etc.

Comme dans le cas des **listes chaînées**, il y a plusieurs façons d'**implémenter** les structures de **piles** et de **files**. Mais avant d'étudier les implémentations possibles, nous allons définir un **interface** (ou un *type abstrait*) permettant de définir les **opérations élémentaires** utilisables dans le cas d'une **pile** et d'une **file**.

!!! abstract "Type abstrait *Pile*"
    Voici *une manière* de définir l'**interface** `Pile` représentant une **pile**.  
    *Note* : La notation $Pile[Element]$ correspond à une **pile** contenant des objets de type $Element$.

	**Utilise :** *Element*, *Entier*, *Booleen*<br />
	**Opérations fondamentales (primitives):**

    | Opération                                                    | Description                                                  |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | $nouvelle\_pile\_vide :~\rightarrow Pile~VIDE$                 | Renvoie une **nouvelle pile VIDE**.                         |
    | $est\_vide :~Pile \rightarrow Booleen$                   | Renvoie `True` si la pile donnée est **vide**, `False` sinon.   |
    | $empiler :~Pile[Element] \times Element \rightarrow \emptyset$ | Ajoute un **nouvel élément** donné au **sommet** d'une **pile d'éléments** donnée. |
    | $depiler :~Pile[Element] \rightarrow Element$                      | Retire l'**élément au sommet** de la **pile NON VIDE donnée**, et **renvoie cet élément**. |

    Voici quelques **opérations supplémentaires** :

    | Opération                                                  | Description                                                  |
    | ---------------------------------------------------------- | ------------------------------------------------------------ |
    | $nombre\_elements :~Pile[Elements] \rightarrow Entier$ | Renvoie le **nombre d'éléments** que contient une **pile donnée**. |
    | $vider :~Pile[Elements] \rightarrow \emptyset$                    | **Vide** le contenu de la **pile** donnée (supprime tous ses éléments).    |
    | $obtenir\_element :~Pile[Elements] \rightarrow Element$                 | Renvoie l'élément au **sommet de la pile** donnée, **sans le retirer**.     |

!!! abstract "Type abstrait *File*"
    Voici *une manière* de définir l'**interface** `File` représentant une **file**.  
    <span style="color:rgb(200,50,50)">(À compléter pour lundi 13/11/2023)</span>

	**Utilise :** *Element*, *Entier*, *Booleen*<br />
	**Opérations fondamentales (primitives):**

    | Opération                                                    | Description                                                  |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | $nouvelle\_file\_vide :~\rightarrow File~VIDE$                 | Renvoie une **nouvelle file VIDE**.                         |
    | $est\_vide :~File \rightarrow Booleen$                   | Renvoie `True` si la file donnée est **vide**, `False` sinon.   |
    | $enfiler :~File[Element] \times Element \rightarrow \emptyset$ | Ajoute un **nouvel élément** donné dans une **file d'éléments** donnée. |
    | $defiler :~File[Element] \rightarrow Element$                      | Retire le **premier élément ajouté** à la **file NON VIDE donnée**, et **renvoie cet élément**. |

    Voici quelques **opérations supplémentaires** :

    | Opération                                                  | Description                                                  |
    | ---------------------------------------------------------- | ------------------------------------------------------------ |
    | $nombre\_elements :~File[Elements] \rightarrow Entier$ | Renvoie le **nombre d'éléments** que contient une **file donnée**. |
    | $vider :~File[Elements] \rightarrow \emptyset$                    | **Vide** le contenu de la **file** donnée (supprime tous ses éléments).    |
    | $obtenir\_element :~File[Elements] \rightarrow Element$                 | Renvoie le **premier élément ajouté** à la **file** donnée, **sans le retirer**.     |

!!! warning "Type abstrait $\ne$ implémentation"
    On rappelle qu'il faut faire la distinction entre l'**interface** et les **implémentations**. On ne spécifie ici pas comment les données sont **représentées**, ni comment les opérations sont **implémentées**.

    Ces **définitions abstraites** du type **Pile** et **File**, bien qu'étant **mutables** (on modifie directement la structure plutôt que d'en renvoyer une nouvelle), n'empêchent toutefois pas de proposer par la suite des implémentations **non mutables**, tant que celles-ci suivent les **opérations définies**.

## Exemple d'utilisation d'une pile

Un exemple d'utilisation d'une **pile** : les opérations d'**accès à une nouvelle page web** et de **retour en arrière** (retour à la dernière page web) sur un navigateur.

On pourrait, en *Python*, définir ces **opérations** de cette manière :

```python
adresse_courante = ""
adresses_precedentes = nouvelle_pile_vide()

def aller_a(adresse_cible):
    adresses_precedentes.empiler(adresse_courante)
    adresse_courante = adresse_cible

def retour():
    if not adresses_precedentes.est_vide():
        adresse_courante = adresses_precedentes.depiler()
```

## Implémentations d'une pile

On fait le choix d'**implémenter** notre **pile** en utilisant la **POO** (programmation orientée objet). On va donc créer une classe `Pile` permettant de **représenter une pile**.

Par ailleurs, tout comme dans notre définition abstraite précédente, on choisit de travailler avec une structure **mutable**.
Cela signifie que les **opérations** `empiler` et `depiler` **modifieront directement la pile**, plutôt que de **renvoyer une nouvelle pile**.

### Avec une liste Python

Nous allons donc créer une classe `Pile` pour représenter notre **pile**, mais il nous faut également une autre **structure de données** pour **stocker** les **éléments de la pile**.
Pour cela, nous allons dans un premier temps utiliser une **liste Python**.

Ainsi, notre classe `Pile` contiendra **un seul attribut**, que nous nommerons `contenu`, qui sera donc de type `list` et qui contiendra tous les **éléments** de la **pile**. Pour une question d'**homogénéité**, notre pile ne contiendra que des **nombres entiers** (type `int`).

!!! note ""
    Ainsi :

    - l'opération `empiler`, permettant d'**ajouter** un **nouvel élément** au **sommet de la pile**, ajoutera cet élément **à la fin** de la *liste Python* de l'attribut `contenu`,
    - l'opération `depiler`, permettant de **retirer** et de **renvoyer** l'élément situé au **sommet de la pile**, retirera et renverra l'élément situé **à la fin** de la *liste Python* de l'attribut `contenu`.

Voici le **squelette** de notre classe `Pile` :

```python
class Pile:

    def __init__(self: 'Pile'):
        ''' Constructeur de la classe Pile. '''

        self.contenu = []

    # Opérations de base

    def est_vide(self: 'Pile') -> bool:
        ''' Renvoie True si la pile est vide, False sinon. '''

        pass

    def empiler(self: 'Pile', elt: int) -> None:
        ''' Empile un élément donné au sommet de la pile. '''

        pass
    
    def depiler(self: 'Pile') -> None:
        ''' Dépiler l'élément situé au sommet de la pile NON VIDE. '''

        pass

    # Autres opérations

    def nombre_elements(self: 'Pile') -> int:
        ''' Renvoie le nb d'éléments de la pile. '''

        pass

    def vider(self: 'Pile') -> None:
        ''' Vide la pile (supprime tous ses éléments). '''

        pass

    def obtenir_element(self: 'Pile') -> int:
        ''' Renvoie l'élément au sommet de la pile NON VIDE SANS LE SUPPRIMER. '''

        pass
        
    '''
```

!!! success ""
    Cette **classe** `Pile` contient :

    - **un attribut** :
        - `contenu`, de type `list`, contenant **les éléments** (en l'occurence des **entiers**, de type `int`) contenus dans la **pile**.
    - **trois méthodes** représentant les **opérations de base** :
        - `est_vide` : **prédicat** qui renvoie `True` si la **pile** est **vide**, et `False` sinon,
        - `empiler` : permet d'**ajouter** un **nouvel élément** `elt` donné au **sommet de la pile**,
        - `depiler` : permet de **retirer** et de **renvoyer** l'**élément** situé au **sommet de la pile**.
    - **trois méthodes** représentant d'**autres opérations** utiles :
        - `nombre_elements` : renvoie le **nombre d'éléments** de la **pile**,
        - `vider` : **retire tous les éléments** de la **pile**,
        - `obtenir_element` : renvoie l'**élément** situé **au sommet de la pile**, **sans le retirer** de la pile.

!!! warning "Annotations de type"
    On a ici utilisé des **annotations de type**, par exemple :  
    `def empiler(self: 'Pile', elt: int) -> None` : les annotations utilisées permettent d'indiquer que le paramètre `self` est de type `Pile`, que le paramètre `elt` est de type `int`, et que la **méthode** ne **renvoie rien** (`None`).

    Les **annotations de type** servent juste d'**indications** et n'ont aucun effet sur l'exécution du programme.

??? tip "Voir l'implémentation complète"
    Voici finalement notre implémentation :

    ```python
    class Pile:

        def __init__(self: 'Pile'):
            ''' Constructeur de la classe Pile. '''

            self.contenu = []

        # Opérations de base

        def est_vide(self: 'Pile') -> bool:
            ''' Renvoie True si la pile est vide, False sinon. '''

            return not self.contenu

        def empiler(self: 'Pile', elt: int) -> None:
            ''' Empile un élément donné au sommet de la pile. '''

            self.contenu.append(elt)
        
        def depiler(self: 'Pile') -> None:
            ''' Dépiler l'élément situé au sommet de la pile NON VIDE. '''

            if self.est_vide():
                raise ValueError("Erreur : Impossible de dépiler sur une pile vide !")
            return self.contenu.pop()

        # Autres opérations

        def nombre_elements(self: 'Pile') -> int:
            ''' Renvoie le nb d'éléments de la pile. '''

            return len(self.contenu)

        def vider(self: 'Pile') -> None:
            ''' Vide la pile (supprime tous ses éléments). '''

            self.contenu = []

        def obtenir_element(self: 'Pile') -> int:
            ''' Renvoie l'élément au sommet de la pile NON VIDE SANS LE SUPPRIMER. '''

            if self.est_vide():
                raise ValueError("Erreur : La pile est vide !")
            return self.contenu[self.nombre_elements() - 1]
    ```

### Avec une liste chaînée

On va cette fois utiliser une **liste chaînée** pour représenter le **contenu** de notre `Pile`.  
On va pour cela ré-utiliser notre classe `Cellule` présentée dans le [cours sur les listes chaînées](../listes/cours.md/#implementations-des-listes-chainees){ target="_blank" }.

!!! note "Implémentation des listes chaînées"
    Avec notre choix d'**implémentation** des **listes chaînées**, une **liste chaînée** est soit :

    - une **liste chaînée VIDE** représentée par l'objet `None`,
    - une **liste chaînée NON VIDE** représentée par une **instance** de la classe `Cellule` de la manière suivante : `Cellule(<premier élément>, <cellule suivante>)`.

Initialement, l'**attribut** `contenu` sera donc égal à `None`, représentant une **liste chaînée vide**.

!!! note ""
    On procédera de la manière suivante :

    - l'opération `empiler`, permettant d'**ajouter** un **nouvel élément** au **sommet de la pile**, ajoutera cet élément **au début** de la *liste chaînée* de l'attribut `contenu`,
    - l'opération `depiler`, permettant de **retirer** et de **renvoyer** l'élément situé au **sommet de la pile**, retirera et renverra l'élément situé **au début** de la *liste chaînée* de l'attribut `contenu`.

    En effet, ajouter les éléments **à la fin de la liste chaînée** serait coûteux car, à chaque **empilement** ou **dépilement**, il faudrait **parcourir entièrement la liste** pour aller chercher la **dernière cellule** ! Alors qu'en ajoutant les éléments** au début de la liste chaînée**, on a **pas de parcours** à effectuer.

Voici le **squelette** de notre classe `Pile` :

```python
class Cellule:
    ''' Une cellule d'une liste chaînée. '''

    def __init__(self, v, s):
        self.valeur = v  # Valeur contenue dans la cellule
        self.suivante = s  # Cellule suivante

class Pile:

    def __init__(self: 'Pile'):
        ''' Constructeur de la classe Pile. '''

        self.contenu = None

    # Opérations de base

    def est_vide(self: 'Pile') -> bool:
        ''' Renvoie True si la pile est vide, False sinon. '''

        pass

    def empiler(self: 'Pile', elt: int) -> None:
        ''' Empile un élément donné au sommet de la pile. '''

        pass
    
    def depiler(self: 'Pile') -> None:
        ''' Dépiler l'élément situé au sommet de la pile NON VIDE. '''

        pass

    # Autres opérations

    def nombre_elements(self: 'Pile') -> int:
        ''' Renvoie le nb d'éléments de la pile. '''

        pass

    def vider(self: 'Pile') -> None:
        ''' Vide la pile (supprime tous ses éléments). '''

        pass

    def obtenir_element(self: 'Pile') -> int:
        ''' Renvoie l'élément au sommet de la pile NON VIDE SANS LE SUPPRIMER. '''

        pass
    '''

```

??? tip "Voir l'implémentation complète"

    ```python
    class Cellule:
        ''' Une cellule d'une liste chaînée. '''

        def __init__(self, v, s):
            self.valeur = v  # Valeur contenue dans la cellule
            self.suivante = s  # Cellule suivante

    class Pile:

        def __init__(self: 'Pile'):
            ''' Constructeur de la classe Pile. '''

            self.contenu = None

        # Opérations de base

        def est_vide(self: 'Pile') -> bool:
            ''' Renvoie True si la pile est vide, False sinon. '''

            return self.contenu is None

        def empiler(self: 'Pile', elt: int) -> None:
            ''' Empile un élément donné au sommet de la pile. '''

            self.contenu = Cellule(elt, self.contenu)
        
        def depiler(self: 'Pile') -> None:
            ''' Dépiler l'élément situé au sommet de la pile NON VIDE. '''

            if self.est_vide():
                raise ValueError("Erreur : Impossible de dépiler sur une pile vide !")
            res = self.contenu.valeur
            self.contenu = self.contenu.suivante
            return res

        # Autres opérations

        def nombre_elements(self: 'Pile') -> int:
            ''' Renvoie le nb d'éléments de la pile. '''

            res = 0
            c = self.contenu
            while c is not None:
                res += 1
                c = c.suivante
            return res

        def vider(self: 'Pile') -> None:
            ''' Vide la pile (supprime tous ses éléments). '''

            self.contenu = None

        def obtenir_element(self: 'Pile') -> int:
            ''' Renvoie l'élément au sommet de la pile NON VIDE SANS LE SUPPRIMER. '''

            if self.est_vide():
                raise ValueError("Erreur : La pile est vide !")
            return self.contenu.valeur
        '''
    ```

## Implémentations d'une file

Comme précédemment, on fait le choix d'implémenter notre **file** en utilisant la **POO**. On va donc créer une classe `File` permettant de **représenter une file**.

Ici aussi, on travaillera avec une structure **mutable**.
Cela signifie que les **opérations** `enfiler` et `defiler` **modifieront directement la file**, plutôt que de **renvoyer une nouvelle file**.

### Avec une liste Python

Ici, on représentera le **contenu de la file** avec une **liste Python** (qui sera affectée à un attribut `contenu`, comme pour notre première implémentation des piles).

!!! note ""
    Cette fois, les **éléments** ajoutés à la **file** (**enfilés**) seront ajoutés **d'un côté** de la *liste Python* de l'attribut `contenu`, et les **éléments défilés** seront retirés **de l'autre côté** de la *liste Python* de l'attribut `contenu`, puisque le *premier élément entré est le premier sorti*. On pourra procéder comme suit :

    - l'opération `enfiler`, permettant d'**ajouter** un **nouvel élément** à la **file**, ajoutera cet élément **à la fin** de la *liste Python* de l'attribut `contenu`,
    - l'opération `defiler`, permettant de **retirer** et de **renvoyer** un élément de la **file**, retirera et renverra l'élément situé **au début** de la *liste Python* de l'attribut `contenu`.

??? tip "Voir l'implémentation complète"
    ```python
    class File:
        def __init__(self):
            ''' Constructeur de la classe File.
            :param contenu: (list[int]) une liste d'entiers '''

            self.contenu = []
            
        def est_vide(self) -> bool:
            ''' Renvoie True si la file est vide, False sinon.'''
            
            return not self.contenu

        def enfiler(self, elt) -> None:
            ''' Enfile un élément dans la file. '''
            
            self.contenu.append(elt)
        
        
        def defiler(self) -> int:
            ''' Défile le premier élément ajouté à la file, et le renvoie.
            LEVER UNE ERREUR si la file est VIDE. '''

            if self.est_vide():
                raise ValueError("La liste ne doit pas être vide")
            else:
                return self.contenu.pop(0)
        
        def nombre_elements(self) -> int:
            ''' Renvoie le nombre d'éléments de la file. '''

            return len(self.contenu)
        
        def vider(self) -> None:
            ''' Vide la file (supprime tous ses éléments). '''

            self.contenu = []
        
        def obtenir_element(self) -> int:
            ''' Renvoie le premier élément ajouté à la file sans le supprimer. '''

            if self.est_vide():
                raise ValueError("La liste ne doit pas être vide")
            else:
                return self.contenu[0]
    ```

### Avec une liste chaînée

Cette fois, l'implémentation d'une **file** avec une **liste chaînée** diffèrera un petit peu de notre implémentation d'une **pile**.

En effet, dans une **pile**, on ajoutait et retirait les éléments du **même côté** de la **liste chaînée** utilisée pour stocker son contenu, puisque **dépiler** un élément dans une pile consiste à retirer le dernier élément ajouté.
L'opération `empiler` consistait donc à **ajouter** un **élément** en **tête** de la **liste chaînée**, et l'opération dép`iler retirait l'**élément** en **tête** de la **liste chaînée**.

Ici, dans le cas d'une **file**, on devra **ajouter** les **éléments** d'**un côté** de la **liste chaînée**, puis les **retirer** de l'**autre côté** de la **liste chaînée**.
Pour éviter d'effectuer des **parcours de liste chaînée**, qui sont **coûteux**, on implémentera notre classe `File` avec **deux attributs** :

- un attribut `tete` qui contiendra la **référence** de la **cellule tête** de la **liste chaînée** permettant de stocker les **éléments** de la **file**,
- un attribut `queue` qui contiendra la **référence** de la **cellule queue** de la **liste chaînée** permettant de stocker les **éléments** de la **file**.

Ainsi :

- la méthode `enfiler` de notre classe `File` **ajoutera** un **élément** à la **queue** de la **liste chaînée**,
- la méthode `defiler` de notre classe `File` **retirera** l'**élément** situé en **tête** de la **liste chaînée**.

??? tip "Voir l'implémentation complète"
    ```python
    class Cellule:
        ''' Implémentation d'une liste chaînée. '''
        
        def __init__(self, v, s):
            self.valeur = v  # valeur de la cellule
            self.suivante = s  # cellule suivante

    class File:
        
        def __init__(self: 'File'):
            # La liste chaînée ne contient initialement aucune cellule,
            # donc la tête et la queue sont initialisées à None
            self.tete = None
            self.queue = None
        
        def est_vide(self: 'File') -> bool:
            # Si la liste chaînée est vide, la tête et la queue contiennent None.
            return self.tete is None
        
        def enfiler(self: 'File', elt: int) -> None:
            a = Cellule(elt, None)  # on crée la nouvelle cellule que l'on ajoutera en queue de la liste chaînée
            if self.est_vide():
                # Si la liste chaînée est vide, la nouvelle cellule ajoutée
                # sera alors à la fois la cellule tête et la cellule queue.
                self.tete = a
            else:
                # Sinon, on lie l'ancienne cellule queue de la liste chaînée à notre nouvelle cellule.
                self.queue.suivante = a
            self.queue = a  # quoiqu'il en soit, la nouvelle cellule créée devient la queue de la liste chaînée
        
        def defiler(self: 'File') -> int:
            if self.est_vide():
                # On ne peut pas défiler sur une file vide, donc on lève une erreur.
                raise IndexError("Impossible de défiler sur une file vide !")
            j = self.tete.valeur  # on stocke la valeur de la cellule tête actuelle de la liste chaînée
            self.tete = self.tete.suivante  # la nouvelle cellule tête est la cellule qui suit l'ancienne
            if self.tete is None:  # si la nouvelle cellule tête est vide :
                self.queue = None  # cela signifie que la liste chaînée est vide, donc la queue vaut aussi None
            return j  # on renvoie la valeur de l'ancienne cellule tête que l'on avait stocké dans j
    ```

## Exercices

!!! note "Exercice 1"
    On souhaite utiliser une **pile** pour vérifier si une **expression arithmétique** est **bien parenthésée**. Écrire une fonction `est_bien_parenthesee(chaine)` qui renvoie `True` si l'expression est **bien parenthésée**, `False` sinon.

    Par exemple :  
    `est_bien_parenthesee('(1 + 3) * (6 + 7)')` renverra `True`.  
    `est_bien_parenthesee('(6 + (4 * 5) - (2 + 1)')` renverra `False`.

??? tip "Correction exercice 1"

    ```python
    def est_bien_parenthesee(chaine):
        pile = Pile()
        for c in chaine:
            if c == "(":
                pile.empiler(c)
            elif c == ")":
                if pile.est_vide():
                    return False
        return pile.est_vide()
    ```

!!! note "Exercice 2"
    L'écriture polonaise inverse des expressions arithmétiques place l'opérateur après ses opérandes. Cette notation ne nécessite aucune parenthèse ni aucune règle de priorité. Ainsi, l'expression polonaise inverse décrite par la chaîne de caractères `1 2 3 * + 4 *` désigne l'expression traditionnellement notée $(1 + 2 \times 3) \times 4$. 

    La valeur d'une telle expression peut être calculée facilement en utilisant une **pile** pour stocker **les résultats intermédiaires**. Pour cela, on observe un à un les éléments de l'expression et on effectue les actions suivantes:
    
    - si on voit un nombre, on le place sur la pile;
    - si on voit un opérateur binaire, on récupère les deux nombres au sommet de la pile, on leur applique l'opérateur, et on replace le résultat sur la pile.
  
    Si l'expression était bien écrite, il y a bien toujours deux nombres sur la pile lorsque l'on voit un opérateur, et à la fin du processus il reste exactement un nombre sur la pile, qui est le résultat.
    
    **Écrire** une **fonction** prenant en **paramètre** une **chaîne de caractères** représentant une expression en **notation polonaise inverse** composée d'**additions** et de **multiplications** de **nombres entiers** et **renvoyant la valeur de cette expression**. On supposera que les éléments de l'expression sont séparés par des **espaces**.
    
    *Attention* : cette fonction ne doit pas renvoyer de résultat si l'expression est mal écrite. 

??? tip "Correction exercice 2"
    On **itère** sur les **éléments obtenus** en **découpant la chaîne** au niveau des **espaces**. 
    On isole d'abord les cas des opérateurs, qui sont les plus faciles à identifier, et on suppose que tout ce qui n'est pas `+` ou `*` est un **entier** (cette branche échouera si on trouve encore autre chose dans l'expression).
    
    À la fin, on **dépile** le **dernier élément** et on **vérifie** que la **pile** est bien **vide** avant de **renvoyer ce résultat**. Si à un moment donné, il était **impossible de dépiler**, alors le programme aura de toute façon **échoué**.
    
    ```python
    def eval_polonaise_inverse(s):
        pile = Pile()
        for e in s.split(" "):
            if e == "+" or e == "*":
                x = pile.depiler()
                y = pile.depiler()
                z = x + y if e == "+" else x * y
                pile.empiler(z)
            else:
                pile.empiler(int(e))
        res = pile.depiler()
        assert pile.est_vide()
        return res
    ```