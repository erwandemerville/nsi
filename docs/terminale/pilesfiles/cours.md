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

...