# Cours - Algorithme des $k$ plus proches voisins

??? quote "Sources / Liens utiles"
    - [monlyceenumerique.fr](http://www.monlyceenumerique.fr/nsi_premiere/algo_a/a4_algo_knn.php)

## Introduction

L'**algorithme** des $k$ **plus proches voisins** (*k-NN*, de l'anglais **k-nearest neighbors**) est une **méthode d'apprentissage automatique supervisé** qui **classe** un *élément* en fonction de la **catégorie prédominante** parmi ses **voisins les plus proches** dans l'**ensemble d'entraînement**.

Son principe peut se résumer par l'expression : *Dis-moi qui sont tes amis et je te dirai qui tu es*.

## Un premier exemple

!!! quote ""
    *Source de cet exemple : [monlyceenumerique](http://www.monlyceenumerique.fr/nsi_premiere/algo_a/a4_algo_knn.php#1.1)*

!!! abstract ""
    Dans cette introduction, nous considérons un ensemble de données structuré de la manière suivante :

    - Les données sont réparties en deux catégories : le type 1 et le type 2.
    - Les données possèdent deux caractéristiques : caractéristique 1 et caractéristique 2.

    Imaginons la situation suivante dans un jeu :

    - Vous avez deux types de personnages : les fantassins (type 1 : 'fantassin') et les chevaliers (type 2 : 'chevalier').
    - Vous avez deux types de caractéristiques : la force (caractéristique 1 : valeur entre 0 et 20) et le courage (caractéristique 2 : valeur entre 0 et 20).
    - Vous disposez d'une collection de personnages dont les caractéristiques et le type sont connus.

    Vous introduisez un nouveau personnage dont le type est inconnu, mais dont vous connaissez les caractéristiques. L'objectif de l'algorithme kNN (k Nearest Neighbors = k plus proches voisins en français) est de déterminer le type de ce nouveau personnage.