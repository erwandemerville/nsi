# Un jeu de snake avec Pyxel

!!! success "Énoncé de l'exercice"
    Voici le **PDF** de l'énoncé de l'exercice comportant des *trous*, ainsi que la **version corrigée** de l'énoncé :

    - [Snake - Énoncé à trous](documents/Snake_Pyxel.pdf){ target="_blank" }
    - [Snake - Énoncé corrigé](documents/Snake_Pyxel_correction.pdf){ target="_blank" }

## Correction

Voici le **programme Python** corrigé, comprenant de nombreux *commentaires* pour vous aider à comprendre le code :

```python
import pyxel
from random import randint

# constantes de jeu (ne sont pas modifiées)
TITLE = "snake"
WIDTH = 200
HEIGHT = 160
CASE = 20
FRAME_REFRESH = 10  # Gère la vitesse de jeu

# initialiser l'application Pyxel
pyxel.init(WIDTH, HEIGHT, title=TITLE)

# variables globales pouvant être modifiées
snake = [[3,3], [2,3], [1,3]]  # position de chaque élément du snake
head = snake[0]  # la tête du serpent
food = [8, 3]  # position de la nourriture
direction = [1,0]  # direction du snake
score = 0  # score

def update():
    # Le mot-clé "global" permet d'autoriser la modification de variables globales
    global direction
    global score
    global food
    global head
    
    # Permet de n'effectuer un déplacement que toutes les 10 frames
    # (cette valeur peut être modifiée dans la variable globale FRAME_REFRESH)
    if pyxel.frame_count % FRAME_REFRESH == 0:
        head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        # insérer la tête au début
        snake.insert(0, head)
        
        # effacer le dernier élément de snake :
        snake.pop()
    
    # En cas d'appui sur une touche : Changer direction du snake
    if pyxel.btn(pyxel.KEY_ESCAPE):
        exit()
    elif pyxel.btn(pyxel.KEY_RIGHT) and direction in ([0, 1], [0, -1]):
        direction = [1, 0]
    elif pyxel.btn(pyxel.KEY_LEFT) and direction in ([0, 1], [0, -1]):
        direction = [-1, 0]
    elif pyxel.btn(pyxel.KEY_UP) and direction in ([1, 0], [-1, 0]):
        direction = [0, -1]
    elif pyxel.btn(pyxel.KEY_DOWN) and direction in ([1, 0], [-1, 0]):
        direction = [0, 1]

    # Faire mourir le snake s'il se touche lui-même ou sort de la zone
    if head in snake[1:] \
       or head[0] < 0 \
       or head[0] > WIDTH/CASE - 1 \
       or head[1] < 0 \
       or head[1] > HEIGHT/CASE - 1:
        exit()
    
    # Lorsque la tête du snake touche une nourriture
    if head == food:  # si la position de la tête = la position de la nourriture
        score += 1
        # replacer la nourriture tant qu'elle est sur le snake
        while food in snake:
            food = [randint(0, WIDTH/CASE - 1), randint(0, HEIGHT/CASE - 1)]
    
def draw():
    # l'écran : à effacer puis remplir de noir
    pyxel.cls(0)
    
    # afficher le scoe en couleur blanche
    pyxel.text(4, 4, f"SCORE : {score}", 7)
    
    # dessiner le corps en vert
    for anneau in snake[1:]:
        x, y = anneau[0], anneau[1]
        # 11 est une couleur un peu verte
        pyxel.rect(x * CASE, y * CASE, CASE, CASE, 11)
    
    # dessiner la tête en orange
    x_head, y_head = snake[0]  # récupérer position (x, y) de la tête
    pyxel.rect(x_head * CASE, y_head * CASE, CASE, CASE, 9)  # 9 est la couleur orange
    
    # dessiner la nourriture
    x_food, y_food = food
    pyxel.rect(x_food * CASE, y_food * CASE, CASE, CASE, 8)  # 8 est la couleur rose

pyxel.run(update, draw)  # exécuter le jeu
```

<center>
[:material-cursor-default-click: Télécharger ce programme](src/snake_corr.py){ target="_blank" }
</center>

## Une version améliorée

Voici une **version améliorée** du jeu dans laquelle :

- on a agrandit la **fenêtre de jeu**,
- à chaque **nourriture mangée**, la **queue** du ***snake* augmente d'un élément**,
- on **accélère la vitesse de déplacement** du ***snake*** toutes les 5 nourritures mangées.

<center>
[:material-cursor-default-click: Télécharger ce programme](src/snake_ameliore.py){ target="_blank" }
</center>