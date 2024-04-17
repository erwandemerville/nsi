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

