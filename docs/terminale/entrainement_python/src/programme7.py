# ===> PROGRAMME 7 <===

'''
Ce fichier contient une classe Noeud représentant un noeud d'une liste chainée,
et une classe Liste représentant une liste chainée.

:Exemple:
>>> l = Liste(Noeud(2, Noeud(4, Noeud(7, Noeud(5, None)))))
>>> l.premierElement()
2
>>> l.dernierElement()
5
>>> l.listePython()
[2, 4, 7, 5]
>>> l.maximum()
7
'''

class Noeud:
    def __init__(self, valeur, noeud_suivant):
        self.valeur = valeur
        self.noeud_suivant = noeud_suivant
        
    def getValeur(self):
        ''' Méthode qui renvoie la valeur du noeud. '''
        
        ...
        
    def getNoeudSuivant(self):
        ''' Méthode qui renvoie le noeud suivant. '''
        
        ...
        
    def setValeur(self, val):
        ''' Méthode qui modifie la valeur du noeud. '''
        
        ...
        
    def estDernier(self):
        ''' Renvoie True si l'attribut noeud_suivant vaut None, False sinon. '''
        
class Liste:
    
    def __init__(self, premier_noeud):
        self.premier_noeud = premier_noeud
        
    def premierElement(self):
        ''' Renvoie le premier élément de la liste. '''
        
        ...
        
    def dernierElement(self):
        ''' Renvoie le dernier élément de la liste. '''
        
        ...
        
    def getElement(self, position):
        ''' Renvoie la valeur de l'élément de la liste à la position spécifiée.
        position = 0 : Première valeur. '''
        
        ...
        
    def listePython(self):
        ''' Renvoie la liste chainée sous forme d'une liste Python. '''
        
        ...
        
    def maximum(self):
        ''' Renvoie le maximum de la liste chainée. '''
        
        ...


# Les lignes suivantes permettent d'activer les tests des fonctions.
if __name__ == '__main__':
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
