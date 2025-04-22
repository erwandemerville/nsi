# Un jeu de Tamagotchi

Le but de cet exercice est de simuler un petit **jeu de Tamagotchi** (très simplifié).

Voici un exemple du résultat attendu :

```
Bienvenue dans le jeu Tamagotchi !
Quel est le nom de ton Tamagotchi ? >> Pikachu

État de Pikachu : humeur = 5, énergie = 5

Que veux-tu faire ? (jouer / manger / quitter) >> jouer
Tu as joué avec Pikachu !

État de Pikachu : humeur = 7, énergie = 4

Que veux-tu faire ? >> manger
Tu as nourri Pikachu !

État de Pikachu : humeur = 7, énergie = 7
...
```

!!! success "À télécharger"
    <center style="font-size: 1.4em">
    [Télécharger *tamagotchi.py*](exercices/tamagotchi.py)
    </center>

!!! note "À faire 1"
    Créer une **==classe==** `Tamagotchi` avec les **attributs** suivants :

    - `nom` : le **nom** du tamagotchi (*chaîne de caractères*)
    - `humeur` : un **entier** entre `0` et `10` (10 = très heureux)
    - `energie` : un **entier** entre `0` et `10` (10 = plein d’énergie)

    **==Constructeur==** :  
    Le constructeur doit **initialiser** le **nom du Tamagotchi** (donné en **entrée**), et fixer l’**humeur** et l’**énergie** à `5` par défaut.

    **==Accesseurs== et ==mutateurs==** :  
    Ajoute des **accesseurs** et **mutateurs** pour chaque **attribut**.  
    Les **mutateurs** doivent garantir que les **valeurs** de `humeur` et `energie` restent entre `0` et `10`.

!!! note "À faire 2"
    Ajouter les **méthodes** suivantes pour interagir avec le **Tamagotchi** :

    - `jouer()` : **augmente l’humeur** de `2`, mais **diminue l’énergie** de `1`
    - `manger()` : **augmente l’énergie** de `3`
    - `etat()` : affiche l’**état actuel** du **Tamagotchi** (*nom*, *humeur* et *énergie*)

!!! note "À faire 3"
    Écrire un **programme** (sous la définition de la classe) qui :

      1. **affiche** un **message de bienvenue**,
      2. demande à l'**utilisateur** de **saisir** un **nom** pour le **Tamagotchi**, et crée un **objet** de type `Tamagotchi` avec le **nom saisi**,
      3. affiche l'**état** du **Tamagotchi**,
      4. permets à l’utilisateur de **choisir une action** (*jouer*, *manger* ou *quitter*) dans une **boucle**,
      5. mets à jour l’**état du Tamagotchi** selon l’**action** choisie,
      6. la boucle s’**arrête** si l’utilisateur choisit "quitter" ou si le Tamagotchi tombe à `0` d’**énergie**.