#!/usr/bin/env python
# -*- coding: utf-8 -*-

CNT = 0  # Variable globale utilisée pour compter le nombre de comparaisons

def tri_selection(tableau: list[int]) -> None:
    ''' Effectue le tri par sélection en place des éléments d'un tableau donné.
    
    :param tableau: (list[int]) un tableau d'entiers à trier '''

    global CNT

    n = len(tableau)  # Récupérer la longueur du tableau
    for debut in range(0, n - 1):  # Parcourir tous les éléments jusqu'à l'avant dernier (*)
        indice_min = debut  # Initialiser l'indice du minimum à debut
        for i in range(debut + 1, len(tableau)):  # Parcourir tous les éléments du tableau à partir de debut + 1
            CNT += 1
            if tableau[i] < tableau[indice_min]:  # Si l'élément d'indice i est inférieur à celui d'indice indice_min
                indice_min = i  # Le nouvel indice du minimum est i
                # On effectue une permutation
        temp = tableau[debut]
        tableau[debut] = tableau[indice_min]
        tableau[indice_min] = temp

def nombre_comparaisons(tableau: list[int]) -> None:
     ''' Affiche le nombre de comparaisons effectué par le tri par sélection d'un tableau donné. '''

     avant = tableau.copy()
     tri_selection(tableau) # Effectuer le tri par sélection de la liste
     print(f'Tableau : {avant}\nNombre de comparaisons : {CNT}')

if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    tableau = [2, 5, 7, 9, 12, 59, 94]

    nombre_comparaisons(tableau)
