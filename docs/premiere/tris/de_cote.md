## L'algorithme (tri insertion)

!!! abstract "Algorithme du tri par sélection"
    **ALGORITHME** : tri_selection  
    **ENTRÉES** :  
    &nbsp;&nbsp;&nbsp;&nbsp;`tableau` : un **tableau** d'éléments pouvant être **comparés**  
    **SORTIE** : aucune (tri *en place*)

    **DÉBUT**  
    &emsp;&emsp;n ← longueur(tableau)  
    &emsp;&emsp;**POUR** debut **ALLANT DE** 0 **À** n - 2  
    &emsp;&emsp;&emsp;&emsp;indice_min ← minimum(tableau, debut)  
    &emsp;&emsp;&emsp;&emsp;echanger(tableau, debut, indice_min)  
    &emsp;&emsp;**FIN POUR**   
    &emsp;&emsp;Renvoyer **∅**  
    **FIN ALGORITHME**

Fonction tri_par_insertion(Tableau T)
    Pour i de 1 à taille(T) - 1
        valeur_courante = T[i]
        position = i

        # Déterminer la position de l'élément à placer (valeur_courante)
        Tant que position > 0 et T[position - 1] > valeur_courante
            T[position] = T[position - 1]
            position = position - 1

        T[position] = valeur_courante  # Placer l'élément au bon endroit
    Fin Pour
Fin Fonction

Ce que fait cet algorithme, c'est qu'il itère sur chaque élément du tableau. Pour chaque élément, il trouve sa position correcte parmi les éléments déjà triés à sa gauche en déplaçant tous les éléments vers la droite jusqu'à ce qu'il trouve la bonne position, puis il insère l'élément à cette position. Cela continue jusqu'à ce que tout le tableau soit trié.

---

    i est l'indice (flèche en vert clair dans l'animation) de la clé-valeur qu'il faut placer

    POUR i variant de 1 à (longueur - 1) inclus

        cle ← t[i]

        on mémorise dans cle la valeur-clé car cette case risque d'être écrasée

        j ← i - 1

        La variable j contient initialement l'indice juste à gauche de la clé (flèche verte dans l'animation)

        TANT QUE j ≥ 0 et que t[j] > cle

            t[j+1] ← t[j]

            On décale la valeur d'une case à droite

            j ← j - 1

            On passe à la case suivante à gauche

        Fin TANT QUE

        t[j+1] ← cle

        On place la valeur-clé à la place voulue pour obtenir un sous-tableau trié

    Fin POUR

    Renvoyer VIDE (∅)