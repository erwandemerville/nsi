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

    !!! warning "Type abstrait $\ne$ implémentation"
        On rappelle qu'il faut faire la distinction entre l'**interface** et les **implémentations**. On ne spécifie ici pas comment les données sont **représentées**, ni comment les opérations sont **implémentées**.

        Cette **définition abstraite** du type **Pile**, bien qu'étant **mutable** (on modifie directement la **pile** plutôt que d'en renvoyer une nouvelle), n'empêche toutefois pas de proposer par la suite une implémentation **non mutable**, tant que celle-ci suit les opérations définies.

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

### Avec une liste Python

On va utiliser une **liste Python** pour représenter le **contenu** de la pile.

**Copiez-collez** le **code suivant** dans *Thonny* :

```python
class Pile:

    def __init__(self):
        ''' Constructeur de la classe Pile. '''

        self.contenu = []

    # Opérations de base

    def est_vide(self) -> bool:
        ''' Renvoie True si la pile est vide, False sinon. '''

        pass

    def empiler(self, elt) -> None:
        ''' Empile un élément au sommet de la pile. '''

        pass
    
    def depiler(self, elt) -> None:
        ''' Dépiler l'élément au sommet de la pile. '''

        pass

    # Autres opérations

    def nombre_elements(self) -> int:
        ''' Renvoie le nb d'éléments de la pile. '''

        pass

    def vider(self) -> None:
        ''' Vide la pile (supprime tous ses éléments). '''

        pass

    def obtenir_element(self) -> int:
        ''' Renvoie l'élément au sommet de la pile SANS LE SUPPRIMER. '''

        pass
        
    '''
```

### Avec une liste chaînée

On va cette fois utiliser une **liste chaînée** pour représenter le **contenu** de notre `Pile`.

**Copiez-collez** le **code suivant** dans *Thonny* :

```python
class Cellule:
    ''' Une cellule d'une liste chaînée. '''

    def __init__(self, v, s):
        self.valeur = v  # Valeur contenue dans la cellule
        self.suivante = s  # Cellule suivante

class Pile:

    def __init__(self):
        ''' Constructeur de la classe Pile. '''

        self.contenu = None

    # Opérations de base

    def est_vide(self) -> bool:
        ''' Renvoie True si la pile est vide, False sinon. '''

        pass

    def empiler(self, elt) -> None:
        ''' Empile un élément au sommet de la pile. '''

        pass
    
    def depiler(self, elt) -> None:
        ''' Dépiler l'élément au sommet de la pile. '''

        pass

    # Autres opérations

    def nombre_elements(self) -> int:
        ''' Renvoie le nb d'éléments de la pile. '''

        pass

    def vider(self) -> None:
        ''' Vide la pile (supprime tous ses éléments). '''

        pass

    def obtenir_element(self) -> int:
        ''' Renvoie l'élément au sommet de la pile SANS LE SUPPRIMER. '''

        pass

    '''

```

## Exercices

!!! note "Exercice 1"
    On souhaite utiliser une **pile** pour vérifier si une **expression arithmétique** est **bien parenthésée**. Écrire une fonction `est_bien_parenthesee(chaine)` qui renvoie `True` si l'expression est **bien parenthésée**, `False` sinon.

    Par exemple :  
    `est_bien_parenthesee('(1 + 3) * (6 + 7)')` renverra `True`.  
    `est_bien_parenthesee('(6 + (4 * 5) - (2 + 1)')` renverra `False`.

!!! note "Exercice 2"
    L'écriture polonaise inverse des expressions arithmétiques place l'opérateur après ses opérandes. Cette notation ne nécessite aucune parenthèse ni aucune règle de priorité. Ainsi, l'expression polonaise inverse décrite par la chaîne de caractères `1 2 3 * + 4 *` désigne l'expression traditionnellement notée $(1 + 2 \times 3) \times 4$. 

    La valeur d'une telle expression peut être calculée facilement en utilisant une **pile** pour stocker **les résultats intermédiaires**. Pour cela, on observe un à un les éléments de l'expression et on effectue les actions suivantes:
    
    - si on voit un nombre, on le place sur la pile;
    - si on voit un opérateur binaire, on récupère les deux nombres au som-met de la pile, on leur applique l'opérateur, et on replace le résultat sur la pile.
  
    Si l'expression était bien écrite, il y a bien toujours deux nombres sur la pilelorsque l'on voit un opérateur, et à la fin du processus il reste exactementun nombre sur la pile, qui est le résultat.
    
    **Écrire** une **fonction** prenant en **paramètre** une **chaîne de caractères** représentant une expression en **notation polonaise inverse** composée d'**additions** et de **multiplications** de **nombres entiers** et **renvoyant la valeur de cette expression**. On supposera que les éléments de l'expression sont séparés par des **espaces**.
    
    *Attention* : cette fonction ne doit pas renvoyer de résultat si l'expression est mal écrite. 