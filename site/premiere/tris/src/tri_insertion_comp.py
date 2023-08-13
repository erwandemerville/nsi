#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

# ===> ZONE À MODIFIER <===
TABLEAU = [12, 9, 7, 5, 3, 1]  # Tableau sur lequel effectuer le tri par insertion
MODE_SLEEP = False  # Mode "pas à pas" (True = activé, False = désactivé)
# =========================

def tri_insertion(tableau: 'list[int]', pas_a_pas: bool) -> None:
    ''' Effectue le tri par insertion en place des éléments d'un tableau donné.
    Affiche l'état du tableau à chaque étape et le nombre de comparaisons effectuées.
    :param tableau: (list[int]) un tableau d'entiers à trier
    :param pas_a_pas: (bool) True pour activer le mode pas à pas, False sinon '''

    cmp = 0

    for i in range(1, len(tableau)):
        print(f'==> ITÉRATION i = {i} <==')

        valeur_courante = tableau[i]
        print(f'Élément à insérer : {valeur_courante}')  # AFFICHAGE DE L'ELEMENT A INSERER

        j = i - 1

        print('[' + ''.join('{:^5}'.format(val) if val != valeur_courante else '{:^5}'.format('|' + str(val) + '|') for val in tableau) + '] - valeur_courante = ' + str(valeur_courante)) # AFFICHAGE : ELEMENT A INSERER
        l = '['
        for k in range(len(tableau)):
            if k == i:
                l += '{:^5}'.format('i')
            elif k == j:
                l += '{:^5}'.format('j')
            else:
                l += '{:^5}'.format('--')
        l += ']'
        print(l) # AFFICHAGE : INDICES i ET j
        
        nbc = 1
        cmp += 1
        if j >= 0:
            print(f'Comparaison entre {tableau[j]} et {valeur_courante}', end=' ')
            if tableau[j] > valeur_courante: print(f'({tableau[j]} > {valeur_courante})')
            else: print(f'({tableau[j]} <= {valeur_courante} donc FIN DU WHILE)')
            print(f'=> {nbc} comparaison ({cmp} au total)\n')

            if pas_a_pas: input('Appuyez sur ENTRER pour continuer...\n')
        while j >= 0 and tableau[j] > valeur_courante:
            tableau[j + 1] = tableau[j]
            j = j - 1

            print('[' + ''.join('{:^5}'.format(val) if val != valeur_courante else '{:^5}'.format('|' + str(val) + '|') for val in tableau) + '] - valeur_courante = ' + str(valeur_courante)) # AFFICHAGE : ELEMENT A INSERER
            l = '['
            for k in range(len(tableau)):
                if k == i:
                    l += '{:^5}'.format('i')
                elif k == j:
                    l += '{:^5}'.format('j')
                else:
                    l += '{:^5}'.format('--')
            l += ']'
            print(l) # AFFICHAGE : INDICES i ET j
            
            if j >= 0:
                nbc += 1
                cmp += 1
                print(f'Comparaison entre {tableau[j]} et {valeur_courante}', end=' ')
                if tableau[j] > valeur_courante: print(f'({tableau[j]} > {valeur_courante})')
                else: print(f'({tableau[j]} <= {valeur_courante} donc FIN DU WHILE)')
                print(f'=> {nbc} comparaisons ({cmp} au total)\n')

                if pas_a_pas: input('Appuyez sur ENTRER pour continuer...\n')

        tableau[j + 1] = valeur_courante
        if j + 1 != i:
            print(f'Repositionner valeur_courante (copier {valeur_courante} dans tableau[{j + 1}])')
        else:
            print(f'Repositionner valeur_courante (pas de changement)')
        print('[' + ''.join('{:^5}'.format(val) if val != valeur_courante else '{:^5}'.format('|' + str(val) + '|') for val in tableau) + ']') # AFFICHAGE : ELEMENT A INSERER
        
        if pas_a_pas: input('\nAppuyez sur ENTRER pour continuer...\n')
        else: print('\n')
    
    print(f'=> {cmp} comparaisons au total <=\n')

if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''

    tri_insertion(TABLEAU, pas_a_pas=MODE_SLEEP)