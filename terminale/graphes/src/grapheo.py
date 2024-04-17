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
    
    def ajouter_arete(self, s1:str, s2:str):
        ''' Ajoute une arête entre les sommets s1 et s2 du graphe.
        Si les sommets n'existent pas, on les crée. '''
        
        pass
    
    def supprimer_sommet(self, s:str):
        ''' Supprime le sommet s du graphe, ainsi que les arêtes associées. '''
        
        pass
    
    def supprimer_arete(self, s1:str, s2:str):
        ''' Supprime l'arête du graphe entre les sommets s1 et s2. '''
        
        pass
    
    # Autres opérations
    
    def est_arete(self,s1,s2) -> bool:
        ''' Renvoie True si une arête existe entre s1 et s2, False sinon. '''
        
        pass

    def est_sommet(self,s) -> bool:
        ''' Renvoie True si s est un sommet du graphe, False sinon. '''
        
        pass
    
    def ordre(self) -> int:
        ''' Renvoie l'ordre du graphe. '''
        
        pass
    
    def degre_entrant(self, s: str) -> int:
        ''' Renvoie le degré entrant d'un sommet s du graphe. '''
        pass
    
    def degre_sortant(self, s: str) -> int:
        ''' Renvoie le degré sortant d'un sommet s du graphe. '''
        
        pass
    
    def degre(self, s: str) -> int:
        ''' Renvoie le degré d'un sommet s donné du graphe.
        On vérifiera si le sommet existe.
        Si le sommet n'existe pas, on renvoie -1. '''
        
        pass
    
    def voisins(self, s: str) -> list:
        ''' Renvoie une liste des voisins du sommet donné.
        On vérifiera si le sommet existe. '''
        
        pass
    
    def affiche(self):
        ''' Affiche une représentation visuelle du graphe. '''
        
        pass
    
    # Parcours de graphes
    
    pass

    # Affichage
    
    def affiche(self):
        ''' Affiche une représentation visuelle du graphe. '''
        
        G = nx.DiGraph()
        for sommet, voisins in self.adj.items():
            for voisin in voisins:
                G.add_edge(sommet, voisin)
        nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, font_size=12, font_weight='bold')
        plt.show()

if __name__ == "__main__":
    ''' Mettre ici les instructions pour tester votre classe Graphe. '''
    
    pass
    
