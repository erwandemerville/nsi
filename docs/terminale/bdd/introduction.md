??? quote "Sources"
    - [lecluse.fr](https://www.lecluse.fr/nsi/NSI_T/bdd/intro/){ target="_blank" }

# Introduction aux bases de données

Le **développement des traitements informatiques** nécessite une **manipulation de données** de plus en plus **nombreuses**. L'**organisation** et le **stockage** de ces **données** constitue un **enjeu essentiel** en termes de performance.

!!! note "Vocabulaire"
    <u>**Donnée**</u> : Une **donnée** est une **représentation informatique** d’une **information**.

    <u>**Bases de données**</u> : Les **bases de données** sont des **ensembles** de **données stockées et organisées** pouvant servir à un ou plusieurs programmes.

L'année dernière, vous avez étudié une manière de **stocker** et **manipuler** des **données structurées** à l'aide de différents formats, comme le format **CSV**. Ces formats sont essentiellement basés sur du **texte** et sont faciles à mettre en oeuvre et à utiliser, mais ne sont pas adaptés au traitement d'un **grand nombre** d'**informations**, en particulier lorsque celles-ci sont réparties dans **plusieurs tables** ou **fichiers**.

!!! quote ""
    Par exemple, une *compagnie aérienne* gérant l'**organisation des vols** ainsi que les **réservations** et l'**exploitation des avions** pourrait difficilement gérer toutes ces **informations** avec des fichiers **CSV**.

Les premières **bases de données** sont apparues dans les années **1960** et se sont développées en même temps que l'informatique. Par la suite est apparu le **langage SQL**, dans les années **1980**, permettant d'**interagir avec les bases de données** (en exécutant des **requêtes** de *sélection*, de *filtrage*, de *mise à jour* sur les **systèmes de bases de données**).

Les **bases de données** sont **omniprésentes** aujourd'hui, notamment sur le **web**. La plupart des sites, comme par exemple les *sites de commerce en ligne*, les utilisent.

## Gestion efficace des données

Dans une **base de données**, l'information est **stockée dans des fichiers**, qui ne sont généralement **pas lisibles** par un être humain : ils nécessitent l'utilisation d'un **système de base de données** (**SGBD**) pour les exploiter. Ces **SGBD** permettent de :

- **lire**, **écrire**, **modifier**, **effacer**, **mettre en relation des données** de différentes **tables**,
- **gérer les utilisateurs** ayant accès aux **données**,
- **gérer les droits d'accès** aux différentes **données**,
- d'**assurer** la **sécurité** et l'**intégrité** des **données**, et la **gestion des accès concurrents** (c'est-à-dire lorsque **plusieurs utilisateurs** accèdent **simultanément** aux **mêmes données**).

Parmis les **logiciels de gestion de bases de données** les plus courants, on retrouve :

- des **logiciels libres** :
    - mariaDB / mySQL / SQLite (que nous utiliserons)
    - postgreSQL
- des **logiciels propriétaires** :
    - IBM DB2
    - Oracle Database
    - Microsoft SQL Server.

Ces logiciels fonctionnent en mode **client/serveur** et sont conçus pour gérer plusieurs **millions**, voire **milliards** d'**enregistrement** de manière **fiable** et **sécurisée**. Leur architecture côté serveur est prévue pour êre répartie sur **plusieurs machines** et ainsi permettre une **tenue en charge** lorsqu'un grand nombre de requêtes est effectué.
