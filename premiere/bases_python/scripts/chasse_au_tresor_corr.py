import tkinter as tk  # Importer le module tkinter, utiliser l'alias tk
from random import randint  # Importer la fonction randint du module random

# ============================================================
# ===================> VARIABLES GLOBALES <===================
# ============================================================

N = 5  # Constante définissant la taille de la grille

# Coordonnées du trésor (choisies au hasard au début du jeu) en fonction de la taille N
# Note : En Python, les indices des cases d'un tableau commencent à partir de 0, et non pas de 1.
# Pour un tableau de taille 5x5, les coordonnées en x et en y seront donc comprises entre 0 et 4.
TRESOR_X = randint(0, N-1)  # On génère une coordonnée aléatoire entre 0 et N-1
TRESOR_Y = randint(0, N-1)  # On génère une coordonnée aléatoire entre 0 et N-1

# Variables pour stocker la position de la dernière case cliquée par le joueur (initialement None)
derniere_pos_x = None
derniere_pos_y = None

# Compteur de tentatives
tentatives = 0

# ============================================================
# ===============> INITIALISATION ZONE DE JEU <===============
# ============================================================

# Fenêtre principale
root = tk.Tk()  # Créer la fenêtre de jeu initiale
root.title("Chasse au trésor")  # Ajouter un titre à la fenêtre de jeu

# Création de la grille de boutons dans la fenêtre de jeu
boutons = []  # Liste de listes (tableau) permettant de stocker tous les boutons
for i in range(N):  # On itère N fois pour créer les N lignes de la grille de boutons
    ligne = []  # Liste permettant de stocker les boutons d'une ligne
    for j in range(N):  # On itère N fois pour créer les N colonnes de la grille de boutons
        # Création d'un bouton qui appelle la fonction verifier_case lors d'un clic :
        btn = tk.Button(root, text="", width=10, height=3, command=lambda i=i, j=j: verifier_case(i, j))
        # Positionner le bouton aux coordonnées (i, j) :
        btn.grid(row=i, column=j)
        # Ajouter le bouton btn dans la liste ligne :
        ligne.append(btn)  # append permet d'ajouter le bouton btn à la liste ligne
    boutons.append(ligne)  # Ajouter enfin la ligne de boutons à la liste de listes boutons

# Création du message initial à afficher en bas de la fenêtre de jeu
# Ce message sera modifié par la fonction verifier_case
message_label = tk.Label(root, text="Trouvez le trésor caché !", font=("Helvetica", 14))
# Placer le message à la ligne N (donc après les boutons), à la colonne 0, et en prenant N colonnes
message_label.grid(row=N, column=0, columnspan=N)  # Le message sera affiché tout en bas et centré

# ============================================================
# =======================> FONCTIONS <========================
# ============================================================

def verifier_case(x, y):
    ''' Fonction appelée lorsqu'on clique sur une case.
    :param x: (int) coordonnée en x de la case cliquée
    :param y: (int) coordonnée en y de la case cliquée
    :return: (None) cette fonction ne renvoie rien '''

    # Permettre la modifications des variables globales
    global tentatives, derniere_pos_x, derniere_pos_y

    # Incrémentation du compteur de tentatives
    tentatives += 1

    # Calcul de la distance entre la case cliquée et le trésor
    distance_actuelle = calculer_distance(x, y, TRESOR_X, TRESOR_Y)

    if distance_actuelle == 0: # Si la distance est 0, le joueur a trouvé le trésor
        # On crée un message de victoire
        texte_victoire = f"Bravo ! Vous avez trouvé le trésor en {tentatives} tentatives !"

        # Afficher le message avec tkinter et changer la couleur de fond du bouton
        message_label.config(text=texte_victoire)
        boutons[x][y].config(bg="pale green")

        # Désactiver tous les boutons après la victoire
        desactiver_boutons()
    else:  # Sinon
        # Si ce n'est pas la première tentative :
        if derniere_pos_x is not None and derniere_pos_y is not None:
            # Calculer la distance entre la dernière case cliquée et le trésor :
            distance_precedente = calculer_distance(derniere_pos_x, derniere_pos_y, TRESOR_X, TRESOR_Y)
            
            #  Si la distance actuelle est plus petite que la distance précédente
            if distance_actuelle < distance_precedente:
                message = f"Plus proche !"  # Créer le message "Plus proche !"
                message_label.config(text=message)  # Afficher le message créé
            else:
                message = f"Plus loin !"  # Créer le message "Plus loin !"
                message_label.config(text=message)  # Afficher le message créé
        else:
            message = "Première tentative !"  # Créer le message "Première tentative !"
            message_label.config(text=message)  # Afficher le message créé

        # Mise à jour de l'apparence du bouton cliqué (changement texte et couleur)
        boutons[x][y].config(bg="cyan", text=f"{tentatives}")

        # Mise à jour des coordonnées de la dernière position du joueur,
        # on les remplace par les coordonnées de la case cliquée
        derniere_pos_x = x
        derniere_pos_y = y

        # Désactiver tous les boutons sur lesquels le joueur a cliqué :
        desactiver_boutons_cliques()

def calculer_distance(x1, y1, x2, y2):
    ''' Fonction qui renvoie la distance de Manhattan entre deux points (x1, y1) et (x2, y2).
    La distance de Manhattan est la somme des distances absolues des coordonnées.
    :param x1: (int) coordonnée en x du point 1
    :param y1: (int) coordonnée en y du point 1
    :param x2: (int) coordonnée en x du point 2
    :param y2: (int) coordonnée en y du point 2
    :return: (int) distance de Manhattan entre les deux points '''

    return abs(x1 - x2) + abs(y1 - y2)

def desactiver_boutons():
    ''' Désactiver tous les boutons de la grille après avoir trouvé le trésor.
    :return: (None) cette fonction ne renvoie rien '''

    for ligne in boutons:  # Pour chaque ligne de la grille de boutons
        for btn in ligne:  # Pour chaque bouton de la ligne
            btn.config(state=tk.DISABLED)  # Désactiver le bouton (le rendre non cliquable)

def desactiver_boutons_cliques():
    ''' Désactiver tous les boutons sur lesquels le joueur a cliqué. 
    :return: (None) cette fonction ne renvoie rien '''

    for ligne in boutons:
        for btn in ligne:
            if btn.cget('text') != "":
                btn.config(state=tk.DISABLED)

# ============================================================
# ===================> BOUCLE PRINCIPALE <====================
# ============================================================

root.mainloop()  # Boucle principale de l'interface