ma_liste = [10, 20, 30, 40, 50]

longueur = len(ma_liste)  # obtenir la longueur de la liste

# Utiliser une boucle for avec la fonction range() pour parcourir les indices
for i in range(longueur):
    element = ma_liste[i]
    print(f"Élément à l'indice {i} : {element}")