''' Script Python permettant la manipulation de tables. '''
import csv

# Variables globales
FICHIER_ENTREE = 'fr-en-effectifs-specialites-doublettes-terminale-generale.csv'
FICHIER_SORTIE = 'mon_fichier.csv'

def lire_csv(fichier=FICHIER_ENTREE, delim=';'):
    '''Créer une table de données à partir d'un fichier.
    :param fichier: (str) Chemin vers un fichier CSV ou TXT.
    :param delim: (str) Délimiteur (Facultatif, ne spécifier que si différent d'une virgule).
    :return (list of dicts): Retourne une liste de dictionnaires.'''
    
    fichier = open(fichier, newline='', encoding='utf-8-sig')
    lecteur = csv.DictReader(fichier, delimiter=delim)  # Création d'un objet lecteur de classe DictReader
    return [dict(ligne) for ligne in lecteur]  # Création d'une liste de dictionnaires par compréhension

def creer_csv(table, fichier=FICHIER_SORTIE, delim=';', ordre=None):
    '''Créer un fichier à partir d'une table de données.
    :param table: (list of dicts) La table de données à exporter.
    :param fichier: (str) Fichier CSV ou TXT à créer.
    :param delim: (str) Délimiteur (Facultatif, ne spécifier que si différent d'une virgule).
    :param ordre: (list de str) Attributs dans l'ordre souhaité (facultatif).'''
    
    if not ordre:  # Si l'ordre des attributs n'est pas spécifié, défini par défaut.
        ordre = [key for key in table[0]]
        
    with open(fichier, 'w', encoding='utf-8-sig') as fic:
        dic = csv.DictWriter(fic, fieldnames=ordre, delimiter=delim)  # Création d'un objet dic de classe DictWriter
        dic.writeheader()  # Écrire la première ligne, celle des attributs
        for ligne in table:  # Pour chaque enregistrement de la table :
            dic.writerow(ligne)  # Écrire les lignes contenant les données de la table


# Manipulation de tables (à compléter)

def creer_table_classe():
    ''' Crée une table dans un fichier CSV contenant le nom, le prénom, l'âge et la classe
    de chaque élève de première NSI.
    :return: (None) la fonction ne renvoie rien, elle crée juste un fichier CSV '''

    # On crée la table sous la forme d'une liste de dictionnaires.
    # Pour simplifier, je n'ai mis que 3 personnes de la classe.
    # Vous pouvez ajouter les autres personnes si vous le souhaitez.
    nouvelle_table = [{'Nom': 'BALLESTER',
                       'Prenom': 'Colin',
                       'Age': '16',
                       'Classe': '1G4'},
                      {'Nom': 'BELMOKHTAR',
                       'Prenom': 'Rahma',
                       'Age': '20',
                       'Classe': '1G4'},
                      {'Nom': 'SAADA',
                       'Prenom': 'Marc',
                       'Age': '16',
                       'Classe': '1G3'}]
    
    # Création d'un fichier eleves.csv à partir de nouvelle_table
    creer_csv(nouvelle_table, fichier="eleves.csv")

def lister_colonnes(table):
    ''' Prend une table en entrée et renvoie une liste contenant ses attributs.
    :param table: (list of dicts) une liste de dictionnaires
    :return: (list) liste des attributs de la table.
    :Exemples:
    >>> table = lire_csv()
    >>> lister_colonnes(table)
    ["RENTREE SCOLAIRE", "REGION ACADEMIQUE", "ACADEMIE", ...] '''

    liste = []  # initialiser une liste vide
    for cle in table[0]:  # pour chaque clé (correspondant à un attribut) du premier dictionnaire de "table"
        liste.append(cle)  # on ajoute la clé à la liste "liste"
    return liste  # on renvoie la liste des attributs

# EXERCICE 3 - Fonctions à compléter
# Les fonctions suivantes concernent la table du fichier fr-en-effectifs-specialites-doublettes-terminale-generale.csv

def chercher_academie(table, academie):
    ''' Renvoie True si le nom de l'académie donné est présent dans la table, False sinon.
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :return: (bool) True ou False
    :Exemples:
    >>> table = lire_csv()
    >>> chercher_academie(table, 'GRENOBLE')
    True
    >>> chercher_academie(table, 'PETAOUCHNOK')
    False
    
    Vous pouvez effectuer les tests ci-dessus pour vérifier le bon fonctionnement de votre fonction. '''
    
    for ligne in table:  # pour chaque enregistrement de la table (chaque élément étant un dictionnaire)
        if ligne["ACADEMIE"] == academie:  # si la valeur associée à la clé "ACADEMIE" est celle qui est recherchée
            return True  # on renvoie True
    return False  # si on n'a pas trouvé l'académie recherchée, on renvoie False

def effectif_total_terminale(table, numero_etablissement, annee):
    ''' Renvoie l' "EFFECTIF TOTAL EN TERMINALE GENERALE" de l'établissement dont le "NUMERO ETABLISSEMENT" est donné.
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :param annee: (str) Une année "2020" ou "2021"
    :param numero_etablissement: (str) le numéro associé à un établissement

    Faites le test avec le "LYCEE JEAN PERRIN" dont le "NUMERO ETABLISSEMENT" est "0590110Z". '''
    
    for ligne in table:  # pour chaque enregistrement de la table (chaque élément étant un dictionnaire)
        if ligne["NUMERO ETABLISSEMENT"] == numero_etablissement and \
           ligne["RENTREE SCOLAIRE"] == annee:  # si le numéro d'établissement et la rentrée scolaire correspondent à ceux recherchés
            return ligne["EFFECTIF TOTAL EN TERMINALE GENERALE"]  # on renvoie l'effectif total des élèves en Tle générale

def effectif_total_eleves_nsi(table, numero_etablissement, rentree):
    ''' Renvoie la somme des effectifs garçons ("0747 - NUMERIQUE ET SCIENCES INFORMATIQUES - garcons")
    + filles ("0747 - NUMERIQUE ET SCIENCES INFORMATIQUES - filles") en NSI pour une "RENTREE SCOLAIRE" (année) donnée,
    et pour un "NUMERO ETABLISSEMENT" donné.
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :param numero_etablissement: (str) le numéro associé à un établissement
    :param rentree: (str) la rentrée scolaire souhaitée
    
    Faites le test avec le "LYCEE JEAN PERRIN" pour la "RENTREE SCOLAIRE" 2020, dont le "NUMERO ETABLISSEMENT" est "0590110Z". '''
    
    for ligne in table:
        if ligne["RENTREE SCOLAIRE"] == rentree and \
           ligne["NUMERO ETABLISSEMENT"] == numero_etablissement:
            return int(ligne["0747 - NUMERIQUE ET SCIENCES INFORMATIQUES - garcons"]) + \
                   int(ligne["0747 - NUMERIQUE ET SCIENCES INFORMATIQUES - filles"])

def compter_lycees_generaux(table):
    ''' Renvoie le nombre de lycées généraux.
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :return: (int) le nombre de lycées dont 'DENOMINATION' = 'LYCEE GENERAL'
    '''
    
    total = 0  # on initialise une variable "total" à 0
    for ligne in table:  # pour chaque enregistrement de la table (chaque élément étant un dictionnaire)
        if ligne["DENOMINATION"] == "LYCEE GENERAL":  # si la valeur associée à la clé "DENOMINATION" est "LYCEE GENERAL"
            total += 1  # on incrémente (c'est-à-dire qu'on ajoute 1) au total
    return total  # on renvoie la valeur de la variable "total"

def moyenne_garcons_nsi(table, region):
    ''' Renvoie la moyenne des effectifs de garçons en NSI ("0747 - NUMERIQUE ET SCIENCES INFORMATIQUES - garcons"),
    dans les lycées dont la "REGION ACADEMIQUE" est donnée.
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :param region: (str) la région pour laquelle calculer la moyenne
    :return: (float) la moyenne des effectifs de garçons en NSI
    
    Faites le test avec la "REGION ACADEMIQUE" des "HAUTS-DE-FRANCE". '''
    
    # même principe que la fonction précédente, mais il faut compter le nombre de lycée
    # pour pouvoir calculer la moyenne
    total = 0
    nb_lycees = 0
    for ligne in table:  # pour chaque enregistrement de la table
        if ligne["REGION ACADEMIQUE"] == region:  # si la région académique du lycée courant est celle qui est recherchée
            total += ligne["0747 - NUMERIQUE ET SCIENCES INFORMATIQUES - garcons"]  # on ajoute l'effectif de garçons en NSI au total
            nb_lycees += 1  # on incrémente le compteur de lycées
    return total / nb_lycees  # on renvoie la moyenne en divisant le total par le nombre de lycées

def lycees_academie(table, academie, fichier=FICHIER_SORTIE):
    ''' Crée une nouvelle table contenant uniquement les enregistrements dont l' "ACADEMIE" est donnée,
    puis enregistre cette table dans le fichier CSV spécifié (qui est initialisé à FICHIER_SORTIE).
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :param academie: (str) l'académie dont on veut garder les enregistrements.
    :param fichier: (str) le fichier de sortie (initialement égal au contenu de la variable globale FICHIER_SORTIE)
    :return: (None) on ne renvoie rien (on crée simplement un nouveau fichier CSV)

    Faites le test pour l' "ACADEMIE" de "LILLE". '''
    
    nouvelle_table = []  # créer une nouvelle table (on initialise à une liste vide)
    for ligne in table:  # pour chaque enregistrement de "table"
        if ligne["ACADEMIE"] == academie:  # si l'académie du lycée courant est celle qui est recherchée
            nouvelle_table.append(ligne)  # on ajoute la ligne dans notre nouvelle table
    creer_csv(nouvelle_table)  # enfin, on crée le nouveau fichier CSV ne contenant que les académies souhaitées

# EXERCICE 4 - Fonctions à compléter
# Les fonctions suivantes concernent la table du fichier fr-en-effectifs-specialites-doublettes-terminale-generale.csv

def patronyme(e):
    ''' FONCTION UTILITAIRE POUR LA FONCTION "trier_selon_patronyme"
    Prend un enregistrement de la table et renvoie la valeur associée à "PATRONYME". '''
    
    return e["PATRONYME"] 

def trier_selon_patronyme(table):
    ''' Trier la table de donnée par rapport à la colonne "PATRONYME".
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :return: (list of dicts) renvoie une nouvelle table de données triée par rapport au patronyme des lycées '''

    table_triee = sorted(table, key=patronyme)  # sorted renvoie une table triée à partir de "table", la clé est la fonction "patronyme"
    return table_triee  # on renvoie la table triée

def effectif(e):
    '''FONCTION UTILITAIRE POUR LA FONCTION "trier_selon_effectif"
    Prend un enregistrement de la table et renvoie la valeur associée à "EFFECTIF TOTAL EN TERMINALE GENERALE". '''
    
    return e["EFFECTIF TOTAL EN TERMINALE GENERALE"]

def trier_selon_effectif(table):
    ''' Trier la table de donnée par rapport à la colonne "EFFECTIF TOTAL EN TERMINALE GENERALE".
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :return: (list of dicts) renvoie une nouvelle table de données triée par rapport à l'effectif total en terminale générale '''

    table_triee = sorted(table, key=effectif)  # ici, on trie "table" en utilisant comme clé la fonction "effectif"
    return table_triee

def academie_puis_effectif(e):
    ''' Prend un enregistrement de la table et renvoie un tuple de deux valeurs associées aux champs : 
    "ACADEMIE" et "EFFECTIF TOTAL EN TERMINALE GENERALE". '''
    
    return e["ADADEMIE"], e["EFFECTIF TOTAL EN TERMINALE GENERALE"]

def trier_selon_academie_et_effectif(table):
    ''' Trier la table de donnée par rapport à la colonne "ACADEMIE" et "EFFECTIF TOTAL EN TERMINALE GENERALE".
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :return: (list of dicts) renvoie une nouvelle table de données triée par rapport à l'académie ET l'effectif total en terminale générale '''
    
    table_triee = sorted(table, key=academie_puis_effectif)
    return table_triee

# EXERCICE 4 - Fonctions à compléter

def fusionner_deux_tables(table1, table2):
    ''' Fusionner deux tables de données.
    :param table1: (list of dicts) une table sous la forme d'une liste de dictionnaires
    :param table2: (list of dicts) une table sous la forme d'une liste de dictionnaires
    :return: (list of dicts) une table sous la forme d'une liste de dictionnaires '''

    # Les deux tables sont des listes :
    # il suffit donc de faire une concaténation (avec le `+`) pour fusionner les deux tables.
    return table1 + table2

    # ATTENTION : cela n'a de sens que si les deux tables possèdent les mêmes attributs ET dans le même ordre !

if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement. '''

    # on lit le fichier CSV dont le nom est indiqué dans la variable globale FICHIER_ENTREE,
    # puis on crée notre table sous la forme d'une liste de dictionnaires, dans une variable "table" :
    table = lire_csv()
    
    # vous pouvez ici faire des tests de vos fonctions sur la table définie à la ligne précédente