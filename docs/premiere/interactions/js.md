# Dynamiser une page web avec JavaScript

<center>
![Logo JavaScript non-officiel](images/unofficial_JavaScript_logo.png){ width="200px" }
</center>

==**JavaScript**== est un **langage de programmation** largement utilisé dans le **développement Web**, réputé pour sa **polyvalence** et sa **capacité** à ==**créer des interactions dynamiques**== sur les **pages Web**. Créé par **Brendan Eich**, un ingénieur logiciel de *Netscape*, en **1995**, **JavaScript** a rapidement évolué pour devenir **l'un des langages de programmation les plus populaires** au monde.  
Contrairement à **HTML** et **CSS**, qui sont utilisés pour **structurer et styliser les pages Web** respectivement, **JavaScript** permet d'ajouter des **fonctionnalités interactives** et **dynamiques** aux **sites Web**, telles que des **formulaires interactifs**, des **animations**, des **jeux en ligne**, et bien plus encore.

## Introduction

!!! abstract "Point de cours"
    ==**Javascript**== est un langage **interprété** (comme *Python*) qui s'exécute dans le **navigateur** du **client**. Javascript s'est imposé depuis son apparition en **1995** dans le navigateur **Netscape** comme le principal **langage de développement Web** en ==**frontend**== (*côté client*) et depuis une dizaine d'années, sa variante **Node.js** concurence les langages de développement **backend** (*côté serveur*) comme **PHP** ou **Python**.

    Une **page Web** moderne, reçue par un **client**, comporte au moins **trois composants logiciels** :

    - ==**HTML**== pour la **structure du document**.
    - ==**CSS**== pour le paramétrage de l'**apparence des éléments** et leur **positionnement**.
    - ==**Javascript**== pour la définition de programmes qui vont réagir à des **événements** déclenchés **par l'utilisateur de la page** et **modifier la structure de données de la page** ( **éléments HTML** et **styles CSS**) à travers l'API nommée **DOM2**. Le ==**DOM**== est une **représentation** de **l'ensemble de la structure de la page Web** sous la forme d'un **arbre** : les **noeuds** sont les **éléments HTML** et ils ont une **liste de propriétés** : *contenu*, *style*, *événements associés*... Exécuter du **javascript** va donc **modifier l'arbre DOM** de la page web.  
    L'**inspecteur des outils de développement**, accessibles avec la touche ++"F12"++ dans un navigateur, permet de visualiser et modifier les **propriétés** des **éléments du DOM**.

    L'environnement d'exécution d'un code **Javascript** est confiné à l'**onglet de la page Web où il est chargé**. Pour des raisons de sécurité il ne doit pas interagir avec d'**autres pages** ou des **ressources** du **poste client**. Par ailleurs, si on recharge la page auprès du serveur, l'**environnement Javascript est réinitialisé** et les **modifications** de la page effectuées par un code Javascript ne sont **pas répercutées sur la page source** disponible sur le **serveur**.

    Le **Javascript** correspond à un ==**paradigme** de **programmation événementielle**==.

<figure markdown="span">
  ![Arbre DOM](images/schema-dom.svg)
  <figcaption>Schéma HTML DOM (<a href="../images/schema-dom.svg" target="_blank">voir en taille réelle</a>)</figcaption>
</figure>

## Premiers pas avec JavaScript

Une manière simple de mener une première expérimentation du langage **JavaScript** est d'**ouvrir la console Javascript** dans la **fenêtre** des **outils de développement**, en appuyant sur ++"F12"++ ou ++ctrl+shift+k++ sous **Firefox**.

On va exécuter de façon **interactive** une **séquence d'instructions Javascript** pour expérimenter quelques **constructions élémentaires** et **propriétés du langage**. Chaque instruction pourra modifier l'état du **DOM** et donc le **rendu graphique de la page Web**.

!!! note "À faire 1"
    Exécutez les **instructions suivantes**, et observez les **résultats obtenus**.

    ```javascript
    >>> let a = 1
    >>> (a * 3 + 1) ** 2 / 5 - 1
    >>> (a * 3 + 1) ** 2 // commentaire !
    >>> let b = "Hello"
    >>> b + " World"
    >>> typeof(a)
    >>> typeof(b)
    >>> a = b + a
    >>> typeof(a)
    ```

    Indiquez les **bonnes réponses** dans la phrase suivante :  
    **Javascript** est à **typage** (fort | faible) et (dynamique | statique) et une **variable égale à 5** se déclare avec (`let a = 5` | `a = 5`).

!!! note "À faire 2"
    Examinons un exemple avec une **fonction**, une **structure conditionnelle** et une **boucle**. Dans la console, passer en mode **éditeur multiligne** en appuyant sur ++ctrl+b++ et saisissez le **code** ci-dessous :

    ```javascript
    function valabs(x){
        if (x < 0){
            return -x;
        }
        else {
            return x;
        }
    }

    for (let i = -4; i < 5; i = i + 1){
        if (valabs(i) > 2){
            alert(i);
        }
        else {
            console.log(i);
        }
    }
    ```

    Indiquez les **bonnes réponses** dans les deux phrases suivantes :
    
    1. en **JavaScript**, les blocs d'instructions sont **délimités** par (l'indentation | des accolades), les **fonctions** sont **déclarées** avec le mot clef (def | function) et une **boucle bornée** sur les **entiers** entre **1** et **10** commence par l'instruction ( `for k in range(1, 11)` | `for (let k = 1; k < 11; k = k + 1)` )
    2. la **fonction** `alert` affiche son paramètre dans (une fenêtre pop-up | la console) tandis que la **fonction** `console.log` affiche son paramètre dans (une fenêtre pop-up | la console).

## Cours

<center>
[:material-cursor-default-click: Cours sur le langage JavaScript (à lire)](https://pgdg.frama.io/1nsi/ihm/js/){ style="font-size:1.5em" target="_blank" }
</center>

*Exemples* de codes à tester issus du cours ci-dessus :

- [Exemple d'implémentation de gestionnaire d'évènements](https://codepen.io/erwandemerville/pen/YPzrgWb)
- [Exemple d'un tableau 3x3 dont on veut connaître la case cliquée](https://codepen.io/erwandemerville/pen/GgRMeEg)
- [Exemple d'utilisation de variable](https://codepen.io/erwandemerville/pen/wBvrOMM)
- [Exemple de sélection d'éléments](https://codepen.io/erwandemerville/pen/yyLzwNb)

## Autres ressources

Voici également d'autres ressources intéressantes pour vous permettre d'approfondir votre maîtrise du langage **javascript** :

- [https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide)
- [https://www.lyceum.fr/1g/nsi/5-interactions-entre-lhomme-et-la-machine-sur-le-web/4-gestion-des-evenements-en-javascript/](https://www.lyceum.fr/1g/nsi/5-interactions-entre-lhomme-et-la-machine-sur-le-web/4-gestion-des-evenements-en-javascript/)
- [https://www.math93.com/lycee/nsi-1ere/nsi-1ere/146-pedagogie/lycee/nsi/993-nsi-numerique-et-sciences-informatiques-javascript-et-html.html](https://www.math93.com/lycee/nsi-1ere/nsi-1ere/146-pedagogie/lycee/nsi/993-nsi-numerique-et-sciences-informatiques-javascript-et-html.html)

Pour vous entraîner, voir la partie [exercices et notebooks](exercices.md).