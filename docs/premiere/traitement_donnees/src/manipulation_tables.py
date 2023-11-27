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
    
    fichier = open(fichier, newline='')
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
        
    with open(fichier, 'w') as fic:
        dic = csv.DictWriter(fic, fieldnames=ordre, delimiter=delim)  # Création d'un objet dic de classe DictWriter
        dic.writeheader()  # Écrire la première ligne, celle des attributs
        for ligne in table:  # Pour chaque enregistrement de la table :
            dic.writerow(ligne)  # Écrire les lignes contenant les données de la table


# Manipulation de tables (à compléter)

def creer_table_classe():

    pass

def lister_colonnes(table):
    ''' Prend une table en entrée et renvoie une liste contenant ses attributs.
    :param table: (list of dicts) une liste de dictionnaires
    :return: (list) liste des attributs de la table.
    :Exemples:
    >>> table = lire_csv()
    >>> lister_colonnes(table)
    ["RENTREE SCOLAIRE", "REGION ACADEMIQUE", "ACADEMIE", ...] '''

    pass

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
    
    pass

def effectif_total_terminale(table, numero_etablissement):
    ''' Renvoie l' "EFFECTIF TOTAL EN TERMINALE GENERALE" de l'établissement dont le "NUMERO ETABLISSEMENT" est donné.
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :param numero_etablissement: (str) le numéro associé à un établissement

    Faites le test avec le "LYCEE JEAN PERRIN" dont le "NUMERO ETABLISSEMENT" est "0590110Z". '''
    
    pass

def effectif_total_eleves_nsi(table, numero_etablissement, rentree):
    ''' Renvoie la somme des effectifs garçons ("0747 - NUMERIQUE ET SCIENCES INFORMATIQUES - garcons")
    + filles ("0747 - NUMERIQUE ET SCIENCES INFORMATIQUES - fille"s) en NSI pour une "RENTREE SCOLAIRE" (année) donnée,
    et pour un "NUMERO ETABLISSEMENT" donné.
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :param numero_etablissement: (str) le numéro associé à un établissement
    :param rentree: (str) la rentrée scolaire souhaitée
    
    Faites le test avec le "LYCEE JEAN PERRIN" pour la "RENTREE SCOLAIRE" 2020, dont le "NUMERO ETABLISSEMENT" est "0590110Z". '''
    
    pass

def compter_lycees_generaux(table):
    ''' Renvoie le nombre de lycées généraux.
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :return: (int) le nombre de lycées dont 'DENOMINATION' = 'LYCEE GENERAL'
    '''
    
    pass

def moyenne_garcons_nsi(table, region):
    ''' Renvoie la moyenne des effectifs de garçons en NSI ("0747 - NUMERIQUE ET SCIENCES INFORMATIQUES - garcons"),
    dans les lycées dont la "REGION ACADEMIQUE" est donnée.
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :param region: (str) la région pour laquelle calculer la moyenne
    :return: (float) la moyenne des effectifs de garçons en NSI
    
    Faites le test avec la "REGION ACADEMIQUE" des "HAUTS-DE-FRANCE". '''
    
    pass

def lycees_academie(table, academie, fichier=FICHIER_SORTIE):
    ''' Crée une nouvelle table contenant uniquement les enregistrements dont l' "ACADEMIE" est donnée,
    puis enregistre cette table dans le fichier CSV spécifié (qui est initialisé à FICHIER_SORTIE).
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :param academie: (str) l'académie dont on veut garder les enregistrements.
    :param fichier: (str) le fichier de sortie (initialement égal au contenu de la variable globale FICHIER_SORTIE)

    Faites le test pour l' "ACADEMIE" de "LILLE". '''
    
    pass

# EXERCICE 4 - Fonctions à compléter
# Les fonctions suivantes concernent la table du fichier fr-en-effectifs-specialites-doublettes-terminale-generale.csv

def trier_selon_patronyme(table):
    ''' Trier la table de donnée spar rapport à la colonne "PATRONYME".
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :return: (list of dicts) renvoie une nouvelle table de données triée par rapport au patronyme des lycées '''

    pass

def trier_selon_effectif(table):
    ''' Trier la table de donnée spar rapport à la colonne "EFFECTIF TOTAL EN TERMINALE GENERALE".
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :return: (list of dicts) renvoie une nouvelle table de données triée par rapport à l'effectif total en terminale générale '''

    pass

def trier_selon_academie_et_effectif(table):
    ''' Trier la table de donnée spar rapport à la colonne "ACADEMIE" et "EFFECTIF TOTAL EN TERMINALE GENERALE".
    :param table: (list of dict) la table sous la forme d'une liste de dictionnaires
    :return: (list of dicts) renvoie une nouvelle table de données triée par rapport à l'académie ET l'effectif total en terminale générale '''

    pass

# EXERCICE 4 - Fonctions à compléter

def fusionner_deux_tables(table1, table2):
    ''' Fusionner deux tables de données.
    :param table1: (list of dicts) une table sous la forme d'une liste de dictionnaires
    :param table2: (list of dicts) une table sous la forme d'une liste de dictionnaires
    :return: (list of dicts) une table sous la forme d'une liste de dictionnaires '''

    pass

if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement. '''

    table = lire_csv()
    sorted(table)