import networkx as nx
import matplotlib.pyplot as plt

class Graphe:
    def __init__(self):
        self.adj = {}

    # Opérations de base

    def ajouter_sommet(self, s: str):
        ''' Ajoute un nouveau sommet au graphe. '''
        
        pass
    
    def ajouter_arete(self, s1: str, s2: str):
        ''' Ajoute une nouvelle arête au graphe à partir de deux sommets.
        Si les sommets n'existent pas, on les crée. '''
        
        pass
    
    def supprimer_sommet(self, s: str):
        ''' Supprime le sommet entré.
        Si le sommet n'existe pas, on affichera un message d'erreur.
        (On pourra utiliser est_sommet pour les vérifications.) '''
        
        pass
    
    def supprimer_arete(self, s1: str, s2: str):
        ''' Supprime l'arête entre les deux sommets donnés.
        Si les deux sommets ou l'arête n'existent pas, on affichera un message d'erreur.
        (On pourra utiliser est_sommet et est_arete pour les vérifications.) '''
        
        pass
    
    # Autres opérations

    def est_sommet(self, s: str) -> bool:
        ''' Vérifie que le sommet donné existe. '''
        
        pass
    
    def est_arete(self, s1: str, s2: str) -> bool:
        ''' Vérifie que l'arête entre les deux sommets donnés existe. '''
        
        pass
    
    def ordre(self) -> int:
        ''' Renvoie l'ordre du graphe. '''
        
        pass
    
    def degre(self, s: str) -> int:
        ''' Renvoie le degré d'un sommet du graphe. '''
        
        pass
    
    def voisins(self, s: str) -> list:
        ''' Renvoie une liste des voisins du sommet donné. '''
        
        pass

    # Parcours de graphes

    pass

    # Connexité, cycles et arbre

    pass

    # Affichage

    def affiche(self):
        ''' Affiche une représentation visuelle du graphe. '''
        
        G = nx.Graph()
        for sommet, voisins in self.adj.items():
            for voisin in voisins:
                G.add_edge(sommet, voisin)
        nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, font_size=12, font_weight='bold')
        plt.show()

if __name__ == "__main__":
    ''' Mettre ici les instructions pour tester votre classe Graphe. '''
    
    pass