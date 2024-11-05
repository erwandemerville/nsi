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

    if lst is None:  # si la liste chaînée est VIDE
        return 0  # sa longueur vaut 0
    else:
        return len(lst)  # sinon, on fait appel à la méthode spéciale __len__

def afficher(lst):
    ''' Affiche textuellement la liste.
    Si la liste est VIDE, représentée par l'objet None, l'affichage sera '[]'.
    Sinon, l'affichage sera obtenu avec la méthode __str__ de la classe Cellule. '''

    if lst is None:  # si la liste chaînée est VIDE
        print('[]')
    else:
        print(lst)  # on fait appel à la méthode spéciale __str__

def nieme_element(n, lst):
    ''' Renvoie le n-ième élément de la liste lst NON VIDE.
    Les éléments sont indexés à partir de 0.
    :param lst: (Cellule) une liste chaînée non vide.
    :return: l'élément contenu à l'indice n de la liste. '''

    if lst is None:
        raise ValueError("La liste ne doit pas être vide !")
    elif n == 0:  # cas de base : si n vaut 0
        return lst.valeur  # on renvoie la première valeur de la liste lst
    else:
        return nieme_element(n - 1, lst.suivante)  # cas général (récursif)

def concatener(l1, l2):
    ''' Renvoie une nouvelle liste, résultant de la concaténation des listes l1 et l2.
    :param l1: (Cellule | None) une liste chaînée
    :param l2: (Cellule | None) une autre liste chaînée
    :return: (Cellule | None) une nouvelle liste chaînée '''

    if l1 is None:  # cas de base : si la liste l1 est VIDE
        return l2  # on renvoie simplement l2
    else:
        return Cellule(l1.valeur, concatener(l1.suivante, l2))  # cas général (récursif)

def renverser_rec(lst):
    ''' Renvoie une nouvelle liste contenant les éléments de `lst` mais dans l'ordre inverse.
    Implémentation récursive, plus simple à écrire mais moins efficace, car on doit
    faire autant de concaténations qu'il y a d'éléments dans lst.
    :param lst: (Cellule | None) une liste chaînée
    :return: (Cellule | None) une nouvelle liste chaînée '''

    if lst is None:  # cas de base : si la liste lst est VIDE
        return None  # une liste VIDE renservée reste une liste VIDE
    else:
        return concatener(renverser_rec(lst.suivante), Cellule(lst.valeur, None))  # cas général (récursif)

def renverser_it(lst):
    ''' Renvoie une nouvelle liste contenant les éléments de `lst` mais dans l'ordre inverse.
    Version itérative, plus efficace que la version récursive précédente.
    :param lst: (Cellule | None) une liste chaînée
    :return: (Cellule | None) une nouvelle liste chaînée '''

    res = None  # créer une nouvelle liste chaînée VIDE
    c = lst  # stocker la première cellule de lst
    while c is not None:  # tant que l'on a pas parcouru toute la liste
        res = Cellule(c.valeur, res)  # on crée une nouvelle liste à partir de la valeur de la cellule c
                                      # et de l'ancienne liste contenue dans res
        c = c.suivante  # on récupère la cellule suivante pour la stocker dans c
    return res  # renvoyer notre nouvelle liste chaînée
    
# Créer une nouvelle liste contenant 1, 2, 3
lst = Cellule(1, Cellule(2, Cellule(3, None)))
lst_vide = None
afficher(lst)
afficher(lst_vide)