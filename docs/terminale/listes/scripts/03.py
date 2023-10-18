class Cellule:
    ''' Une cellule d'une liste chaînée. '''

    def __init__(self, v, s):
        self.valeur = v  # Valeur contenue dans la cellule
        self.suivante = s  # Cellule suivante

# Créer une nouvelle liste contenant 1, 2, 3
lst = Cellule(1, Cellule(2, Cellule(3, None)))