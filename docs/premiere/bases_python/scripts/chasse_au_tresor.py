import tkinter as tk  # Importer le module tkinter, utiliser l'alias tk
from random import randint  # Importer la fonction randint du module random

# ============================================================
# ===================> VARIABLES GLOBALES <===================
# ============================================================

N = 5  # Constante définissant la taille de la grille

# Coordonnées du trésor (choisies aléatoirement au début du jeu)
# À COMPLÉTER
TRESOR_X = randint(...)
TRESOR_Y = randint(...)

# Variables pour stocker la position de la dernière case cliquée par le joueur (initialement None)
derniere_pos_x = None
derniere_pos_y = None

# Compteur de tentatives (initialement 0)
tentatives = 0

# ============================================================
# ===============> INITIALISATION ZONE DE JEU <===============
# ============================================================

# Création de la fenêtre principale du jeu
root = tk.Tk()  # Créer la fenêtre de jeu initiale (vide)
root.title("Chasse au trésor")  # Ajouter un titre à la fenêtre de jeu

# Création de la grille de boutons dans la fenêtre de jeu
# À COMPLÉTER
boutons = []  # Liste de listes (tableau) permettant de stocker tous les boutons
for i in range(...):  # On itère N fois pour créer les N lignes de la grille de boutons
    ligne = []  # Liste permettant de stocker les boutons d'une ligne
    for j in range(...):  # On itère N fois pour créer les N colonnes de la grille de boutons
        # Création d'un bouton qui appelle la fonction verifier_case lors d'un clic :
        btn = tk.Button(root, text="", width=10, height=3, command=lambda i=i, j=j: verifier_case(i, j))
        # Positionner le bouton aux coordonnées (i, j) :
        btn.grid(row=i, column=j)
        # Ajouter le bouton btn dans la liste ligne :
        ligne.append(btn)
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
    :return: (None) cette fonction ne renvoie rien

    À COMPLÉTER. '''

    # Permettre la modifications des variables globales
    global tentatives, derniere_pos_x, derniere_pos_y

    # Incrémentation du compteur de tentatives (on l'augmente de 1)
    tentatives += ...

    # Calcul de la distance entre la case cliquée et le trésor,
    # vous devez appeler la fonction calculer_distance
    distance_actuelle = ...

    if ... == ...:  # Si la distance actuelle est de 0, le joueur a trouvé le trésor
        # On crée un message de victoire
        texte_victoire = f"Bravo ! Vous avez trouvé le trésor en {...} tentatives !"

        # Afficher le message avec tkinter et changer la couleur de fond du bouton
        message_label.config(text=texte_victoire)
        boutons[x][y].config(bg="pale green")

        # Désactiver tous les boutons après la victoire
        ...  # Vous devez appeler la fonction desactiver_boutons
    else:  # Sinon
        if ...:  # Si ce n'est pas la première tentative
            # Calculer la distance entre la dernière case cliquée et le trésor :
            distance_precedente = ...

            if ...: # Si la distance actuelle est plus petite que la distance précédente
                message = ...  # Créer le message "Plus proche !"
                message_label.config(text=message)  # Afficher le message créé
            else:
                message = ...  # Créer le message "Plus loin !"
                message_label.config(text=message)  # Afficher le message créé
        else:  # Sinon
            message = ...  # Créer le message "Première tentative !"
            message_label.config(text=message)  # Afficher le message créé

        # Mise à jour de l'apparence du bouton cliqué (changement texte et couleur)
        boutons[x][y].config(bg="cyan", text=f"{tentatives}")

        # Mise à jour des coordonnées de la dernière position du joueur,
        # on les remplace par les coordonnées de la case cliquée
        derniere_pos_x = ...
        derniere_pos_y = ...

def calculer_distance(x1, y1, x2, y2):
    ''' Fonction qui renvoie la distance de Manhattan entre deux points (x1, y1) et (x2, y2).
    La distance de Manhattan est la somme des distances absolues des coordonnées.
    :param x1: (int) coordonnée en x du point 1.
    :param y1: (int) coordonnée en y du point 1.
    :param x2: (int) coordonnée en x du point 2.
    :param y2: (int) coordonnée en y du point 2.
    :return: (int) distance de Manhattan entre les deux points.
    
    À COMPLÉTER. '''

    return ...

def desactiver_boutons():
    ''' Désactiver tous les boutons de la grille après avoir trouvé le trésor.
    :return: (None) cette fonction ne renvoie rien '''
    
    for ligne in boutons:  # Pour chaque ligne de la grille de boutons
        for btn in ligne:  # Pour chaque bouton de la ligne
            btn.config(state=tk.DISABLED)  # Désactiver le bouton (le rendre non cliquable)

# ============================================================
# ===================> BOUCLE PRINCIPALE <====================
# ============================================================

root.mainloop()  # Boucle principale de l'interface