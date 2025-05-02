from time import time

def trouver_ville_suivante(ville_actuelle, villes_restantes, villes):
    ''' Trouve la ville, parmi celles qui restent à parcourir, ayant la plus
    petite distance avec la ville dans laquelle on se trouve actuellement.
    :param ville_actuelle: (str) la ville actuelle
    :param villes_restantes: (list[str]) liste des villes qui restent à parcourir
    :param villes: (dict[dict]) le dictionnaire des villes et distances
    :return: (str) la ville de plus petite distance avec la ville actuelle '''
    
    ...

def voyageur(villes, ville_depart):
    ''' Résolution du problème du voyageur de commerce.
    :param villes: (dict[dict]) dictionnaire des villes et distances
    :param ville_depart: (str) la ville de départ
    :return: (tuple) tuple contenant le trajet effectué (list[str]) et la distance totale parcourue (int) '''
    
    trajet = [...]  # le trajet effectué contient au début seulement la ville de départ
    distance_totale = 0  # la distance totale parcourue est initialement de 0 km
    ville_actuelle = ...  # la ville actuellement parcourue est la ville de départ
    villes_restantes = [ville for ville in villes if ville != ...]  # liste des villes restantes à parcourir

    while ...:  # tant qu'il reste des villes à parcourir
        prochaine_ville = ...  # on récupère la prochaine ville à parcourir en appelant la fonction adéquate
        ... # on ajoute la prochaine ville à parcourir au trajet
        distance_totale += ...  # on ajoute la distance entre la ville actuelle
                                # et la prochaine ville à la distance totale
        ... = ...  # la "prochaine ville" devient la ville actuellement parcourue
        villes_restantes.remove(...)  # on supprime la nouvelle ville actuelle des villes restantes à parcourir

    # Retourner à la ville de départ
    ...  # on doit revenir dans la ville de départ, on l'ajoute donc au trajet
    distance_totale += ...  # on ajoute à la distance totale la distance
                            # entre la ville actuelle et la ville de départ

    return trajet, distance_totale  # enfin, on renvoie le trajet déterminé et la distance correspondante

def creer_dict(villes, distances):
    ''' Renvoie un dictionnaire contenant les noms des villes et
    les distances entre chaque ville. 
    :param villes: (liste des villes) 
    :param distances: (tableau des distances) 
    :return: (dict of dict) dictionnaire des villes et distances entre elles '''
    
    res = {}  # définir un dictionnaire vide
    nb_villes = ...  # nombre de villes (obtenu grace à la taille du tableau des distances)
    for i in range(...):  # pour i allant de 0 à la nb_villes - 1
        ...  # ajouter la ville d'indice i au dictionnaire res en l'associant à un dictionnaire vide
        for j in range(...):  # pour j allant de 0 à la nb_villes - 1
            res[...][...] = ...  # ajout de la ville d'indice j dans le dictionnaire de la ville
                                 # d'indice i, avec la distances entre la ville i et j comme valeur
    return res

# =====> PROGRAMME PRINCIPAL <=====

# Variables (constantes) pouvant être modifiées
VILLE_DEPART = "Lyon"  # indique la ville de départ
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
villes = villes[:NB_VILLES]
distances = [[distances[i][j] for j in range(NB_VILLES)] for i in range(NB_VILLES)]  # réduire le tableau des distances au nombre de villes indiqué

# Création d'un dictionnaire des villes et distances
v = creer_dict(villes, distances)

# Appel à la fonction et affichage des résultats
temps_avant = time()  # mesure du temps avant exécution
resultat = voyageur(v, VILLE_DEPART)  # appel de la fonction de résolution gloutonne
temps_apres = time()  # mesure du temps après exécution
trajet, distance_totale = resultat  # récupérer le trajet et la distance totale obtenus
print("Trajet:", trajet)
print("Distance totale parcourue:", distance_totale, "km")
print("\nTEMPS D'EXÉCUTION : ", round(temps_apres - temps_avant, 6), "s")