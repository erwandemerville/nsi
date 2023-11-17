??? quote "Sources"
    - [lecluse.fr](https://www.lecluse.fr/nsi/NSI_T/bdd/modrel/){ target="_blank" }
    - [lyceum.fr](https://www.lyceum.fr/tg/nsi/2-bases-de-donnees/1-les-bases-de-donnees-relationnelles/){ target="_blank" }

# Le modèle relationnel

Un **modèle de données** est une **représentation** (*mathématique* ou *informatique*) de **concepts** que l'on souhaite étudier. Un **modèle** permet d'**énoncer des propriétés** de ces **données** en termes **logiques**, mais aussi de **programmer** des processus réels complexes sous forme d'**opérations élémentaires** sur les **données**.

Il existe différents **modèles de bases de données** :

- les **bases données relationnelles** utilisant des **tableaux de données organisées** en **lignes** et **colonnes** auxquelles on accède grâce au langage **SQL**,
- les **bases de données non relationnelles** dites *noSQL* qui peuvent stocker des données de formes diverses comme des graphes, des documents…

Nous nous intéresserons cette année uniquement au **modèle relationnel**.

Dans ce **modèle**, un **objet modélisé** (on parle d'**entité**) est représenté par un **n-uplet** de **valeurs** et les **collections d'objets** par des **ensembles de n-uplets** appelés <u>**relations**</u>. 

!!! warning "Modèle de données vs. structure de données"
    Il faut bien distinguer le **modèle de données** de la **structure de données**, qui se placent à différents niveaux d'*abstraction*.

    Le modèle indique quelles **caractéristiques** d'une **entité** réelle on souhaite manipuler dans un programme ainsi que les **relations entre les entités**.

    Une **structure de données** indique comment les données vont être **organisées en machine** (dans un langage de programmation). On peut, pour un même modèle de données, choisir **plusieurs structures de données** différentes.

## Présentation

Les **principes de base** du **modèle relationnel** sont les suivants :

- séparer les données dans **plusieurs tables** :
    - chaque table contient des données relatives à un même sujet,
    - éviter la redondance des données,
    - ne pas stocker des données qui peuvent être calculées (exemple : une ligne Total),
    - chaque champ ne contient qu'**une seule information**,
- mettre les **tables en relation** par l'utilisation de **clés** :
    - **<u>clés primaires</u>** : leurs valeurs (souvent des entiers) permettent d'identifier une donnée de **manière unique**,
    - **<u>clés étrangères</u>** : référencent une clé primaire d'une autre table.
