class Pile:
    ''' Classe permettant de définir une structure de pile. 
    Le contenu d'une pile est représentée par une liste Python. '''

    def __init__(self: 'Pile'):
        ''' Constructeur de la classe Pile. '''

        self.contenu = []

    # Opérations de base

    def est_vide(self: 'Pile') -> bool:
        ''' Renvoie True si la pile est vide, False sinon. '''

        return not self.contenu

    def empiler(self: 'Pile', elt: int) -> None:
        ''' Empile un élément donné au sommet de la pile. '''

        self.contenu.append(elt)
    
    def depiler(self: 'Pile') -> int:
        ''' Dépiler l'élément situé au sommet de la pile NON VIDE. '''

        if self.est_vide():
            raise ValueError("Erreur : Impossible de dépiler sur une pile vide !")
        return self.contenu.pop()