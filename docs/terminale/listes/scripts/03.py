class Cellule:
    ''' Une cellule d'une liste chaînée. '''

    def __init__(self, v, s):
        self.valeur = v  # Valeur contenue dans la cellule
        self.suivante = s  # Cellule suivante

    def __len__(self):
        ''' Renvoie la longueur de la liste non vide. '''
        
        if self.suivante == None:
            return 1
        else:
            return 1 + len(self.suivante)
        
    def __str__(self):
        ''' Renvoie une représentation textuelle de la liste. '''

        res = f'[{self.valeur}'
        cell = self.suivante
        while cell:
            res += f', {cell.valeur}'
            cell = cell.suivante
        res += ']'
        return res

# Fonctions définies en dehors de la classe

def longueur(lst):
    ''' Renvoie la longueur d'une liste.
    Si la liste est un objet None, cette longueur vaut 0.
    Sinon, la longueur est calculée avec la méthode __len__ de la classe Cellule. '''

    pass

def afficher(lst):
    ''' Renvoie un affichage textuelle de la liste.
    Si la liste est l'objet None, l'affichage sera [].
    Sinon, l'affichage sera obtenu avec la méthode __str__ de la classe Cellule. '''

    pass

def nieme_element(n, lst):
    ''' Renvoie le n-ième élément de la liste lst NON VIDE.
    Les éléments sont indexés à partir de 0.
    :param lst: (Cellule) une liste chaînée non vide.
    :return: l'élément contenu à l'indice n de la liste. '''

    if lst is None:
        raise ValueError("La liste ne doit pas être vide !")
    else:
        # À COMPLÉTER
        pass

def concatener(l1, l2):
    ''' Renvoie une nouvelle liste, résultant de la concaténation des listes l1 et l2.
    :param l1: (Cellule | None) une liste chaînée
    :param l2: (Cellule | None) une autre liste chaînée
    :return: (Cellule | None) une nouvelle liste chaînée '''

    pass

def renverser(lst):
    ''' Renvoie une nouvelle liste contenant les éléments de `lst` mais dans l'ordre inverse.
    :param lst: (Cellule | None) une liste chaînée
    :return: (Cellule | None) une nouvelle liste chaînée '''

# Créer une nouvelle liste contenant 1, 2, 3
lst = Cellule(1, Cellule(2, Cellule(3, None)))
lst_vide = None
afficher(lst)
afficher(lst_vide)