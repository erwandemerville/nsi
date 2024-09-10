# Activité d'introduction

!!! quote "Source"
    Inspiré d'une activité du *Hachette NSI Terminale*.

Pour simuler la **trajectoire d’un projectile** que l’on lance en l’air avec une certaine **vitesse** et qui est soumis à la **gravité**, on a besoin de connaître sa **position** $x$ et $y$ et sa **vitesse** $vx$ et $vy$.  
Après un intervalle de temps $dt$, la **position** et la **vitesse** du projectile sont modifiées ainsi :

- $x = x + dt \times vx ; y = y + dt \times vy$ ;
- $vy = vy − g \times dt$ où $g$ est l’intensité de la pesanteur ($9,81 m/s^2$ sur Terre).

Pour représenter le **projectile**, nous allons utiliser un **nouveau type de données** : un ==**objet**==.

Pour créer un **objet** représentant un **projectile**, il faut d’abord définir une ==**classe**==, que l’on appellera ici `Projectile`.

La fonction `Projectile()` **renverra** alors un **nouvel objet** de type `Projectile`, qui est comme une coquille vide.  
On peut ensuite « remplir » cette coquille avec des ==**attributs**== qui représentent l’**état du projectile**, ici `x`, `y`, `vx` et `vy`, auxquels on accède par la **notation pointée** :

```python
class Projectile:  # déclarer une classe
    pass

balle = Projectile()  # créer un objet
balle.x = 0  # affecter son attribut x,
balle.y = 0  # son attribut y,
balle.vx = 10  # son attribut vx,
balle.vy = 20  # et son attribut vy
```

<figure markdown>
  ![Screen](images/screen_activite_preliminaire.png){ width="50%" }
  <figcaption>Représentation de l'objet `balle`</figcaption>
</figure>

!!! success "À faire"
    Télécharger et ouvrir dans **Thonny** le script *Python* suivant :

    - [projectile.py](exercices/projectile.py) : script *Python* à compléter (en suivant les exercices suivants)

!!! note "Exercice 1"
    Écrire la **fonction** `pas(balle, dt)` qui prend une balle en paramètre et modifie son état après l’intervalle de temps `dt` (vous devez donc redéfinir les **attributs** `x`, `y` et `vy`).

!!! note "Exercice 2"
    Écrire un **programme** qui **crée une balle** et **appelle 50 fois la fonction** `pas` avec le paramète `dt = 0.1` en **affichant** à chaque fois la **position de la balle**.

!!! note "Exercice 3"
    **Modifier** la **fonction** `pas` pour qu’elle **affiche la trajectoire de la balle** en **dessinant un trait** depuis sa dernière position.  
    On utilisera la bibliothèque `turtle` et notamment la fonction `goto(x,y)` qui déplace la tortue à la position `x`, `y` en **traçant un trait**.

La fonction `pas` n’a de sens que si on lui passe un projectile comme premier paramètre.  
Pour rendre cela explicite, on peut la définir *à l’intérieur* de la classe `Projectile`. On dit que l’on définit la **méthode** `pas` de la **classe** `Projectile`.  
Au lieu d’appeler la fonction `pas(balle, dt)`, on utilise la **notation pointée** pour appeler cette méthode : `balle.pas(dt)`.

```python
class Projectile:
    def pas(self , dt):  # définir la méthode `pas` dans la classe `Projectile`
        ...              # `self` est l'objet pour lequel on a appelé la méthod
...
balle.pas(dt)            # appeler la méthode `pas` pour l'objet `balle`
```

!!! note "Exercice 4"
    Modifier le **programme** précédent pour définir la fonction `pas` sous forme d’une **méthode** de la classe `Projectile`.

!!! note "Exercice 5"
    Modifier la **méthode** `pas` pour programmer le **rebond sur le sol** : si la coordonnée $y$ du projectile devient **négative**, on **inverse** la **vitesse verticale** $vy$.

    *Note : Tel que programmé ici, le rebond n’a pas lieu au moment où la balle touche le sol à proprement parler, mais après qu’elle l’ait déjà traversé. Il en résulte que la vitesse verticale risque d’être plus élevée que dans la réalité, et la balle risque de rebondir plus haut que son rebond précédent. Une simulation correcte devrait estimer le moment précis où la balle.*

!!! note "Exercice 6"
    Modifier le **programme** pour créer **plusieurs balles** avec des **positions** et des **vitesses initiales différentes**, et lancer une simulation en appelant répétitivement la **méthode** `pas` de **chaque balle** à tour de rôle.

    On pourra utiliser les fonctions `penup` et `pendown` du module `Turtle` pour **relever** et **rabaisser** le crayon pour passer d'une balle à une autre.