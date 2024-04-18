# Cours - La recherche dichotomique

La **méthode de recherche dichotomique** est **une approche puissante et efficace** utilisée en informatique et dans d'autres domaines pour **trouver** rapidement des **éléments** dans des **ensembles** de données **ordonnées**.

Aussi connue sous le nom de *recherche binaire*, cette méthode repose sur un **principe simple** mais efficace, consistant à **diviser à chaque étape l'intervalle de recherche par deux**, réduisant ainsi considérablement le **nombre d'itérations nécessaires** pour trouver la **valeur cible**.

Dans ce cours, nous explorerons en détail les principes fondamentaux de la ==**recherche dichotomique**==, ses avantages et ses limitations, ainsi que des **exemples** concrets pour illustrer son fonctionnement.

!!! question ""
    Vous avez probablement déjà joué au **jeu** consistant à "trouver un nombre entre `1` et `100`", et proposé la réponse `50`.  
    Si la réponse est "perdu, c'est plus", vous proposez alors `75` et si l'on vous répond "perdu c'est moins" vous proposez finalement `62`... C'est un exemple de recherche dichotomique !

    Faire une recherche dichotomique, c'est **chercher** une **valeur** dans un **tableau** en prenant le **milieu** de l'**ensemble des solutions possibles** (qui sont donc **rangées**) pour éliminer **la moitié des possibilités** à chaque **étape**.

## L'algorithme

L'algorithme en **pseudo-code** peut s'écrire de la manière suivante :

!!! abstract "Algorithme de recherche dichotomique" 
    <div style="font-size:1.1em">
    **ALGORITHME** : recherche_dicho  
    **ENTRÉE** :  
    &emsp;&emsp;`tableau` : un **tableau** d'éléments  
    &emsp;&emsp;`element` : un **élément à chercher** dans le tableau  
    **SORTIE** : VRAI si l'élément est trouvé, FAUX sinon

    **DÉBUT**  
    &emsp;&emsp;debut ← 0  
    &emsp;&emsp;fin ← longueur(tableau) - 1  
    &emsp;&emsp;trouve ← FAUX  
    &emsp;&emsp;**TANT QUE** PAS trouve **ET QUE** debut ⩽ fin :  
    &emsp;&emsp;&emsp;&emsp;milieu ← partie_entière((debut + fin) / 2)  
    &emsp;&emsp;&emsp;&emsp;**SI** tableau[milieu] **EST ÉGAL À** élément :  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;trouve ← VRAI  
    &emsp;&emsp;&emsp;&emsp;**SINON** :  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**SI** element **EST SUPÉRIEUR À** tableau[milieu] :  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;debut ← milieu + 1  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**SINON** :  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fin ← milieu - 1  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**FIN SI**  
    &emsp;&emsp;&emsp;&emsp;**FIN SI**  
    &emsp;&emsp;**FIN TANT QUE**  
    &emsp;&emsp;**RENVOYER** trouve  
    **FIN ALGORITHME**
    </div>

## Simulation de la recherche dichotomique

Voici un **simulateur** vous permettant de tester l'**algorithme** de **recherche dichotomique**.  
(*Source* : [Infoforall](https://www.infoforall.fr/art/algo/animation-de-la-recherche-dichotomique/#partie_1))

!!! success "Simulateur de recherche dichotomique"
    <p><input type="button" onclick="hasard('etape8Dicho')" value="Créer des valeurs au hasard" style="padding: 10px;background: #CCCC55;" /></p>
    <p>Valeur cherchée : <input id="valRecherche" type="number" value="50" min="0" max="100" step="1"></p>

    <p>
        <input type="button" onclick="startdicho2('etape8Dicho')" value="Lancer la recherche dichotomique" style="padding: 10px;background: #CCCC55;">
        <input type="button" onclick="vitesse('etape8Dicho',1)" value="Rapide" style="padding: 10px;background: #CCCC55;">
        <input type="button" onclick="vitesse('etape8Dicho',5)" value="Moyen" style="padding: 10px;background: #CCCC55;">
        <input type="button" onclick="vitesse('etape8Dicho',10)" value="Lent" style="padding: 10px;background: #CCCC55;">
        <input type="button" onclick="pause('etape8Dicho')" value="Pause / Reprise" style="padding: 10px;background: #CCCC55;">
    </p>

    <div id="etape8Dicho">
        <div style="overflow-x:auto;">
            <table class="color6" style="font-size:small;">
                <tbody>
                    <tr class="trindic">
                        <td></td>
                        <td class="ext"><span style="font-size: large">g</span></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class="pilier"><span style="font-size: large">c</span></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class="ext"><span style="font-size: large">d</span></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                    </tr>
                    <tr class="index">
                        <td>Index</td>
                        <td class="ext">00</td>
                        <td class="ext">01</td>
                        <td class="ext">02</td>
                        <td class="ext">03</td>
                        <td class="pilier">04</td>
                        <td class="ext">05</td>
                        <td class="ext">06</td>
                        <td class="ext">07</td>
                        <td class="ext">08</td>
                        <td class="rejet">09</td>
                        <td class="rejet">10</td>
                        <td class="rejet">11</td>
                        <td class="rejet">12</td>
                        <td class="rejet">13</td>
                        <td class="rejet">14</td>
                        <td class="rejet">15</td>
                        <td class="rejet">16</td>
                        <td class="rejet">17</td>
                        <td class="rejet">18</td>
                        <td class="rejet">19</td>
                    </tr>
                    <tr class="trelement">
                        <td>Elément</td>
                        <td class="val">06</td>
                        <td class="val">08</td>
                        <td class="val">09</td>
                        <td class="val">13</td>
                        <td class="pilier">18</td>
                        <td class="val">37</td>
                        <td class="val">37</td>
                        <td class="val">59</td>
                        <td class="val">60</td>
                        <td class="rejet">60</td>
                        <td class="rejet">61</td>
                        <td class="rejet">68</td>
                        <td class="rejet">70</td>
                        <td class="rejet">80</td>
                        <td class="rejet">80</td>
                        <td class="rejet">83</td>
                        <td class="rejet">83</td>
                        <td class="rejet">89</td>
                        <td class="rejet">91</td>
                        <td class="rejet">96</td>
                    </tr>
                    <tr class="trraison" style="height:50px;">
                        <td></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class="trouve">ok</td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                        <td class=""></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <script src='../javascripts/animation_dicho.js'></script>
    <script src='../javascripts/lancement_dicho_finale_uniquement.js'></script>
    <link rel="stylesheet" href="../stylesheets/style_simulateur.css">

## Implémentation en Python

### Recherche séquentielle

On a tout d'abord implémenté l'algorithme de **recherche séquentielle** que nous avons déjà vu auparavant. Cela nous permettra de comparer cet ancien algorithme avec le nouvel algorithme de **recherche dichotomique**.

```python
def recherche_sequentielle(tableau, element):
    ''' Renvoie True si element est trouvé, False sinon.
    :param tableau: (list[int]) une liste d'éléments
    :param element: (int) l'élément à rechercher
    :return (bool): True ou False '''

    for el in tableau:
        if element == el:
            return True
    return False
```

Voici une **autre version** de cette fonction utilisant un **parcours par indice** plutôt que par élément :

```python
def recherche_sequentielle_v2(tableau, element):
    for i in range(len(tableau)):
        if element == tableau[i]:
            return True
    return False
```

### Recherche dichotomique

La **recherche dichotomique** peut s'implémenter en *Python* de la manière suivante :

```python
def recherche_dicho(tableau, element):
    ''' Effectue une recherche dichotomique dans un tableau.
    Renvoie True si element est trouvé, False sinon. '''
    
    debut = 0
    fin = len(tableau) - 1
    trouve = False
    while not trouve and debut <= fin:
        milieu = (debut + fin) // 2
        if tableau[milieu] == element:
            trouve = True
        else:
            if element > tableau[milieu]:
                debut = milieu + 1
            else:
                fin = milieu - 1
    return trouve
```

On rappelle que l'opérateur `//` permet d'obtenir le **quotient d'une division euclidienne** entre deux nombres.  
Ainsi, l'instruction `milieu = (debut + fin) // 2` de la **ligne 9** permet d'obtenir un **nombre entier**.

## Coût de la recherche dichotomique

!!! success "Un programme pour analyser les algorithmes de recherche"
    Voici un **programme Python** permettant :

    - de générer les **courbes** de l'**évolution du nombre de comparaisons** effectuées pour les deux **algorithmes** de **recherche**, dans le **pire des cas**.
    - de générer les **courbes** de l'**évolution du temps d'exécution** mesuré pour les deux **algorithmes** de **recherche**, dans le **pire des cas**.
    - d'afficher dans la console un **tableau** montrant le **nombre de comparaisons** effectuées pour les deux **algorithmes** de **recherche**.

    <center>
    [:material-language-python: Télécharger le programme `analyse_recherche.py`](src/analyse_recherche.py){ style="font-size:1.5em" target="_blank" }
    </center>

!!! abstract "Analyse du nombre de comparaisons"
    Voici un tableau montrant l'évolution du **nombre de comparaisons** pour les deux **algorithmes de recherche**, pour des **tailles** de tableaux allant de $N = 2^0$ jusqu'à $N = 2^{10}$ :

    <center>

    | Taille N   | Recherche séquentielle | Recherche dichotomique |
    |------------|------------------------|------------------------|
    | $2^0 = 1$  | 1                      | 1                      |
    | $2^1 = 2$  | 2                      | 2                      |
    | $2^2 = 4$  | 4                      | 3                      |
    | $2^3 = 8$  | 8                      | 4                      |
    | $2^4 = 16$ | 16                     | 5                      |
    | $2^5 = 32$ | 32                     | 6                      |
    | $2^6 = 64$ | 64                     | 7                      |
    | $2^7 = 128$ | 128                    | 8                      |
    | $2^8 = 256$ | 256                    | 9                      |
    | $2^9 = 512$ | 512                    | 10                     |
    | $2^{10} = 1024$ | 1024                   | 11                     |

    </center>

    ---

    Voici des **courbes d'évolution** du **nombre de comparaisons** pour les deux **algorithmes de recherche**. On s'est ici arrêté à une taille $N = 2^6$ afin de mieux observer la forme des courbes :

    ![Courbes évolution nb comps.](images/evolution_comps.png)

!!! note "Exercice 1"
    En vous aidant des informations précédentes, déterminez le **nombre de comparaisons effectuées** pour une taille $N = 2^{11} = 2048$ :

    - dans le cas d'une **recherche séquentielle** dans le **pire des cas** (élément recherché absent du tableau),
    - dans le cas d'une **recherche dichotomique** dans le **pire des cas** (élément recherché absent du tableau).

!!! note "Exercice 2"
    Exprimez la taille $N$ d'un tableau en fonction :

    - du **nombre de comparaisons**, que l'on notera $C_{seq}, nécessaire dans le **pire cas** pour rechercher un élément dans un tableau de taille $N$ avec la **recherche séquentielle**,
    - du **nombre de comparaisons**, que l'on notera $C_{dicho}, nécessaire dans le **pire cas** pour rechercher un élément dans un tableau de taille $N$ avec la **recherche dichotomique.**.