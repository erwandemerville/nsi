import tkinter as tk
from random import randint

N = 5  # Variable globale définissant la taille de la grille

# Fenêtre principale
root = tk.Tk()
root.title("Chasse au trésor")

# Création de la grille de boutons
# À COMPLÉTER
boutons = []  # Liste de listes pour stocker tous les boutons
for i in range(...):  # On itère N fois pour créer N lignes
    ligne = []  # Liste pour stocker les boutons d'une ligne
    for j in range(...):  # On itère N fois pour créer N colonnes
        btn = tk.Button(root, text="", width=10, height=3, command=lambda i=i, j=j: verifier_case(i, j))
        btn.grid(row=i, column=j)  # Positionner le bouton aux coordonnées (i, j)
        ligne.append(btn)  # Ajouter le bouton btn à la liste ligne
    boutons.append(ligne)  # Ajouter la ligne de boutons à la liste de listes boutons

# Coordonnées du trésor (choisies aléatoirement au début du jeu)
# À COMPLÉTER
tresor_x = randint(...)
tresor_y = randint(...)

# Variables pour stocker la dernière position du joueur (initialement None)
derniere_pos_x = None
derniere_pos_y = None

# Compteur de tentatives (initialement 0)
tentatives = 0

# Zone d'affichage des messages (indices et victoire)
message_label = tk.Label(root, text="Trouvez le trésor caché !", font=("Helvetica", 14))
message_label.grid(row=N, column=0, columnspan=N)  # Afficher le message tout en bas, centré

def verifier_case(x, y):
    '''
    Fonction appelée lorsqu'on clique sur une case.
    :param x: coordonnée en x de la case cliquée.
    :param y: coordonnée en y de la case cliquée.

    À COMPLÉTER.
    '''

    # Permettre la modifications de certaines variables globales
    global tentatives, derniere_pos_x, derniere_pos_y

    # Incrémentation du compteur de tentatives (on l'augmente de 1)
    tentatives += ...

    # Calcul de la distance entre la case cliquée et le trésor,
    # vous devez appeler la fonction calculer_distance
    distance_actuelle = ...

    if ... == ...:  # Si la distance actuelle est de 0, le joueur a trouvé le trésor
        # On affiche un message de victoire
        texte_victoire = f"Bravo ! Vous avez trouvé le trésor en {...} tentatives !"

        # Afficher le message avec tkinter et changer la couleur de fond du bouton
        message_label.config(text=texte_victoire)
        boutons[x][y].config(bg="green")

        # Désactiver tous les boutons après la victoire
        desactiver_boutons()
    else:  # Sinon
        if ...:  # Si ce n'est pas la première tentative
            # Récupérer distance entre la dernière position et le trésor avec calculer_distance :
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

        # Mise à jour de l'apparence du bouton cliqué
        boutons[x][y].config(bg="blue", text=f"{tentatives}")

        # Mise à jour des coordonnées de la dernière position du joueur,
        # on les remplace par les coordonnées de la case cliquée
        derniere_pos_x = ...
        derniere_pos_y = ...

def calculer_distance(x1, y1, x2, y2):
    '''
    Fonction qui renvoie la distance de Manhattan entre deux points (x1, y1) et (x2, y2).
    La distance de Manhattan est la somme des distances absolues des coordonnées.
    :param x1: coordonnée en x du point 1.
    :param y1: coordonnée en y du point 1.
    :param x2: coordonnée en x du point 2.
    :param y2: coordonnée en y du point 2
    
    À COMPLÉTER.
    '''

    return ...

def desactiver_boutons():
    '''Désactiver tous les boutons de la grille après avoir trouvé le trésor.
    RIEN À COMPLÉTER DANS CETTE FONCTION. '''
    
    for ligne in boutons:
        for btn in ligne:
            btn.config(state=tk.DISABLED)

# Boucle principale de l'interface
root.mainloop()