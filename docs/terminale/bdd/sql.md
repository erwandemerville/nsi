# Le langage SQL

## Introduction

Le **modèle relationnel** introduit est un **modèle mathématique** permettant de raisonner sur des **données tabulées**. Il est mis en œuvre par un **logiciel** particulier, le **système de gestion de bases de données** (**SGBD** en abrégé).

Un **SGBD relationnel** est un **SGBD** utilisant le **modèle relationnel** pour la **représentation des données**. L'écrasante majorité des **SGBD relationnels** utilisent le **langage SQL** (*Structured Query Language*, langage de requête structuré).

Ce dernier permet d'envoyer des **ordres** au **SGDB**. Les **ordres** peuvent être de **deux natures** :

- les **mises à jour** permettant la **création** de **relations**,
- l'ajout d'**entités** dans ces **dernières**, leur **modification** et leur **suppression**,
- les **requêtes** permettent de **récupérer les données** répondant à des **critères particuliers**.

Présenter de façon **intuitive** le **langage SQL** et les **SGBD**, tout en restant dans le cadre du programme de terminale, est une tâche complexe. En effet, on ne peut comprendre certains aspects du langage sans connaître un peu le fonctionnement des **SGBD** et à l'inverse le fonctionnement et les limites des **SGBD** ne sont explicables qu'avec une certaine pratique de la **manipulation de données**.

## SQL: un langage de définition de données

Directement inspiré du **modèle relationnel** introduit par Edgar Frank Codd (considéré comme l'**inventeur** du **modèle relationnel** et des **SGBD relationnels**), le **langage SQL** permet la **définition de relations** (ou **tables**) dans une **base de données relationnelle**. Ce langage est standardisé par l'**ISO** (*Organisation internationale de normalisation*), sous la référence *ISO / IEC 9075*. La dernière version du standard date de **2016**.

Le **langage SQL** permet de **créer des tables** en spécifiant leur **nom**, leurs **attributs**, les **types** de ces derniers et les **contraintes** associées à la table. 