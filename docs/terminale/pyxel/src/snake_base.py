import pyxel
from random import randint

class SnakeGame:
    def __init__(self):
        
        # AJOUTEZ ICI VOS INSTRUCTIONS
        
        # exécuter le jeu (cette instruction doit rester à la fin du constructeur)
        pyxel.run(self.update, self.draw)

    def update(self):
        
        pass

    def draw(self):
        
        # on ajoute une instruction permettant d'effacer l'écran
        # et de le remplir avec la couleur 0 (= couleur noire) :
        pyxel.cls(0)
        
        pass

if __name__ == "__main__":
    SnakeGame()  # Instanciation de la classe SnakeGame