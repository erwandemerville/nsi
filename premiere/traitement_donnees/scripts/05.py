d = {"nom":"Alice", "jour":7, "mois":1, "annee":1941}

# Afficher chaque clé du dictionnaire
for cle, val in d.items():
    print(f'{cle} : {val}')

# Autre possibilité
for el in d.items():
    print(el)

# Créer une liste de tuples (clé, valeur)
elements = list(d.items())
print(elements)