def trouver_ville_suivante(ville_actuelle, villes_restantes, villes):
    ''' Trouve la ville, parmi celles qui restent à parcourir, ayant la plus
    petite distance avec la ville dans laquelle on se trouve actuellement.
    :param ville_actuelle: (str) la ville actuelle
    :param villes_restantes: (list[str]) liste des villes qui restent à parcourir
    :param villes: (dict[dict]) le dictionnaire des villes et distances
    :return: (str) la ville de plus petite distance avec la ville actuelle '''
    
    min_distance = float('inf')  # la distance minimale actuelle est définie à l'infini
    ville_suivante = None  # la ville suivante est initialement non définie (None)
    for ville in villes_restantes:  # pour chaque ville parmi les villes restantes à parcourir
        distance = villes[ville_actuelle][ville]  # on récupère la distance entre cette ville et la ville actuelle
        if distance < min_distance:  # si la distance est plus petite que le minimum actuellement stocké
            min_distance = distance  # on remplace la distance minimale par cette distance
            ville_suivante = ville  # on remplace la ville suivante par cette ville
    return ville_suivante  # on renvoie la ville que l'on a finalement déterminé

def voyageur(villes, ville_depart):
    ''' Résolution du problème du voyageur de commerce.
    :param villes: (dict[dict]) dictionnaire des villes et distances
    :param ville_depart: (str) la ville de départ
    :return: (tuple) tuple contenant le trajet effectué (list[str]) et la distance totale parcourue (int) '''
    
    trajet = [ville_depart]  # le trajet effectué contient au début seulement la ville de départ
    distance_totale = 0  # la distance totale parcourue est initialement de 0 km
    ville_actuelle = ville_depart  # la ville actuellement parcourue est la ville de départ
    villes_restantes = [ville for ville in villes if ville != ville_depart]  # récupérer les villes restantes à parcourir

    while villes_restantes:  # tant qu'il reste des villes à parcourir
        prochaine_ville = trouver_ville_suivante(ville_actuelle, villes_restantes, villes)  # on récupère la prochaine ville à parcourir
        trajet.append(prochaine_ville)  # on ajoute la ville choisie au trajet
        distance_totale += villes[ville_actuelle][prochaine_ville]  # on ajouter la distance entre la ville actuelle
                                                                    # et la prochaine ville à la distance totale
        ville_actuelle = prochaine_ville  # la "prochaine ville" devient la ville actuellement parcourue
        villes_restantes.remove(ville_actuelle)  # on supprime la prochaine ville des villes restantes à parcourir

    # Retourner à la ville de départ
    trajet.append(ville_depart)  # on revient sur la ville de départ
    distance_totale += villes[ville_actuelle][ville_depart]  # on ajoute à la distance totale la distance
                                                              # entre la dernière ville et la ville de départ

    return trajet, distance_totale  # enfin, on renvoie le trajet déterminé et la distance correspondante

def creer_dict(villes, distances):
    d = {}
    for i in range(len(distances)):
        d[villes[i]] = {}
        for j in range(len(distances)):
            d[villes[i]][villes[j]] = distances[i][j]
    return d

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