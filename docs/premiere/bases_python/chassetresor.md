# Jeu - Chasse au trésor

<figure markdown="span">
  ![Capture 1](images/chassetresor_capture2.png)
  <figcaption>Une image du jeu</figcaption>
</figure>

!!! abstract "Présentation du jeu"
    L'objectif de ce **TP** est de créer un petit jeu de **chasse au trésor** en *Python*, dans lequel le but est de **trouver un trésor** dans une **grille** de taille donnée.

    Le joueur devra cliquer sur les **boutons** de son choix dans la grille, avec à chaque erreur un indice lui indiquant s'il se **rapproche** ou s'il **s'éloigne** du **trésor**.

    Le **nombre de tentatives effectuées** sera enregistré et affiché à la fin du jeu.

    Le module `tkinter` sera utilisé pour gérer l'interface graphique du jeu.

!!! success "À télécharger"
    **Téléchargez** et **ouvrez dans Thonny** le fichier *Python* suivant :

    <center style="font-size:1.3em">
    [chasse_au_tresor.py](scripts/chasse_au_tresor.py)
    </center>

!!! note "À faire"
    Vous devez **compléter le programme** `chasse_au_tresor.py`, en remplaçant les pointillés `...` par le **code approprié**. Les parties du programme à compléter sont indiquées par le commentaire `"À COMPLÉTER"`.

    Vous devez également compléter les **fonctions** `verifier_case` et `calculer_distance`.

    Pour `calculer_distance` :
    
    - vous utiliserez la **fonction native** `abs` qui renvoie la **valeur absolue** d'un nombre donné en entrée,
    - vous utiliserez la [distance de Manhattan](https://fr.wikipedia.org/wiki/Distance_de_Manhattan).

    Aidez-vous des **commentaires** pour compléter les lignes de code incomplètes.

    Une fois votre programme complet, **exécutez-le** pour **tester votre jeu**.

!!! tip "Changer la taille de la grille"
    La **taille de la grille de jeu** est déterminée par la **variable globale** `N` :

    ```python
    N = 5  # Variable globale définissant la taille de la grille
    ```

    Vous pouvez à tout moment modifier cette valeur pour **augmenter la taille** de la **grille** de votre jeu !