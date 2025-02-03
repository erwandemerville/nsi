def lire_fichier(fichier, delimiteur=","):
    '''Crée une table de données à partir d'un fichier.
    :param fichier: (str) Le chemin vers un fichier txt ou csv.
    :param delimiteur: (str) Le séparateur des éléments d'une ligne (par défaut une virgule).
    :return (list of dicts): Retourne une liste de dictionnaires.
    
    :CU: Le fichier doit contenir des données.'''
    
    f = open(fichier, "r")                    # Ouvrir en mode de lecture
    cles = f.readline()                       # Lire la première ligne pour récupérer les clés
    cles = cles.rstrip("\n")                  # Retirer le "\n" en fin de ligne
    cles = cles.split(delimiteur)             # Découper la ligne en plusieurs éléments selon le délimiteur
    lignes = f.readlines()                    # Stocker toutes les autres lignes du fichier
    table = [{} for _ in range(len(lignes))]  # Créer une liste de dictionnaires
    for i in range(len(lignes)):              # Pour chaque ligne...
        lignes[i] = lignes[i].rstrip("\n")
        t = lignes[i].split(delimiteur)
        for j in range(len(t)):               # Ajouter les éléments de la ligne dans un dictionnaire de table...
            table[i][cles[j]]=t[j]
    f.close()                                 # Refermer le fichier
    return table                              # Renvoyer la table

def ecrire_fichier(table, fichier, delimiteur=","):
    '''Crée un fichier à partir d'une table de données.
    :param table: (list of dicts) La table de données à exporter.
    :param fichier: (str) Fichier txt ou csv à créer.
    :param delimiteur: (str) Le séparateur à ajouter entre les éléments d'une ligne (par défaut une virgule).
    
    :CU: La table doit contenir des données.
    Eviter de choisir le point ou "\n" comme délimiteur.'''
    
    f = open(fichier, "w")                    # Ouvrir en mode de écriture
    cles = [cle for cle in table[0]]          # Créer une liste des attributs de la table de données
    f.write(f"{delimiteur.join(cles)}\n")     # Ecrire en première ligne les clés et ajouter un retour à la ligne
    for i in range(len(table)):
        t = [val for cle, val in table[i].items()] # Récupérer les valeurs de la ligne dans une liste
        f.write(f"{delimiteur.join(t)}\n")
    f.close()

# VOTRE PROGRAMME
# 1 - Lire le fichier exemple.csv
table = ...
# 2 - Créer un nouveau dictionnaire avec vos informations
infos = {}
# 3 - Ajouter ce dictionnaire à la liste table
...
# 4 - Créer le nouveau fichier CSV
...