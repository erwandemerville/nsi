# Exercices - Arbres binaires de recherche

Voici 3 **arbres binaires** :

![exo_abr_comparer.png](images/exo_abr_comparer.png)

!!! note "Exercice 1"
    
    1. Parmi ces arbres, pouvez-vous dire lesquels sont des arbres binaires *de recherche* ?
    2. Dans un **arbre binaire de recherche**, où se trouve le **plus petit élément** ? Le **plus grand élément** ?
    3. Quelle est l'ordre des *noeuds* lors des parcours *préfixe*, *infixe*, *postfixe* du premier arbre ?
    4. Quel parcours est particulièrement intéressant avec les arbres binaire *de recherche* ? Pourquoi ?
    5. Comment vérifier facilement si un **arbre binaire** est un **arbre binaire de recherche** ?

!!! note "Exercice 2"
    Créez un **arbre binaire de recherche** en partant d'un **arbre binaire vide** et en  **insérant progressivement** les **nœuds de valeurs suivantes** (en suivant cet ordre) : **18, 13, 21, 20, 15, 10, 23**.

!!! note "Exercice 3"
    Dessinez un **arbre binaire de recherche** :

    1. En **insérant**, en suivant l'ordre, les nœuds de valeurs suivantes dans l'arbre : **14,13,12,11,8,5,4,3,1**<br />
    Que constatez-vous ? À quelle autre **structure de données** cet arbre s'apparente t-il ?
    2. Re-dessinez cet arbre de manière à obtenir un arbre **équilibré**.
    3. Si on **insère progressivement** chaque valeur une par une dans l'arbre, dans quel ordre faut-il les ajouter pour obtenir un arbre équilibré ? Décrivez votre méthode.

!!! note "Exercice 4"
    1. Décrivez, en **pseudo-langage**, un algorithme **récursif** de **recherche** dans un **arbre binaire de recherche**, qui renvoie `Vrai` si un **élément fourni en entrée** est **présent** dans l'arbre, et `Faux` s'il ne l'est pas.
    2. Dessinez **deux arbres binaires de recherche**, construits en partant d'un arbre vide et en insérant progressivement les **nœuds suivants** :
        * **20, 15, 22, 18, 21, 16, 23, 13**
        * **13, 15, 16, 18, 20, 21, 22, 23**
  
    3. Que pouvez-vous dire du premier arbre ? Du second ?
    4. Déroulez votre algorithme sur **les deux arbres précédemment dessinés**, puis **comptez le nombre d'appels récursifs** pour rechercher :
        * la valeur **17** dans le premier arbre
        * la valeur **25** dans le deuxième arbre
  
    5. Choisissez ainsi le bon **coût algorithmique** dans le tableau ci-dessous **dans le pire cas** :

    |                  | **O(1)** | **O($log_2{n}$)** | **O(n)** | **O($nlog_2{n}$)** | **O(n²)** |
    | ---------------- | -------- | ----------------- | -------- | ------------------ | --------- |
    | ABR **équilibré** |          |                   |          |                    |           |
    | ABR **non équilibré** |        |                   |          |                    |           |

!!! note "Exercice 5"
    1. Décrivez, en **pseudo-langage**, un algorithme **récursif** d'**insertion** dans un **arbre binaire de recherche** qui **renvoie un nouvel arbre** dans lequel est ajouté **un nœud dont la valeur est donnée en entrée**.
    2. Déroulez votre algorithme sur **les deux arbres dessinés** à la *question précédente*, puis, pour chacun, **comptez le nombre d'appels récursifs** effectués pour insérer :
        * la valeur **17** dans le premier arbre
        * la valeur **25** dans le deuxième arbre

    3. Choisissez ainsi le bon **coût algorithmique** dans le tableau ci-dessous **dans le pire cas** :
    
    |                  | **O(1)** | **O($log_2{n}$)** | **O(n)** | **O($nlog_2{n}$)** | **O(n²)** |
    | ---------------- | -------- | ----------------- | -------- | ------------------ | --------- |
    | ABR **équilibré** |          |                   |          |                    |           |
    | ABR **non équilibré** |        |                   |          |                    |           |
