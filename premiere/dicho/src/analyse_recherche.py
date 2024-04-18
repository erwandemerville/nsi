import time
import matplotlib.pyplot as plt

def recherche_naive(tableau, element):
    ''' Renvoie True si element est trouvé, False sinon.
    :param tableau: (list[int]) une liste d'éléments
    :param element: (int) l'élément à rechercher
    :return (bool): True ou False '''
    comps = 0  # Variable pour compter le nombre de comparaisons
    for el in tableau:
        comps += 1
        if element == el:
            return True, comps
    return False, comps

def recherche_dicho(tableau, element):
    ''' Effectue une recherche dichotomique dans un tableau.
    Renvoie True si element est trouvé, False sinon. '''
    comps = 0  # Variable pour compter le nombre de comparaisons
    debut = 0
    fin = len(tableau) - 1
    trouve = False
    while not trouve and debut <= fin:
        milieu = (debut + fin) // 2
        comps += 1
        if tableau[milieu] == element:
            trouve = True
        else:
            if element > tableau[milieu]:
                debut = milieu + 1
            else:
                fin = milieu - 1
    return trouve, comps

def courbes_comp(p):
    sizes = [2**i for i in range(p)]
    naive_comps = []
    dichotomy_comps = []

    for size in sizes:
        # Création du tableau et de l'élément à rechercher
        tableau = list(range(size))
        element = size

        # Recherche naïve
        _, naive_comp = recherche_naive(tableau, element)
        naive_comps.append(naive_comp)

        # Recherche dichotomique
        _, dichotomy_comp = recherche_dicho(tableau, element)
        dichotomy_comps.append(dichotomy_comp)

    # Affichage des courbes
    plt.plot(sizes, naive_comps, label='Recherche séquentielle')
    plt.plot(sizes, dichotomy_comps, label='Recherche dichotomique')
    plt.xlabel('Taille du tableau')
    plt.ylabel('Nombre de comparaisons')
    plt.title('Comparaison des méthodes de recherche')
    plt.legend()
    plt.show()

def courbes_temps(p):
    powers_of_two = [2 ** i for i in range(p)]  # Tailles de tableau de 2^0 à 2^p
    naive_times = []
    dichotomy_times = []

    for size in powers_of_two:
        # Création du tableau et de l'élément à rechercher
        tableau = list(range(size))
        element = size

        # Recherche naïve
        start_time = time.time()
        recherche_naive(tableau, element)
        end_time = time.time()
        naive_times.append(end_time - start_time)

        # Recherche dichotomique
        start_time = time.time()
        recherche_dicho(tableau, element)
        end_time = time.time()
        dichotomy_times.append(end_time - start_time)

    # Affichage des courbes
    plt.plot(powers_of_two, naive_times, label='Recherche séquentielle')
    plt.plot(powers_of_two, dichotomy_times, label='Recherche dichotomique')
    plt.xlabel('Taille du tableau (2^N)')
    plt.ylabel('Temps d\'exécution (s)')
    plt.title('Comparaison des temps d\'exécution')
    plt.legend()
    plt.show()

def nb_comps(p):
    sizes = [2**i for i in range(p)]
    print("Taille N\tRecherche séquentielle\tRecherche dichotomique")
    for size in sizes:
        tableau = list(range(size))
        element = size
        naive_found, naive_comp = recherche_naive(tableau, element)
        dichotomy_found, dichotomy_comp = recherche_dicho(tableau, element)
        print(f"{size}\t\t{naive_comp}\t\t\t{dichotomy_comp}")

if __name__ == "__main__":
    ''' Exemples d'utilisation.
    Les valeurs données en entrées des fonctions permettent d'indiquer la taille max souhaitée pour les tableaux générés.
    Le tableau prendra ainsi les tailles N = 2^0, 2^1, ..., 2^p, où p est le nombre donné en entrée.
    Attention, un nombre trop grand peut amener à un temps d'exécution important. '''
    
    courbes_comp(6)  # affiche les courbes d'évolution du nombre de comparaisons effectuées
    courbes_temps(15)  # affiche les courbes d'évolution de la mesure du temps d'exécution
    nb_comps(10)  # affiche dans la console un tableau des nombres de comparaisons effectuées
