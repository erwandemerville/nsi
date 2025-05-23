# Exercice Python - Voyageur de commerce

L'objectif de cet exercice est d'**implémenter** en *Python* un ==**algorithme glouton**== permettant de résoudre le problème du [voyageur de commerce](cours.md#probleme-du-voyageur-de-commerce).

!!! success "À télécharger"
    Voici le programme *Python* que vous devrez compléter :

    <center style="font-size:1.3em">
    [Télécharger `voyageur_commerce_glouton.py`](src/voyageur_commerce_glouton.py)
    </center>

    Voici un programme **déjà complet** permettant de tester la **résolution** du problème du **voyageur de commerce** avec la **méthode par force brute** :

    <center style="font-size:1.3em">
    [Télécharger `voyageur_commerce_bf.py`](src/voyageur_commerce_bf.py)
    </center>

!!! info ""
    Vous répondrez aux questions suivantes **sur une feuille**.

!!! note "Exercice 1"
    Ouvrez le **programme** `voyageur_commerce_bf.py`.

    L'algorithme de **résolution par force brute** peut être testé avec un **maximum** de **14 villes de France**, définies dans la liste `villes`. Les **distances** entre chaque ville sont définies dans le tableau `distances`.

    La **ville de départ** est indiquée dans la constante `VILLE_DEPART` (et vaut initialement `Brest`)
    La constante `NB_VILLES` contient initialement la valeur `6`, ce qui signifie que seules les **6 premières villes** de la liste `villes` sont prises en compte.  
    Il s'agit des mêmes villes que dans [le cours](cours.md#probleme-du-voyageur-de-commerce).

    Sans rien changer au programme, **exécutez-le**, et vérifiez que vous obtenez bien les **mêmes résultats** que ceux que l'on avait indiqué dans [le cours](cours.md#resolution-par-force-brute).

!!! note "Exercice 2"
    Toujours dans le programme `voyageur_commerce_bf.py`, remplacez la valeur de `NB_VILLES` par `9`, et **exécutez** de nouveau le programme.  
    Quel est le **temps d'exécution** (en secondes) obtenu ?

    Même question avec `10` villes, `11` villes et éventuellement `12` villes (si c'est trop long, stoppez le programme.)

    Que peut-on dire de l'évolution **du temps d'exécution** à chaque ajout d'**une** ville ?

!!! note "Exercice 3"
    Ouvrez à présent le **programme** `voyageur_commerce_glouton.py`.

    Les **variables** et **constantes** sont les mêmes que dans le programme précédent.

    Ici, pour écrire plus facilement l'algorithme glouton de résolution du problème, on va préalablement créer un **dictionnaire des distances**, contenant à la fois les **noms des villes** et les **distances entre chaque ville**.  
    Il s'agira d'un **dictionnaire de dictionnaires**, sous la forme suivante (ici avec 6 villes) :

    ```python
    {'Brest': {'Brest': 0, 'Bordeaux': 598, 'Lille': 708, 'Lyon': 872, 'Marseille': 1130, 'Paris': 572}, 
    'Bordeaux': {'Brest': 598, 'Bordeaux': 0, 'Lille': 802, 'Lyon': 520, 'Marseille': 637, 'Paris': 554}, 
    'Lille': {'Brest': 708, 'Bordeaux': 802, 'Lille': 0, 'Lyon': 650, 'Marseille': 1002, 'Paris': 225}, 
    'Lyon': {'Brest': 872, 'Bordeaux': 520, 'Lille': 650, 'Lyon': 0, 'Marseille': 367, 'Paris': 465}, 
    'Marseille': {'Brest': 1130, 'Bordeaux': 637, 'Lille': 1002, 'Lyon': 367, 'Marseille': 0, 'Paris': 777}, 
    'Paris': {'Brest': 572, 'Bordeaux': 554, 'Lille': 225, 'Lyon': 465, 'Marseille': 777, 'Paris': 0}}
    ```

    Complétez la **fonction** `creer_dict` qui **crée ce dictionnaire**.

!!! note "Exercice 4"
    On souhaite maintenant écrire une fonction `trouver_ville_suivante(ville_actuelle, villes_restantes, dico_villes)`, qui sera utilisée par la fonction principale de résolution `voyageur`, et qui prend en entrée **une ville** (`ville_actuelle`), une **liste des villes non encore visitées** (`villes_restantes`) et le **dictionnaire des villes et distances** (`dico_villes`) telle que définie dans l'exercice précédent, et qui **renvoie** la **prochaine ville à visiter**, c'est-à-dire la ==**ville non visitée de plus petite distance avec la ville actuelle**==.

    Par exemple, si on appelle la fonction avec `"Lyon"` pour `ville_actuelle`, et `["Brest", "Bordeaux", "Lille", "Marseille", "Paris"]` pour `villes_restantes`, la fonctionn doit **renvoyer** `"Marseille"`.

    Écrivez cette **fonction** `trouver_ville_suivante`.

!!! note "Exercice 5"
    Enfin, on peut maintenant écrire la **fonction principale** `voyageur(dico_villes, ville_depart)`, qui résout le **problème du voyageur** avec la ==**méthode gloutonne**==.  
    Cette fonction prend le **dictionnaire des villes et distances** (`dico_villes`), et une **ville de départ** pour le trajet (`ville_depart`), et **renvoie** un **tuple de deux éléments** contenant **le trajet** (une *liste* de *noms de villes*) et la **distance** correspondante à ce trajet.

    Complétez la fonction à trous `voyageur`, puis **exécutez le programme** avec `VILLE_DEPART = "Lyon"` et `NB_VILLES = 6` pour vérifier si vous obtenez bien le **même résultat** que dans [le cours](cours.md#algorithme-glouton).

!!! note "Exercice 6"
    Toujours dans le programme `voyageur_commerce_glouton.py`, remplacez la valeur de `NB_VILLES` par `9`, et **exécutez** de nouveau le programme.  
    Quel est le **temps d'exécution** (en secondes) obtenu ?

    Même question avec `10` villes, `11` villes et `12` villes.

    Que peut-on dire de l'évolution **du temps d'exécution** à chaque ajout d'**une seule** ville, en comparaison avec la **résolution par force brute** ?

!!! note "Exercice 7"
    En utilisant l'**algorithme de force brute**, déterminez le **meilleur trajet** en partant de *Marseille* pour parcourir *10 villes*.

    1. Quel est le résultat (**trajet** et **distance totale parcourue**) obtenu ?  
    (Vous indiquerez l'*une* des *deux solutions* affichées.)
    2. L'algorithme de **résolution gloutonne** de ce problème donne t-il ici la **meilleure solution** ?
    3. Peut-on déterminer, de manière certaine, le meilleur trajet pour parcourir **les 14 villes** en partant de *Marseille* ? Pourquoi ?