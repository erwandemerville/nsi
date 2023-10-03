ma_liste = [10, 20, 30, 40, 50]

# Obtenez la longueur de la liste
longueur = len(ma_liste)

# Utilisez une boucle for avec la fonction range() pour générer des indices
for i in range(longueur):
    element = ma_liste[i]
    print(f"Élément à l'indice {i} : {element}")