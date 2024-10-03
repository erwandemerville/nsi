import tkinter as tk
from random import randint

N = 5  # Variable globale définissant la taille de la grille

# Fenêtre principale
root = tk.Tk()
root.title("Chasse au trésor")

# Création de la grille de boutons
boutons = []  # Liste de listes pour stocker tous les boutons
for i in range(N):  # On itère N fois pour créer N lignes
    ligne = []  # Liste pour stocker les boutons d'une ligne
    for j in range(N):  # On itère N fois pour créer N colonnes
        btn = tk.Button(root, text="", width=10, height=3, command=lambda i=i, j=j: verifier_case(i, j))
        btn.grid(row=i, column=j)  # Positionner le bouton aux coordonnées (i, j)
        ligne.append(btn)  # Ajouter le bouton btn à la liste ligne
    boutons.append(ligne)  # Ajouter la ligne de boutons à la liste de listes boutons

# Coordonnées du trésor (choisies au hasard au début du jeu)
tresor_x = randint(0, N-1)
tresor_y = randint(0, N-1)

# Variables pour stocker la dernière position du joueur
derniere_pos_x = None
derniere_pos_y = None

# Compteur de tentatives
tentatives = 0

# Zone d'affichage des messages (indices et victoire)
message_label = tk.Label(root, text="Trouvez le trésor caché !", font=("Helvetica", 14))
message_label.grid(row=N, column=0, columnspan=N)  # Afficher le message tout en bas, centré

def verifier_case(x, y):
    '''
    Fonction appelée lorsqu'on clique sur une case.
    :param x: coordonnée en x de la case cliquée.
    :param y: coordonnée en y de la case cliquée.
    '''

    # Permettre la modifications de certaines variables globales
    global tentatives, derniere_pos_x, derniere_pos_y

    # Incrémentation du compteur de tentatives
    tentatives += 1

    # Calcul de la distance entre la case cliquée et le trésor
    distance_actuelle = calculer_distance(x, y, tresor_x, tresor_y)

    if distance_actuelle == 0:
        # Si la distance est 0, le joueur a trouvé le trésor
        message_label.config(text=f"Bravo ! Vous avez trouvé le trésor en {tentatives} tentatives !")
        boutons[x][y].config(bg="green")
        # Désactiver tous les boutons après la victoire
        desactiver_boutons()
    else:
        # Si ce n'est pas la première tentative, comparer avec la distance précédente
        if derniere_pos_x is not None and derniere_pos_y is not None:
            distance_precedente = calculer_distance(derniere_pos_x, derniere_pos_y, tresor_x, tresor_y)
            if distance_actuelle < distance_precedente:
                message_label.config(text="Plus proche !")
            else:
                message_label.config(text="Plus loin !")
        else:
            message_label.config(text="Première tentative !")

        # Mise à jour de l'apparence du bouton cliqué
        boutons[x][y].config(bg="blue", text=f"{tentatives}")

        # Mise à jour des coordonnées de la dernière tentative
        derniere_pos_x, derniere_pos_y = x, y

def calculer_distance(x1, y1, x2, y2):
    '''
    Fonction qui renvoie la distance de Manhattan entre deux points (x1, y1) et (x2, y2).
    La distance de Manhattan est la somme des distances absolues des coordonnées.
    :param x1: coordonnée en x du point 1.
    :param y1: coordonnée en y du point 1.
    :param x2: coordonnée en x du point 2.
    :param y2: coordonnée en y du point 2.
    '''

    return abs(x1 - x2) + abs(y1 - y2)

def desactiver_boutons():
    '''Désactiver tous les boutons de la grille après avoir trouvé le trésor.'''

    for ligne in boutons:
        for btn in ligne:
            btn.config(state=tk.DISABLED)

# Boucle principale de l'interface
root.mainloop()