import networkx as nx
import matplotlib.pyplot as plt

class Graphe:
    
    # Opérations de base
    def __init__(self):
        ''' Constructeur de la classe Graphe. '''
        
        self.etiq = {}  # dictionnaire associant une étiquette à un numéro de sommet
        self.mat = []  # matrice d'adjacence
        self.nb_sommets = 0  # nombre de sommets
        
    def ajouter_sommet(self, s:str):
        ''' Ajoute un sommet dans le graphe.
        On vérifiera si le sommet n'existe pas déjà. '''
        
        pass
    
    def ajouter_arc(self, s1:str, s2:str):
        ''' Ajoute un arc entre les sommets s1 et s2 du graphe.
        Si les sommets n'existent pas, on les crée. '''
        
        pass
    
    def supprimer_sommet(self, s:str):
        ''' Supprime le sommet s du graphe, ainsi que les arêtes associées. '''
        
        pass
    
    def supprimer_arc(self, s1:str, s2:str):
        ''' Supprime l'arc du graphe entre les sommets s1 et s2. '''
        
        pass
    
    # Autres opérations

    def est_sommet(self,s) -> bool:
        ''' Renvoie True si s est un sommet du graphe, False sinon. '''
        
        pass

    def est_arc(self,s1,s2) -> bool:
        ''' Renvoie True si un arc existe entre s1 et s2, False sinon. '''
        
        pass

    def ordre(self) -> int:
        ''' Renvoie l'ordre du graphe. '''
        
        pass
    
    def degre_entrant(self, s: str) -> int:
        ''' Renvoie le degré entrant d'un sommet s du graphe.
        On vérifiera si le sommet existe.
        Si le sommet n'existe pas, on renvoie -1. '''

        pass
    
    def degre_sortant(self, s: str) -> int:
        ''' Renvoie le degré sortant d'un sommet s du graphe.
        On vérifiera si le sommet existe.
        Si le sommet n'existe pas, on renvoie -1. '''
        
        pass
    
    def degre(self, s: str) -> int:
        ''' Renvoie le degré total d'un sommet s donné du graphe.
        On vérifiera si le sommet existe.
        Si le sommet n'existe pas, on renvoie -1. '''
        
        pass
    
    def successeurs(self, s: str) -> list:
        ''' Renvoie une liste des successeurs du sommet donné.
        On vérifiera si le sommet existe. '''
        
        pass

    def predecesseurs(self, s: str) -> list:
        ''' Renvoie une liste des prédecesseurs du sommet donné.
        On vérifiera si le sommet existe. '''
        
        pass

    # Parcours de graphes

    def parcours_largeur(self, depart: str) -> list:
        ''' Renvoie liste des sommets parcourus avec le parcours
        en largeur. '''
        
        pass

    def parcours_profondeur(self, depart: str) -> list:
        ''' Renvoie liste des sommets parcourus avec parcours en profondeur. '''
        
        pass

    # Affichage

    def affiche(self):
        ''' Affiche une représentation visuelle du graphe. '''
        
        G = nx.DiGraph()
        for sommet in self.etiq:
            G.add_node(sommet)
        for s1 in range(self.nb_sommets):
            for s2 in range(self.nb_sommets):
                if self.mat[s1][s2] == 1:
                    G.add_edge(self.etiq[s1], self.etiq[s2])
        nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, font_size=12, font_weight='bold')
        plt.show()

if __name__ == "__main__":
    ''' Mettre ici les instructions pour tester votre classe Graphe. '''
    
    pass
    
