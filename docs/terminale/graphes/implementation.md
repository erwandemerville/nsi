# Implémentation des graphes en Python

Comme nous l'avons vu dans le [cours](cours.md), il existe **deux manières** de **représenter les graphes** :

- en utilisant les **listes d'adjacence** (ou *listes de successeurs*),
- en utilisant des **matrices d'adjacence**.

Dans cette partie, nous **implémenterons** la **structure de graphe** en *Python* en choisissant comme **paradigme** la **programmation orientée objet** (*POO*).

Nous proposerons une première implémentation en utilisant une **liste d'adjacence** que l'on implémentera en *Python* sous la forme d'un **dictionnaire**. Nous élaborerons ensuite une seconde implémentation en utilisant une **matrice d'adjacence**, implémentée sous la forme d'une **liste de listes**.

On distinguera une structure de **graphe non-orienté**, et une structure de **graphe orienté**.

## Graphe non-orienté

### Type abstrait

Avant d'implémenter notre **structure de graphe** en Python, définissons tout d'abord le **type abstrait `Graphe`**, ainsi que les **opérations** qui y sont associées.

!!! abstract "Type abstrait *Graphe*"

	**Utilise :** *Sommet*, *Entier*, *Booléen*, *Liste*<br />
	**Opérations de base :**<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $nouveau\_graphe :~\rightarrow Graphe$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $ajouter\_sommet :~Graphe \times Sommet \rightarrow Graphe$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $ajouter\_arete :~Graphe \times Sommet \times Sommet \rightarrow Graphe$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $supprimer\_sommet :~Graphe \times Sommet \rightarrow Graphe$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $supprimer\_arete :~Graphe \times Sommet \times Sommet \rightarrow Graphe$<br />
	**Autres opérations :**<br />
    &nbsp;&nbsp;&nbsp;&nbsp; $est\_sommet :~Graphe \times Sommet \rightarrow Booléen$<br />
    &nbsp;&nbsp;&nbsp;&nbsp; $est\_arete :~Graphe \times Sommet \times Sommet \rightarrow Booléen$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $ordre :~Graphe \rightarrow Entier$<br />
    &nbsp;&nbsp;&nbsp;&nbsp; $degre :~Graphe \times Sommet \rightarrow Entier$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $voisins :~Graphe \times Sommet \rightarrow Liste$<br />

### Implémentation avec un dictionnaire

!!! note "À faire"
    **Téléchargez** le **fichier Python** ci-dessous :

    <center>
    [:material-cursor-default-click: Télécharger `graphe.py`](src/imple_graphe.py){ style="font-size:1.2em" target="_blank" }
    </center>

    Complétez chaque **méthode** de la classe `Graphe` (à l'exception de la méthode `affiche` qui vous est donnée.)

!!! tip "Test de votre classe"

    Dans le bloc en bas de script `if __name__ == "__main__"`, ajoutez les instructions suivantes :

    ```python
    graphe = Graphe()  # création d'un nouveau graphe
    graphe.ajouter_arete('A', 'B')  # ajout d'une arête entre A et B
    graphe.ajouter_arete('B', 'C')  # ajout d'une arête entre B et C
    graphe.ajouter_arete('C', 'D')  # ajout d'une arête entre C et D
    graphe.ajouter_arete('D', 'A')  # ajout d'une arête entre D et A
    graphe.ajouter_arete('A', 'C')  # ajout d'une arête entre A et C
    graphe.affiche()  # afficher le graphe
    ```

    Si votre programme est correct, vous devriez obtenir la visualisation suivante en exécutant votre programme :

    ![Test Graphe](images/graphe_test.png){ width="450" }