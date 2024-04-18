# Cours - Les algorithmes gloutons

## Introduction

Nous allons voir à travers ce chapitre un **nouveau type d'algorithme** permettant de répondre à des **problèmes complexes**.

!!! question "Force brute"
    La stratégie la plus évidente pour résoudre un problème compliqué est la **force brute** :

    ![Hulk](images/force_brute.png)
    
    - **Principe** : on calcule **tout**, quitte à calculer les choses **plusieurs fois**, voire à calculer des choses qui n'ont pas d'utilité pour trouver la solution.
    - **Type de problème** : tous les problèmes à priori.
    - **Problème** : cela peut prendre énormément de temps si l'on doit faire beaucoup de calculs.

Nous allons voir que l'on peut "tricher" en utilisant la **==stratégie gloutonne==**.

- **Principe** : on ne regarde pas le **problème** dans **sa totalité**. On prend une décision **localement optimale**, de façon **définitive** et sans se soucier de ce que va devenir le problème restant à traiter.
- **Type de problème** : ceux pour lequels on peut trouver plusieurs solutions, optimales ou pas.

Voici un *exemple* : **Mr. Glouton** veut atteindre la case en **bas à droite** en mangeant le plus mal possible.

![Mr Glouton](images/mr_glouton.png)

Comme on le voit, la taille du problème à traiter diminue à chaque décision.

## La problématique des problèmes complexes

Les **problèmes complexes** (**NP**, *Non déterministe Polynomial*) sont des problèmes pour lequels :

- le **coût** de la **résolution** par **force brute** est **plus complexe** qu'un coût **polynomial**,
- on peut trouver la **meilleure solution** si on fait les bons choix **par hasard** et qu'on a de la **chance**,
- on peut vérifier qu'une **solution** qu'on vous propose est **valide** ou **pas** avec un **coût polynomial**.

Nous allons justement voir des problèmes de ce type, et nous y tenterons d'y répondre en temps raisonnable.

## Problème du voyageur de commerce

### Présentation

!!! info "Le problème"
    Imaginons le **problème suivant** : vous devez organiser la tournée de votre commercial. Il doit passer dans **toutes les villes** sous sa responsabilité (une fois uniquement) et revenir à son **point de départ** (*Lille* pour notre exemple). Pour limiter les frais, il faut définir le **trajet le moins long** au total.

    Nous allons nous limiter à **6 villes** uniquement ici.

    ![France](images/france.png)

    Voici un **tableau** récapitulant les **distances** entre ces **6 villes** :

    |            | Brest | Bordeaux | Lille | Lyon | Marseille | Paris |
    |------------|-------|----------|-------|------|-----------|-------|
    | Brest      |   -   |   598    |  708  | 872  |   1130    |  572  |
    | Bordeaux   |  598  |    -     |  802  | 520  |   637     |  554  |
    | Lille      |  708  |   802    |   -   | 650  |   1002    |  225  |
    | Lyon       |  872  |   520    |  650  |  -   |   367     |  465  |
    | Marseille  | 1130  |   637    | 1002  | 367  |    -      |  777  |
    | Paris      |  572  |   554    |  225  | 465  |   777     |   -   |

    Nous pourrions choisir la ville de départ parmi la liste des 6 villes. Il y a donc **6 choix de lieux de départ**.

!!! note "Q.1"
    Partons de **Lille**. Combien de destinations différentes peut-on choisir ?

!!! note "Q.2"
    Partant de **Lille**, on choisit Bordeaux. Combien de destinations différentes peut-on choisir ensuite ?

!!! note "Q.3"
    Après avoir choisi **Lille - Bordeaux - Brest**, combien de destinations différentes peut-on choisir ensuite ?

!!! note "Q.4"
    Combien de **possibilités d'itinéraires différents** va-t-on avoir en partant d'une **première ville aléatoire** pour aller jusqu'à la **6e ville** ? Faire le **calcul**.

Ici, il s'agit de trouver un **chemin fermé**, c'est un **cycle**.

- **1er simplification** : le point de départ n'a aucune importance puisqu'on passe successivement dans **toutes les villes** et qu'on revient au **point de départ**.
- **2e simplification** : le **sens de parcours du cycle** n'a pas d'importance non plus. Dans les deux cas, on fera le tour des **6 villes**. Qu'on fasse Lyon-Lille-... ou Lille-Lyon-... ne changera rien à la **distance parcourue**.

![France parcours](images/france_parcours.png)

!!! note "Q.5"
    Combien de **possibilités** doit-on vraiment calculer en tenant compte des **deux simplifications** précédentes ?

!!! note "Q.6"
    Combien de **possibilités d'itinéraires différents** va-t-on avoir pour **12 villes** ? Juste deux petites villes en plus...

### Résolution par force brute

Avant de passer aux **algorithmes gloutons**, voyons comment résoudre ce problème par **force brute** : nous allons faire **tous les calculs** et ne garder que le **meilleur**.

Ici, avec **6 villes**, il faut donc tester les **60 possibilités** une par une.  
Avec **12 villes**, on passe à **20 millions de possibilités**.

C'est faisable avec **6 villes**.

Le **trajet optimal** sera réalisé avec le parcours suivant (dans un sens ou dans l'autre) :

- **Brest-Bordeaux-Marseille-Lyon-Paris-Lille-Brest en 3000 km**
- **Brest-Lille-Paris-Lyon-Marseille-Bordeaux-Brest en 3000 km**

![France optimum](images/france_optimum.png)

L'itinéraire de la partie précédente était correct mais celui proposé ici donne un trajet optimal (si on a réussi à le trouver !)

!!! note "Q.7"
    Choisir un **autre itinéraire** et calculer **à la main** la **distance parcourue**. Le tableau des distances est fourni ci-dessous. Vérifier qu'on obtient pas moins qu'avec le trajet optimal.

    |            | Brest | Bordeaux | Lille | Lyon | Marseille | Paris |
    |------------|-------|----------|-------|------|-----------|-------|
    | Brest      |   -   |   598    |  708  | 872  |   1130    |  572  |
    | Bordeaux   |  598  |    -     |  802  | 520  |   637     |  554  |
    | Lille      |  708  |   802    |   -   | 650  |   1002    |  225  |
    | Lyon       |  872  |   520    |  650  |  -   |   367     |  465  |
    | Marseille  | 1130  |   637    | 1002  | 367  |    -      |  777  |
    | Paris      |  572  |   554    |  225  | 465  |   777     |   -   |

### Algorithme glouton

Nous avons vu que la **force brute** ne permet pas de résoudre (en un temps raisonnable) le problème du **voyageur de commerce** lorsqu'on **augmente le nombre de villes**.

!!! info "Stratégie"
    Nous appliquerons une **stratégie gloutonne** à notre **voyageur de commerce**.

    Voici le **choix local** que nous allons toujours privilégier en espérant que cela nous mène à une solution globale correcte : nous allons systématiquement **choisir la ville non-visitée la plus proche**.

On rappelle les distances :

|            | Brest | Bordeaux | Lille | Lyon | Marseille | Paris |
|------------|-------|----------|-------|------|-----------|-------|
| Brest      |   -   |   598    |  708  | 872  |   1130    |  572  |
| Bordeaux   |  598  |    -     |  802  | 520  |   637     |  554  |
| Lille      |  708  |   802    |   -   | 650  |   1002    |  225  |
| Lyon       |  872  |   520    |  650  |  -   |   367     |  465  |
| Marseille  | 1130  |   637    | 1002  | 367  |    -      |  777  |
| Paris      |  572  |   554    |  225  | 465  |   777     |   -   |

!!! note "Q.8"
    On décide de partir de Lyon. Choisir la ville suivante en prenant la ville la plus proche non encore visitée. Calculer la distance parcourue.

!!! note "Q.9"
    On a fait Lyon-Marseille. Quelle ville choisir ensuite ?

!!! note "Q.10"
    On a fait Lyon-Marseille-Bordeaux. Quelle ville choisir ensuite ?

!!! note "Q.11"
    On a fait Lyon-Marseille-Bordeaux-Paris. Quelle ville choisir ensuite ?

A partir de là, c'est fini. On fait **Lille-Brest** (c'est la seule destination disponible) puis **Brest-Lyon** pour revenir au **point de départ**.

Cela donne **d = 367 + 637 + 554 + 225 + 708 + 872 km**, soit au total **d = 3363 km**.

- **Désavantage** : c'est moins bien que la **solution optimale de 3000 km**.
- **Avantage** : avec plus de villes que sur notre exemple, le programme en **force brute** tournerait encore très longtemps...
