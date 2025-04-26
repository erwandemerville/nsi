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
    
    ...

def creer_dict(villes, distances):
    ...

# =====> PROGRAMME PRINCIPAL <=====

# Exemple d'appel à la fonction
villes = ["Brest", "Bordeaux", "Lille", "Lyon", "Marseille", "Paris"]
distances = [
    [0, 598, 708, 872, 1130, 572],
    [598, 0, 802, 520, 637, 554],
    [708, 802, 0, 650, 1002, 225],
    [872, 520, 650, 0, 367, 465],
    [1130, 637, 1002, 367, 0, 777],
    [572, 554, 225, 465, 777, 0]
]

v = creer_dict(villes, distances)  # créer dictionnaire des villes et distances

resultat = voyageur(v, "Lyon")
trajet, distance_totale = resultat
print("Trajet:", trajet)
print("Distance totale parcourue:", distance_totale, "km")