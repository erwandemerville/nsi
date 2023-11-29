??? quote "Sources"
    - [lecluse.fr](https://www.lecluse.fr/nsi/NSI_T/bdd/modrel/){ target="_blank" }
    - [lyceum.fr](https://www.lyceum.fr/tg/nsi/2-bases-de-donnees/1-les-bases-de-donnees-relationnelles/){ target="_blank" }
    - "Spécialité Numérique et sciences informatiques : 24 leçons avec exercices corrigés - Terminale" de *Thibaut Balabonski*

# Le modèle relationnel

La **théorie** et la **pratique** des **bases de données relationnelles** est un domaine de recherche **toujours actif**, mais qui s'est fortement développé et complexifié depuis ses débuts dans les années *1970*.

!!! abstract "Modèle de données"
    Un **modèle de données** est une **représentation** (*mathématique* ou *informatique*) de **concepts** que l'on souhaite étudier. Un **modèle** permet d'**énoncer des propriétés** de ces **données** en termes **logiques**, mais aussi de **programmer** des processus réels complexes sous forme d'**opérations élémentaires** sur les **données**.

    Il existe différents **modèles de bases de données** :

    - les **bases de données relationnelles** utilisant des **tableaux de données organisées** en **lignes** et **colonnes** auxquelles on accède grâce au langage de requête structuré **SQL**, qui permet de **manipuler** une **base de données** de façon **interactive**,
    - les **bases de données non relationnelles** dites *noSQL* qui peuvent stocker des données de formes diverses comme des *graphes*, des *documents*…

Nous nous intéresserons cette année uniquement au **modèle relationnel**.

Dans ce **modèle**, un **objet modélisé** (on parle d'**entité**) est représenté par un **n-uplet** de **valeurs** et les **collections d'objets** (les **tables** de données) par des **ensembles de n-uplets** appelés <u>**relations**</u>.

!!! warning "Modèle de données vs. structure de données"
    Il faut bien distinguer le **modèle de données** de la **structure de données**, qui se placent à différents niveaux d'*abstraction*.

    Le modèle indique quelles **caractéristiques** d'une **entité** réelle on souhaite manipuler dans un programme ainsi que les **relations entre les entités**.

    Une **structure de données** indique comment les données vont être **organisées en machine** (dans un langage de programmation). On peut, pour un même modèle de données, choisir **plusieurs structures de données** différentes.

## Présentation

!!! abstract "Les principes de base"
    Les **principes de base** du **modèle relationnel** sont les suivants :

    - séparer les données dans **plusieurs tables** :
        - chaque **table** contient des **données relatives à un même sujet**,
        - éviter la **redondance des données**,
        - ne pas **stocker** des données qui peuvent être **calculées** (exemple : une ligne `Total`),
        - chaque champ ne contient qu'**une seule information**,
    - mettre les **tables en relation** par l'utilisation de **clés** :
        - **<u>clés primaires</u>** : leurs valeurs (souvent des entiers) permettent d'**identifier** une **donnée** de **manière unique**,
        - **<u>clés étrangères</u>** : **référencent** une **clé primaire d'une autre table**.

!!! note "Éléments de vocabulaire"
    - un **enregistrement** est composé de plusieurs informations distinctes appartenant à un même **objet** ou une même **entité**. Cela correspond à une **ligne** du tableau.
    - un **attribut** est une information élémentaire appartenant à un **enregistrement**. Les **attributs** sont visibles sur les **intitulés de colonne**. Un **attribut atomique** est un **attribut** ne contenant qu'**une seule information**.
    - Chaque **attribut** possède un **type** (*Int*, *String*, *Date*, etc.) et un **domaine** (il s'agit de l'**ensemble**, fini ou infini, de **valeurs admissibles**). Par exemple, *année_publication* serait du **type** *Int* et ses valeurs permises (son **domaine**) seraient par exemple comprises entre `1800` et `2023`.

!!! success "Modéliser des données"
    La **modélisation des données** se décompose en **plusieurs étapes**:
    
    1. déterminer les *entités* (objets, actions, personnes, etc.) que l'on souhaite **manipuler**;
    2. modéliser les *ensembles d'entités* comme des **relations** en donnant leur **schéma**, en s'attachant en particulier à choisir le **bon domaine** pour **chaque attribut**;
    3. définir les *contraintes* de la **base de données**, c'est-à-dire l'**ensemble** des **propriétés logiques** que nos **données** doivent **vérifier à tout moment** (voir la partie [contraintes d'intégrité](#les-contraintes-dintégrité).)

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

!!! note "Exercice 1"
    1. Combien notre table possède t-elle d'**enregistrements** ?
    2. Quels sont tous les **attributs** de la table ?
    3. Citez un **attribut atomique** et un attribut non atomique.
    4. Pour chaque attribut, précisez le **type** et le **domaine**.

!!! note "Exercice 2"
    Quels éléments de la table sont en contradiction avec les **principes du modèle relationnel** énoncés ci-dessus ?
   
    Redistribuer les données dans **4 tables différentes**, en donnant leur *schéma relationnel*.

??? tip "Correction possible exercice 2"
    Voici une possibilité de **modélisation** de cette **base de données**, ici sous la forme d'un **diagramme** :

    ```mermaid
    erDiagram
        LIVRES ||--o{ AUTEURS : "Auteur_ID"
        LIVRES ||--o{ LANGUES : "Langue_ID"
        LIVRES {
            INT ID_Livre
            STR Titre
            INT Annee_Publication
            INT Langue_ID
            INT Auteur_ID
        }

        AUTEURS {
            INT ID_Auteur
            STR Nom
            STR Prenom
            DATE Date_Naissance
        }

        THEMES {
            INT ID_Theme
            STR Nom
        }

        LANGUES {
            INT ID_Langue
            STR Nom
        }

        LIVRES_Themes ||--o{ LIVRES : "ID_Livre"
        LIVRES_Themes ||--o{ THEMES : "ID_Theme"
        LIVRES_Themes {
            INT ID_Livre
            INT ID_Theme
        }
    ```

    Et voici le **schéma relationnel** correspondant :

    - *Livres*(<u>*ID_Livre* Int</u>, *Titre* String, *Annee_Publication* Int, #*Langue_ID* Int, #*Auteur_ID* Int)
    - *Auteurs*(<u>*ID_Auteur* Int</u>, *Nom* String, *Prenom* String, *Date_Naissance* Date)
    - *Themes*(<u>*ID_Theme* Int</u>, *Nom* String)
    - *Langues*(<u>*ID_Langue* Int</u>, *Nom* String)
    - *Livres_Themes*(<u>#*ID_Livre* Int, #*ID_Theme* Int</u>)

!!! warning ""
    On peut **modéliser** une **base de données** sous la forme d'un **diagramme** ou d'un **schéma relationnel** (voir le bloc de *correction* ci-dessus).  
    Dans le cadre du *programme de terminale*, vous devez surtout retenir la façon dont on crée un **schéma relationnel**.

## Les contraintes d'intégrité

La **cohérence des données** au sein d'une **base de données** est assurée par des <u>**contraintes d'intégrité**</u>.

Ces dernières sont des **invariants**, c'est-à-dire des **propriétés logiques que les données doivent vérifier à tout moment**. 

!!! abstract "Contraintes d'intégrité"
    Voici les différentes ==**contraintes d'intégrité**== à distinguer :

    - Les ==**contraintes d'entité**== qui garantissent que chaque **entité** d'une **relation** est **unique**. Une **clé primaire** est un **attribut** ou un **ensemble d'attributs** qui identifie **chaque entité** de la **relation** de manière **unique** et garantit la **contrainte d'entité**. Par exemple, dans une table "Employés", la contrainte d'entité pourrait s'appliquer à la colonne "ID_Employé", assurant ainsi l'unicité de chaque identifiant d'employé.
    - Les ==**contraintes de référence**== qui créent des **associations** entre **deux relations**. Elle permettent de garantir qu'une **entité** d'une **relation B** mentionne une **entité existante** dans une **relation A**. Les contraintes de référence sont utilisées pour maintenir la **cohérence** entre les **tables** en **utilisant une clé étrangère**, c'est-à-dire un **attribut** ou **ensemble d'attributs** d'une **table** qui est une **clé primaire dans une autre table**. Par exemple, imaginons une table "Commandes" avec une clé étrangère "ID_Client" faisant référence à la clé primaire "ID_Client" dans la table "Clients"
    - Les ==**contraintes de domaines**== qui restreignent les valeurs d'un **attribut** à celles du **domaine** et évitent que l'on puisse donner à un **attribut** une **valeur illégale**. Par exemple, une colonne "Âge" dans une table "Clients" pourrait avoir une **contrainte de domaine** limitant les **valeurs** à des **entiers positifs** compris entre `18` et `100`.
    - Les ==**contraintes utilisateurs**== permettent de définir toutes autres **règles personnalisées** pour assurer l'**intégrité des données** en fonction des **besoins spécifiques d'une application**. Par exemple, une **contrainte utilisateur** pourrait être définie pour s'assurer que le *stock* d'un *produit* ne devienne jamais **négatif** dans une table "Produits". Ces **contraintes** permettent de s'assurer que les **données** sont « conformes » aux **entités du monde réel** qu'elles **représentent**.

    Toutes ces **contraintes** garantissent la **cohérence**, la **fiabilité** et la **validité** des **données stockées dans la base de données**.

## Exercices

Voici quelques **exercices** supplémentaires pour vous entraîner là-dessus :

!!! note "Exercice 3"
    On souhaite modéliser un **annuaire téléphonique simple** dans lequel **chaque personne** (identifiée par son *nom* et son *prénom*) est associée à son **numéro de téléphone**. Proposer une **modélisation relationnelle** de cet annuaire. 

!!! note "Exercice 4"
    Donner la **modélisation relationnelle** d'un bulletin scolaire.Cette dernière doit permettre de mentionner :
    
    - des **élèves**, possédants un **numéro d'étudiant alphanumérique unique**,
    - un **ensemble** de **matières fixées**, mais qui ne sont pas données,
    - au plus une **note sur 20**, par **matière** et par **élève**.

    On prendra soin de préciser **toutes les contraintes utilisateurs** qui ne peuvent êtres inscrites dans les **schémas des relations**.

!!! note "Exercice 5"
    Proposer une **modélisation** pour un **réseau de bus**. Cette dernière doit être **suffisamment riche** pour permettre de générer, pour chaque arrêt de bus du réseau, une **fiche horaire** avec **tous** les **horaires de passage** de **toutes les lignes de bus** qui desservent **l'arrêt**.
    
    <u>Indication</u> : ici, plus qu'une simple traduction du français vers le modèle relationnel, on essayera de déterminer dans un premier temps quelles informations sont pertinentes et comment les représenter. On pourra ensuite procéder à la modélisation sous forme de relations. 