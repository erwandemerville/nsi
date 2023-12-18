# from dessin import dessiner

''' Classe implémentant un Arbre Binaire. '''

class Arbre:
    def __init__(self, valeur=None, gauche=None, droite=None):
        ''' Crée un nouvel arbre binaire.
        :param valeur: (int|str) La valeur du noeud racine, soit un entier, soit une chaîne de caractères
        :param gauche: (Arbre) Le sous-arbre binaire gauche (None pour arbre binaire vide)
        :param droite: (Arbre) Le sous-arbre binaire droit (None pour arbre binaire vide)
        :CU: Si valeur est à None, gauche et droite doivent être également à None (cas de l'arbre vide),
        sinon, gauche et droite doivent être de type Arbre. 
        
        :Exemples:

        >>> a = Arbre()
        >>> a.est_ABR()
        True
        >>> a = a.inserer(6) 
        >>> a.est_ABR()
        True
        >>> a = a.inserer(8)
        >>> a = a.inserer(4)
        >>> a = a.inserer(5)
        >>> a = a.inserer(3)
        >>> a.est_ABR()
        True
        >>> a.droite().valeur_racine() == 8
        True
        >>> a.gauche().droite().valeur_racine() == 5
        True
        >>> a.rechercher(7)
        False
        >>> a.rechercher(3)
        True
        >>> a.maximum() == 8
        True
        >>> a.minimum() == 3
        True
        >>> Arbre(7, Arbre(5, Arbre(6, Arbre(), Arbre()), Arbre()), Arbre()).est_ABR()
        False
        '''
        
        assert (valeur == None and gauche == None and droite == None) or \
               (type(valeur) in (int, str) and type(gauche) == Arbre and type(droite) == Arbre)
        
        self.v = valeur
        self.g = gauche
        self.d = droite

    # ===> MÉTHODES FOURNIES <===

    def est_vide(self: 'Arbre') -> bool:
        ''' Renvoie True si l'arbre binaire est vide, False s'il ne l'est pas. '''
        
        return self.v == None
        # Si la valeur du noeud racine est à None, le sous-arbre gauche et droit le sont également (donc l'arbre est vide)
    
    def racine(self: 'Arbre') -> 'Arbre':
        ''' Renvoie le Noeud racine de l'arbre binaire.
        :CU: L'arbre n'est PAS vide '''
        
        return self
    
    def valeur_racine(self: 'Arbre') -> 'int|str':
        ''' Renvoie la valeur de la racine de l'arbre binaire.
        :CU: L'arbre n'est PAS vide '''
        
        return self.v
    
    def gauche(self: 'Arbre') -> 'Arbre':
        ''' Renvoie le sous-arbre gauche de l'arbre binaire.
        :CU: L'arbre n'est PAS vide '''
        
        return self.g
    
    def droite(self: 'Arbre') -> 'Arbre':
        ''' Renvoie le sous-arbre droit de l'arbre binaire.
        :CU: L'arbre n'est PAS vide '''
        
        return self.d
    
    def est_feuille(self: 'Arbre') -> 'Arbre':
        ''' Renvoie True si l'arbre binaire est une feuille, False s'il ne l'est pas.
        :CU: L'arbre n'est PAS vide '''
        
        return self.gauche().est_vide() and self.droite().est_vide()
    
    def parcours_infixe(self: 'Arbre') -> list:
        ''' Effectue le parcours infixe d'un arbre binaire,
        renvoie la liste des valeurs des noeuds visités dans cet ordre. '''

        if self.est_vide():  # Si l'arbre binaire EST VIDE, renvoyer liste vide
            return []

        res = []
        if not self.gauche().est_vide():
            res += self.gauche().parcours_infixe()
        res += [self.valeur_racine()]
        if not self.droite().est_vide():
            res += self.droite().parcours_infixe()
        return res

    # ===> MÉTHODES À COMPLÉTER <===
    
    # Méthodes pour déterminer si un arbre binaire est un arbre binaire de recherche

    def minimum(self: 'Arbre') -> int:
        ''' Renvoie la valeur minimale des noeuds de l'arbre
        :CU: L'abre n'est PAS vide '''

        pass

    def maximum(self: 'Arbre') -> int:
        ''' Renvoie la valeur maximale des noeuds de l'arbre
        :CU: L'arbre n'est PAS vide '''

        pass
        
    def est_ABR(self: 'Arbre') -> bool:
        ''' Renvoie True si l'arbre binaire est un arbre binaire de recherche, False sinon. '''
        
        pass

    def est_ABR_v2(self: 'Arbre') -> bool:
        ''' Renvoie True si l'arbre binaire est un arbre binaire de recherche, False sinon.
        Autre version, vérifiant si la liste des noeuds visités en ordre infixe est triée dans l'ordre croissant. '''
        
        lst_valeurs = self.parcours_infixe()  # Récupérer la liste des valeurs des noeuds visités en parcours infixe
        pass # À COMPLÉTER

    # Recherche et insertion dans un arbre binaire de recherche
    
    def rechercher(self: 'Arbre', elt: 'int|str') -> bool:
        ''' Recherche l'élément elt dans l'arbre, renvoie True s'il est trouvé, False sinon.
        :CU: self.est_ABR() == True '''
        
        pass

    def inserer(self: 'Arbre', elt: 'int|str') -> 'Arbre':
        ''' Insère l'élément elt dans l'arbre 
        :CU: self.est_ABR() == True '''
        
        pass

    # Partie "Aller plus loin"

    def minimum_abr(self: 'Arbre') -> int:
        ''' Renvoie la valeur minimale des noeuds de l'arbre binaire de recherche
        :CU: self.est_ABR() == True and not self.est_vide() '''

        pass

    def maximum_abr(self: 'Arbre') -> int:
        ''' Renvoie la valeur maximale des noeuds de l'arbre binaire de recherche
        :CU: self.est_ABR() == True and not self.est_vide() '''

        pass

def trier(liste: list) -> list:
    ''' Trie les éléments (int|str) d'une liste dans l'ordre croissant.
    Renvoie la liste triée. '''
    
    pass

if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    import doctest
    doctest.testmod(verbose=False)
