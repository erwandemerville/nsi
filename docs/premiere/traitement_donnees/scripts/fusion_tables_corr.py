def fusionner(table1, table2):
    ''' Effectue la fusion de deux tables de données qui possèdent des
    colonnes en commun et des colonnes qui diffèrent.
    :param table1: (list of dicts) une table de données
    :param table2: (list of dicts) une autre table de données
    :return: (list of dicts) une nouvelle table de données qui résulte de la fusion '''

    # on copie la table1 avec la méthode par compréhension
    nouvelle_table = [{cle: valeur for cle, valeur in e.items()} for e in table1]

    for i in range(len(table2)):  # on parcourt la table2
        for cle, val in table2[i].items():  # pour chaque enregistrement (chaque dictionnaire) de la table2
            if cle in table1[i]:  # si la clé était déjà présente dans la table1
                if val != table1[i][cle]:  # si la valeur est différente de celle de la table 1
                    nouvelle_table[i][cle] = val  # on remplace l'ancienne valeur par la nouvelle
            else:  # si la clé n'était pas présente dans la table1
                nouvelle_table[i][cle] = val  # on ajoute la nouvelle clé en l'associant à la valeur val
    return nouvelle_table # on renvoie la nouvelle table

# Test de la fonction fusionner
table1 = [{"nom":"Duchmol","prenom":"Jean","moyenne":12}, {"nom":"Martin","prenom":"Lise","moyenne":14}]
table2 = [{"nom":"Duchmol","prenom":"Jean","classe":"3A"}, {"nom":"Martin","prenom":"Lise","classe":"5B"}]

print(fusionner(table1, table2))