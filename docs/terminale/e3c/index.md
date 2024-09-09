# Corrigé sujet 6 e3c

!!! success "Sujet"
    <center style="font-size:1.3em">
    [Télécharger le sujet](src/sujet6.pdf)
    </center>

!!! quote "Source de la correction"
    Ce corrigé est proposé par *@Messieu_Rayan* du *Collège-Lycée La Jonchère*.  
    [Cliquez ici](src/sujet6_correction.pdf) pour consulter le PDF d'origine.

## Thème A : Types de Base

!!! tip "Question A1"
    Réponse **D**.

    **Justification** : La représentation binaire de $-126$ en **complément à deux** sur 8 bits est `10010010`, qui est l'inverse du nombre `01101101` ($65$ en décimal) plus $1$.

!!! tip "Question A2"
    Réponse **D**.

    **Justification** : L'expression `True or (True and False)` renvoie `True`, car l'opérateur `or` renvoie `True` si l'une des opérandes est `True`.

!!! tip "Question A3"
    Réponse **B**.

    **Justification** : Le codage en **complément à 2** est utilisé pour **représenter des nombres entiers négatifs en binaire**.


!!! tip "Question A4"
    Réponse **B**.

    **Justification** : L'opération $(a^b) = (2^3)$ donne $8$, et $(8%3)$ (le reste de la division de $8$ par $3$) donne $2$. Donc, la valeur de `d` est $2$.

!!! tip "Question A5"
    Réponse **C**.

    **Justification** : **"Arial"** est un nom de police de caractères, pas une méthode d'encodage des caractères. Les autres options (*UTF-16*, *ASCII*, *Unicode*) sont des méthodes d'encodage.

!!! tip "Question A6"
    Réponse **A**.

    **Justification** : L'expression `x == 3 or y == 5` renvoie `True`, car `x` est égal à $3$ même si `y` n'est pas égal à $5$.

## Thème B : Types Construits

!!! tip "Question B1"
    Réponse **A**.

    **Justification** : La fonction **renvoie** le maximum de la liste `L`, car elle parcourt `L` et met à jour `m` chaque fois qu'elle trouve un élément supérieur à `m`.

!!! tip "Question B2"
    Réponse **C**.

    **Justification** : `u` contiendra `[6, 8, 21]` car il s'agit des éléments de `t` qui sont supérieurs à `3`.

!!! tip "Question B3"
    Réponse **C**.

    **Justification** : `V` ne prend que les multiples de `3`

!!! tip "Question B4"
    Réponse **B**.

    **Justification** : L'expression `T[2][1]` évalue à `8`, car elle accède au **deuxième élément** (indice `1`) du **troisième sous-tableau** (indice `2`) de `T`.

!!! tip "Question B5"
    Réponse **D**.

    **Justification** : `r` vaudra `6` car il s'agit de la différence entre le **quatrième** et le **deuxième élément** du tuple `t`.

!!! tip "Question B6"
    Réponse **D**.

    **Justification** : `d['z']` récupère la valeur associée à la clé 'z' dans le dictionnaire `d`, qui est `26`.

## Thème C : Traitement de Données en Tables

!!! tip "Question C1"
    Réponse **C**.

    **Justification** : La fonction **renvoie** le **nom** de la **première personne** dont l'**âge** est **supérieur à 18** dans le dictionnaire, qui est `"charlotte"`.

!!! tip "Question C2"
    Réponse **A**.

    **Justification** : La réponse **A** est le **format correct** d'un fichier **CSV**, où les valeurs sont **séparées par des virgules**.

!!! tip "Question C3"
    Réponse **B**.

    **Justification** : L'expression `t[1]['quantité']` permet d'accéder à la **quantité de scies**, qui est le **deuxième élément** de la liste `t`.

!!! tip "Question C4"
    Réponse **B**.

    **Justification** : `mendeleiev[1][6] = 'F'` corrige le symbole du **Fluor** dans le tableau périodique.

!!! tip "Question C5"
    Réponse **A**.

    **Justification** : L'instruction `data = data1 + data2` crée une **nouvelle table** en combinant les éléments de `data1` et `data2`.

!!! tip "Question C6"
    Réponse **C**.

    **Justification** : L'expression `c = a + b` combine les deux listes `a` et `b`, donnant `[1, 2, 3, 4, 5, 6]`.

## Thème D : Interactions entre l'homme et la machine sur le Web.

!!! tip "Question D1"
    Réponse D.

    Justification : La méthode POST du protocole HTTP est utilisée pour envoyer des données, comme celles d'un formulaire HTML, vers un serveur.

!!! tip "Question D2"
    Réponse B.

    Justification : La balise <title> est utilisée dans l'en-tête d'un document HTML pour définir le titre de la page.

!!! tip "Question D3"
    Réponse D.

    Justification : L'attribut onmouseover en HTML est utilisé pour exécuter un script lorsqu'un utilisateur passe la souris sur un élément spécifique.

!!! tip "Question D4"
    Réponse C.

    Justification : La balise <input type="checkbox"> est utilisée pour créer des cases à cocher dans un formulaire HTML.

!!! tip "Question D5"
    Réponse C.

    Justification : La propriété onclick d'une balise <button /> en HTML est utilisée pour définir un script JavaScript à exécuter lors du clic sur le bouton.

!!! tip "Question D6"
    Réponse C.

    Justification : Le sélecteur CSS #tab-nav a cible les liens (<a>) à l'intérieur de l'élément avec l'ID tab-nav, ce qui correspond à la structure donnée pour la barre de navigation.

## Thème E : Architectures Matérielles et Systèmes d'Exploitation Question E1.

!!! tip "Question E1"
    Réponse C.

    Justification : La commande chmod a+x jeu sous Linux donne les droits d'exécution à tous les utilisateurs pour le fichier jeu.

!!! tip "Question E2"
    Réponse C.

    Justification : La commande cp /users/luc/interro.txt ./ sous Linux copie le fichier interro.txt vers le répertoire courant.

!!! tip "Question E3"
    Réponse C.

    Justification : Après les commandes, les fichiers help.txt et tutorial.txt seront dans le répertoire Documents du répertoire de l'utilisateur.

!!! tip "Question E4"
    Réponse C.

    Justification : La commande cat readme.txt sous Linux est utilisée pour afficher le contenu du fichier readme.txt.

!!! tip "Question E5"
    Réponse C.

    Justification : Dans l'architecture de Von Neumann, l'unité arithmétique et logique (UAL) a pour rôle d'effectuer les opérations de base.

!!! tip "Question E6"
    Réponse D.

    Justification : L'affirmation selon laquelle un système d'exploitation propriétaire est plus sécurisé est subjective et ne peut être établie comme universellement vraie.

## Thème F : Langages et Programmation Question F1.

!!! tip "Question F1"
    Réponse D.

    Justification : L'instruction (random.randint(0, 4) - 2) * 2 génère un entier aléatoire entre 0 et 4, soustrait 2, puis multiplie le résultat par 2, couvrant l'ensemble {-4, -2, 0, 2, 4}.

!!! tip "Question F2"
    Réponse B 

    Justification : Le test ranger(3, 4, 1) échoue à trier correctement car il permute le 4 et le 1 mais laisse le 3 devant

!!! tip "Question F3"
    Réponse D.

    Justification : L'expression [1 * 7] crée une liste contenant 7 fois le nombre 1, donc [7, 7, 7, 7, 7, 7, 7].

!!! tip "Question F4"
    Réponse C.

    Justification : Les conditions a <= b < longueur(T) garantissent que les indices sont dans les limites correctes du tableau sans chevauchement.

!!! tip "Question F5"
    Réponse B.

    Justification : Remplacer les pointillés par L[i] > m garantit que m sera mis à jour avec le plus grand élément rencontré dans la liste. Question F6.

!!! tip "Question F6"
    Réponse C.

    Justification : Il est déconseillé d'utiliser des flottants avec cette fonction car la précision des opérations flottantes peut entraîner des erreurs inattendues dans la comparaison.

## Thème G : Algorithmique Question G1.

!!! tip "Question G1"
    Réponse A.

    Justification : Pour la recherche dichotomique, la liste doit être triée pour permettre la division de la liste et la comparaison des éléments de manière efficace.

!!! tip "Question G2"
    Réponse D.

    Justification : Dans le pire des cas, un algorithme de recherche dichotomique sur une liste de taille 2 nécessite 2 + 1 = 3 comparaisons.

!!! tip "Question G3"
    Réponse D.

    Justification : La fonction retourne le maximum de la liste donnée.

!!! tip "Question G4"
    Réponse B.

    Justification : La fonction compte le nombre d'occurrences de la lettre 'e' dans "Vive l’informatique", qui apparaît 2 fois.

!!! tip "Question G5"
    Réponse C.

    Justification : Cette fonction implémente la recherche dichotomique, un algorithme de recherche qui divise successivement la liste pour trouver un élément.

!!! tip "Question G6"
    Réponse B.

    Justification : Le script B boucle indéfiniment car i commence plus petit que K et diminue à chaque fois, mais la condition de la boucle est que i soit plus petit que K ce qui est toujours vrai.