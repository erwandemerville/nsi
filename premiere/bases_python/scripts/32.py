from random import randint

# Créer une liste de taille et d'éléments aléatoires
lst = [randint(0, 100) for _ in range(1, randint(1, 51))]

# On cherche le dernier élément de cette liste
print("taille : ", len(lst))  # afficher la taille de lst
dernier_el = lst[len(lst) - 1]  # récupérer le dernier élément
print("dernier élément : ", dernier_el)  # afficher l'élément