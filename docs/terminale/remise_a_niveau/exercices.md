# Plus d'exercices

!!! note "Exercice 1"
    Réaliser une fonction `sommeLigneValeurTab` qui prend en paramètre un **tableau à deux dimensions** `tab` et **renvoie** une liste constituée des **sommes** de **chaque ligne** de `tab`. 0 si la liste est vide.

    ```python
    def sommeLigneValeurTab(tab):
        ...
    ```

    Pour vérifier votre fonction, vous pouvez ajouter ces **assertions** à votre programme :

    ```python
    assert sommeListeValeurTab([[1,0], [2,1]]) == [1, 3]
    assert sommeListeValeurTab([[1,1,1], [0,1,0]]) == [3, 1]
    assert sommeListeValeurTab([[1], [2], [3]]) == [1, 2, 3]
    assert sommeListeValeurTab([]) == []
    ```

!!! note "Exercice 2"
    Réaliser une fonction `insererListe` qui prend en paramètre une **liste d'entiers triée** `liste` et un **entier** `n` et qui **renvoie** une **nouvelle liste** constituée des **valeurs de la liste** avec l'élément `n` rangé au bon **indice**. 

    ```python
    def insererListe(liste, n):
        ...
    ```

    Pour vérifier votre fonction, vous pouvez ajouter ces **assertions** à votre programme :

    ```python
    assert insererListe([1, 2, 9], 5) == [1, 2, 5, 9]
    assert insererListe([1, 3, 6, 6, 8], 1) == [1, 1, 3, 6, 6, 8]
    assert insererListe([], 4) == [4]
    ```

!!! note "Exercice 3"
    On donne le **dictionnaire** suivant indiquant le **nom de produits** et le **prix** correspondant (en *euros*) :

    ```python
    dispo = {'Sabre laser': 229,
            'Etoile de ninja': 29.95,
            'Cape': 75,
            'Baguette': 35,
            'Chapeau': 12,
            'Bandeau': 12,
            'Balai': 130}
    ```

    1. Definir une fonction `dispo(p, dispo)` renvoyant `True` si le produit `p` est **présent** dans le **dictionnaire** `dispo` et `False` sinon.
    2. Definir une fonction `prix_moyen(dispo)` qui calcule et **renvoie** le **prix moyen** des **produits** proposés dans le dictionnaire `dispo` (qui contient au moins un produit).
    3. Definir une fonction `intervalle_prix(m, M, dispo)` qui **renvoie** l’ensemble des **noms de produits** du dictionnaire `dispo` dont le **prix** est compris entre `m` et `M`.