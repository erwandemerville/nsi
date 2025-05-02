from itertools import permutations
from time import time
        
def calculer_distance(trajet, distances):
    ''' Calculer et renvoyer la distance d'un trajet. '''
    distance_totale = 0
    for i in range(len(trajet) - 1):
        distance_totale += distances[trajet[i]][trajet[i + 1]]
    # Ajouter la distance pour revenir à la ville de départ
    distance_totale += distances[trajet[-1]][trajet[0]]
    return distance_totale

def voyageur_brute(villes, distances, ville_depart):
    ''' Algorithme de force brute pour déterminer le ou les meilleurs trajets possibles. '''
    # Créer une liste des indices des villes (0, 1, 2, ...)
    indices_villes = list(range(len(villes)))

    # Retirer l'indice correspondant à la ville de départ
    ville_depart_index = villes.index(ville_depart)
    indices_villes.remove(ville_depart_index)

    # Générer toutes les permutations possibles des indices des villes restantes
    permutations_villes = permutations(indices_villes)

    # Initialiser liste des résultats et distance min
    res = []
    dmin = float('inf')

    for permutation in permutations_villes:
        # Ajouter l'indice de la ville de départ au début de la permutation
        trajet = [ville_depart_index] + list(permutation)
        # Calculer la distance totale du trajet
        distance_totale = calculer_distance(trajet, distances)
        # Convertir les indices des villes en noms de villes
        trajet_villes = [villes[i] for i in trajet] + [ville_depart]
        # Ajouter ou non à la liste des résultats
        if distance_totale < dmin:
            dmin = distance_totale
            res = []
            res.append((distance_totale, trajet_villes))
        elif distance_totale == dmin:
            res.append((distance_totale, trajet_villes))

    return res

# ====> Test de la fonction <=====

# Variables (constantes) pouvant être modifiées
VILLE_DEPART = "Brest"  # indique la ville de départ
NB_VILLES = 6  # indique avec combien de villes tester l'algorithme

# Définition des villes et distances
villes = ["Brest", "Bordeaux", "Lille", "Lyon", "Marseille", "Paris", "Toulouse", 
          "Nice", "Strasbourg", "Nantes", "Rennes", "Montpellier", "Grenoble", "Dijon"]
distances = [
    [0, 598, 708, 872, 1130, 572, 1256, 1468, 1024, 372, 426, 1025, 1084, 992],
    [598, 0, 802, 520, 637, 554, 243, 862, 957, 450, 572, 804, 655, 654],
    [708, 802, 0, 650, 1002, 225, 899, 1457, 308, 656, 736, 191, 661, 532],
    [872, 520, 650, 0, 367, 465, 570, 429, 486, 660, 762, 308, 81, 492],
    [1130, 637, 1002, 367, 0, 777, 403, 474, 795, 1004, 1099, 117, 776, 630],
    [572, 554, 225, 465, 777, 0, 680, 1244, 397, 345, 208, 668, 514, 316],
    [1256, 243, 899, 570, 403, 680, 0, 873, 857, 589, 590, 864, 721, 678],
    [1468, 862, 1457, 429, 474, 1244, 873, 0, 795, 1380, 1396, 407, 998, 678],
    [1024, 957, 308, 486, 795, 397, 857, 795, 0, 1044, 1137, 493, 689, 345],
    [372, 450, 656, 660, 1004, 345, 589, 1380, 1044, 0, 104, 740, 1058, 688],
    [426, 572, 736, 762, 1099, 208, 590, 1396, 1137, 104, 0, 799, 1140, 775],
    [1025, 804, 191, 308, 117, 668, 864, 407, 493, 740, 799, 0, 716, 313],
    [1084, 655, 661, 81, 776, 514, 721, 998, 689, 1058, 1140, 716, 0, 576],
    [992, 654, 532, 492, 630, 316, 678, 678, 345, 688, 775, 313, 576, 0]
]
villes = villes[:NB_VILLES]  # réduire la liste des villes au nombre de villes indiqué
distances = [[distances[i][j] for j in range(NB_VILLES)] for i in range(NB_VILLES)]  # réduire le tableau des distances au nombre de villes indiqué

# Appel à la fonction et affichage des résultats
temps_avant = time()  # mesure du temps avant exécution
resultats = voyageur_brute(villes, distances, VILLE_DEPART)  # Appel à la fonction voyageur_brute
temps_apres = time()  # mesure du temps après exécution
for distance, trajet in resultats:  # pour chaque trajet de la liste des résultats
    print("Distance totale parcourue:", distance, "km")  # afficher la distance parcourue
    print("Trajet:", trajet)  # afficher le trajet
print("\nTEMPS D'EXÉCUTION : ", round(temps_apres - temps_avant, 6), "s")