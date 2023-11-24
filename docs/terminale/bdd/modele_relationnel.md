??? quote "Sources"
    - [lecluse.fr](https://www.lecluse.fr/nsi/NSI_T/bdd/modrel/){ target="_blank" }
    - [lyceum.fr](https://www.lyceum.fr/tg/nsi/2-bases-de-donnees/1-les-bases-de-donnees-relationnelles/){ target="_blank" }

# Le modèle relationnel

Un **modèle de données** est une **représentation** (*mathématique* ou *informatique*) de **concepts** que l'on souhaite étudier. Un **modèle** permet d'**énoncer des propriétés** de ces **données** en termes **logiques**, mais aussi de **programmer** des processus réels complexes sous forme d'**opérations élémentaires** sur les **données**.

Il existe différents **modèles de bases de données** :

- les **bases données relationnelles** utilisant des **tableaux de données organisées** en **lignes** et **colonnes** auxquelles on accède grâce au langage **SQL**,
- les **bases de données non relationnelles** dites *noSQL* qui peuvent stocker des données de formes diverses comme des graphes, des documents…

Nous nous intéresserons cette année uniquement au **modèle relationnel**.

Dans ce **modèle**, un **objet modélisé** (on parle d'**entité**) est représenté par un **n-uplet** de **valeurs** et les **collections d'objets** (les **tables** de données) par des **ensembles de n-uplets** appelés <u>**relations**</u>.

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

## Un exemple pratique

Voici une **table de données** sur plusieurs **livres** :

| titre                   | nom_auteur  | prenom_auteur | date_nai_auteur | langue  | année_publication | thèmes                                           |
|-------------------------|-------------|---------------|------------------|---------|-----------|--------------------------------------------------|
| 1984                    | Orwell      | George        | 1903             | anglais | 1949      | Totalitarisme, science-fiction, anticipation, Dystopie |
| Dune                    | Herbert     | Frank         | 1920             | anglais | 1965      | science-fiction, anticipation                    |
| Fondation               | Asimov      | Isaac         | 1920             | anglais | 1951      | science-fiction, Economie                         |
| Le meilleur des mondes | Huxley      | Aldous        | 1894             | anglais | 1931      | Totalitarisme, science fiction, dystopie          |
| Fahrenheit 451          | Bradbury    | Ray           | 1920             | anglais | 1953      | science-fiction, Dystopie                         |
| Ubik                    | K. Dick     | Philip        | 1928             | anglais | 1969      | science-fiction, anticipation                    |
| Chroniques martiennes   | Bradbury    | Rey           | 1920             | anglais | 1950      | science-fiction, anticipation                    |
| La nuit des temps       | Barjavel    | René          | 1911             | français| 1968      | science-fiction, tragédie                        |
| Blade runner            | K Dick      | Philip        | 1928             | anglais | 1968      | Intelligence artificielle, science fiction       |
| Les robots              | Asimov      | Isaac         | 1920             | anglais | 1950      | science fiction, Intelligence artificielle        |
| La planète des singes   | Boulle      | Pierre        | 1912             | français| 1963      | science fiction, Dystopie                         |
| Ravage                  | Barjavel    | René          | 1911             | français| 1943      | Science-Fiction, anticipation                    |
| Le maître du haut chateau| K.Dick     | Philip        | 1928             | anglais | 1962      | Dystopie, Uchronie                               |
| Le monde des A          | Van Vogt    | Alfred Elton  | 1912             | anglais | 1945      | science fiction, IA                              |
| La fin de l'éternité    | Asimov      | Isaac         | 1920             | anglais | 1955      | science-fiction, voyage dans le temps             |
| De la Terre à la Lune   | Verne       | Jules         | 1828             | français| 1865      | Science-Fiction, aventure                         |

On rappelle les quelques **éléments de vocabulaire** suivants :

!!! note ""
    - un **enregistrement** est composé de plusieurs informations distinctes appartenant à un même **objet** ou une même **entité**. Cela correspond à une **ligne** du tableau.
    - un **attribut** est une information élémentaire appartenant à un **enregistrement**. Les **attributs** sont visibles sur les **intitulés de colonne**. Un **attribut atomique** est un **attribut** ne contenant qu'**une seule information**.
    - Chaque **attribut** possède un **type** et un **domaine**, il s'agit de l'**ensemble** (fini ou infini) de **valeurs admissibles**. Par exemple, *année_publication* serait du **type** *Int* et les valeurs permises seraient par exemple comprises entre `1800` et `2023`.

!!! note "Exercice 1"
    1. Combien notre table possède t-elle d'**enregistrements** ?
    2. Quels sont tous les **attributs** de la table ?
    3. Citez un **attribut atomique** et un attribut non atomique.
    4. Pour chaque attribut, précisez le **type** et le **domaine**.

!!! note "Exercice 2"
   Quels éléments de la table sont en contradiction avec les **principes du modèle relationnel** énoncés ci-dessus ?
   
   Redistribuer les données dans **4 tables différentes**, en donnant leur *schéma relationnel*.