# Exercices sur les boucles non-bornées `while`

!!! note "Exercice 1"
    On veut écrire une **simulation du jeu de Monopoly**.  
    Un joueur peut rejouer s'il fait un **double**.

    Mais attention ! S'il faut **trois doubles de suite**, il doit aller en **prison**.

    Le **programme** à concevoir doit :

    - **Simuler le lancer** aléatoire de deux dés à 6 faces (vous utiliserez la fonction `randint` du module `random`.);
    - **Afficher la valeur** de chaque face ainsi que le nombre de cases à parcourir ;
    - **Relancer les dés** dans le cas d'un double ;
    - **Recommencer**... et envoyer le joueur en prison s'il y a **trois doubles de suite**.

    Un exemple d'affichage avec envoi en prison :

    ```python
    Les faces sont 5 et 5 : Avancez de 10 cases.
    Il y a un double, rejouez.
    Les faces sont 2 et 2 : Avancez de 4 cases.
    Il y a un double, rejouez.
    Les faces sont 6 et 6 : Avancez de 12 cases.
    Oups ! Encore un double, allez en prison !
    ```

!!! note "Exercice 2"
    On souhaite écrire un programme permettant de restreindre l'accès à une plateforme aux visiteurs adultes.

    Écrivez un **programme** qui :

    - demande à l'utilisateur son **âge**,
    - **tant que** l'**âge** est **inférieur** à **18** ans, on redemande l'âge.
    - Si l'âge est d'au moins **18** ans, on affiche "Vous pouvez entrer".