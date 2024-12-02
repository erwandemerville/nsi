import pyxel

# constantes de jeu (ne sont pas modifiées)
TITLE = "snake"
WIDTH = 200
HEIGHT = 160
CASE = 20

# initialiser l'application Pyxel
pyxel.init(..., ..., title=...)

# variables globales pouvant être modifiées
...

def update():
    pass
    
def draw():
    # effacer l'écran puis remplir avec du noir
    pyxel.cls(0)
    
    pass

# Lancer le jeu
pyxel.run(update, draw)  # exécuter le jeu