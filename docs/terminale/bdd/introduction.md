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

Parmis les **logiciels de gestion de bases de données** (*SGBD*) les plus courants, on retrouve :

- des **logiciels libres** :
    - MariaDB / MySQL
    - PostgreSQL
- des **logiciels propriétaires** :
    - IBM DB2
    - Oracle Database
    - Microsoft SQL Server.

Ces **logiciels** (à l'exception de *SQLite*) fonctionnent en mode **client/serveur** et sont conçus pour gérer plusieurs **millions**, voire **milliards** d'**enregistrement** de manière **fiable** et **sécurisée**. Leur architecture côté serveur est prévue pour êre répartie sur **plusieurs machines** et ainsi permettre une **tenue en charge** lorsqu'un grand nombre de requêtes est effectué.

!!! success ""
    Dans notre cas, pour simplifier les choses, nous travaillerons avec **SQLite** : c'est une **base de données embarquée** sous la forme d'une **bibliothèque**, qui ne repose donc pas sur une **architecture client-serveur** comme les **SGBD** cités précédemment.

!!! tip "Différences SQLite / MySQL"
    **<u>Architecture</u>** :
    
    - **SQLite** : Il s'agit d'une **base de données embarquée**, ce qui signifie qu'elle est **intégrée directement dans l'application**. Il n'y a **pas de serveur distinct**, et la **base de données** est **stockée** dans un **simple fichier** sur le système de fichiers.
    - **MySQL** : Il utilise une **architecture client-serveur**. Un **serveur MySQL** est nécessaire pour gérer les **connexions des clients** et **exécuter les requêtes**.

    **<u>Accessibilité</u>** :
    
    - **SQLite** : En raison de son caractère embarqué, **SQLite** est souvent utilisé pour les **applications mobiles**, les **logiciels autonomes** et les **petits projets**. Il est **léger** et ne nécessite pas d'installation de **serveur**.
    - **MySQL** : Il est couramment utilisé pour des applications nécessitant une **gestion centralisée des données**. Il est plus adapté aux **projets plus importants** et aux **applications Web**.

    **<u>Configuration et Administration</u>** :
    
    - **SQLite** : En raison de sa **nature embarquée**, il nécessite **moins de configuration et d'administration**. Cependant, cela signifie également qu'il a **moins de fonctionnalités avancées** par rapport aux **systèmes de gestion de bases de données client-serveur**.
    - **MySQL** : Il offre une large gamme de **fonctionnalités avancées**, mais cela peut rendre la **configuration** et l'**administration plus complexes**.

    **<u>Performance</u>** :
    
    - **SQLite** : En général, **SQLite** peut être **plus rapide** dans certaines situations, en particulier pour des cas d'utilisation simples et avec des volumes de données limités.
    - **MySQL** : Il peut être plus adapté aux **applications nécessitant une gestion de données plus complexe**, des **transactions multiples** et une grande **concurrence d'accès aux données**.

    En résumé, bien que **SQLite** et **MySQL** soient tous deux des **SGBD**, ils sont adaptés à des **contextes différents** en raison de leurs **architectures** et **fonctionnalités respectives**. **SQLite** est souvent préféré pour des **projets plus légers**, tandis que **MySQL** est utilisé dans des **environnements plus complexes** et nécessitant une **gestion centralisée des données**.