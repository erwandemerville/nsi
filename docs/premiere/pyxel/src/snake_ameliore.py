import pyxel
from random import randint

# constantes de jeu
TITLE = "snake"
WIDTH = 400
HEIGHT = 320
CASE = 20

# initialiser l'application Pyxel
pyxel.init(WIDTH, HEIGHT, title=TITLE)

# variables globales pouvant être modifiées
snake = [[3,3], [2,3], [1,3]]
head = snake[0]  # Déclarer head (la tête du serpent)
food = [8, 3]
direction = [1,0]
score = 0

# Gère la vitesse de jeu
frame_refresh = 10
accelerer = False

def update():
    global direction
    global score
    global food
    global head
    global frame_refresh
    global accelerer
    
    if pyxel.frame_count % frame_refresh == 0:
        head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        # insérer la tête au début
        snake.insert(0, head)
        
        # effacer le dernier élément de snake :
        snake.pop()
    
    # Déplacement du snake
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

    # Faire mourir le snake
    if head in snake[1:] \
       or head[0] < 0 \
       or head[0] > WIDTH/CASE - 1 \
       or head[1] < 0 \
       or head[1] > HEIGHT/CASE - 1:
        exit()
    
    if head == food:
        score += 1
        # insérer une case à la queue du snake
        tail = [snake[-1][0] - direction[0], snake[-1][1] - direction[1]]
        snake.insert(len(snake), tail)
        # replacer la nourriture tant qu'elle est sur le snake
        while food in snake:
            food = [randint(0, WIDTH/CASE - 1), randint(0, HEIGHT/CASE - 1)]
        
        # accélérer la vitesse lors de certains paliers
        if score == 5 or score == 10 or score == 15 or score == 20 or score == 25:
            if not accelerer:
                accelerer = True
                frame_refresh -= 1
        if score == 6 or score == 11 or score == 16 or score == 21 or score == 26:
            accelerer = False
    
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
    
    # 9 est la couleur orange
    pyxel.rect(x_head * CASE, y_head * CASE, CASE, CASE, 9)
    
    # dessiner la nourriture
    x_food, y_food = food
    # 8 est la couleur rose
    pyxel.rect(x_food * CASE, y_food * CASE, CASE, CASE, 8)

pyxel.run(update, draw)