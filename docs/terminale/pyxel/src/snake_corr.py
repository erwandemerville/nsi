import pyxel
from random import randint

class SnakeGame:
    def __init__(self):
        # constantes de jeu (ne sont pas modifiées)
        self.TITLE = "snake"
        self.WIDTH = 200
        self.HEIGHT = 160
        self.CASE = 20
        self.FRAME_REFRESH = 10  # Gère la vitesse de jeu

        # initialiser l'application Pyxel
        pyxel.init(self.WIDTH, self.HEIGHT, title=self.TITLE)

        # variables globales pouvant être modifiées
        self.snake = [[3, 3], [2, 3], [1, 3]]  # position de chaque élément du snake
        self.head = self.snake[0]  # la tête du serpent
        self.food = [8, 3]  # position de la nourriture
        self.direction = [1, 0]  # direction du snake
        self.score = 0  # score

        # exécuter le jeu
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count % self.FRAME_REFRESH == 0:
            # la nouvelle tête est l'ancienne, déplacée dans la direction
            self.head = [self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1]]
            # on l'insère au début
            self.snake.insert(0, self.head)
            
            if not self.head == self.food:
                self.snake.pop()

        # En cas d'appui sur une touche : Changer direction du snake
        if pyxel.btn(pyxel.KEY_ESCAPE):
            exit()
        elif pyxel.btn(pyxel.KEY_RIGHT) and self.direction in ([0, 1], [0, -1]):
            self.direction = [1, 0]
        elif pyxel.btn(pyxel.KEY_LEFT) and self.direction in ([0, 1], [0, -1]):
            self.direction = [-1, 0]
        elif pyxel.btn(pyxel.KEY_UP) and self.direction in ([1, 0], [-1, 0]):
            self.direction = [0, -1]
        elif pyxel.btn(pyxel.KEY_DOWN) and self.direction in ([1, 0], [-1, 0]):
            self.direction = [0, 1]

        # Faire mourir le snake s'il se touche lui-même ou sort de la zone
        if self.head in self.snake[1:] \
           or self.head[0] < 0 \
           or self.head[0] > self.WIDTH/self.CASE - 1 \
           or self.head[1] < 0 \
           or self.head[1] > self.HEIGHT/self.CASE - 1:
            exit()

        # Lorsque la tête du snake touche une nourriture
        if self.head == self.food:
            self.score += 1
            
            while self.food in self.snake:
                self.food = [randint(0, self.WIDTH/self.CASE - 1), \
                             randint(0, self.HEIGHT/self.CASE - 1)]
            # sortie du while : on a trouvé une nouvelle case pour la pomme

    def draw(self):
        pyxel.cls(0)

        # afficher le score en couleur blanche
        pyxel.text(4, 4, f"SCORE : {self.score}", 7)

        # dessiner le corps en vert
        for anneau in self.snake[1:]:
            x, y = anneau[0], anneau[1]
            pyxel.rect(x * self.CASE, y * self.CASE, self.CASE, self.CASE, 11)

        # dessiner la tête en orange
        x_head, y_head = self.snake[0]
        # 9 est la couleur orange
        pyxel.rect(x_head * self.CASE, y_head * self.CASE, self.CASE, self.CASE, 9)

        # dessiner la nourriture
        x_food, y_food = self.food
        # 8 est la couleur rose
        pyxel.rect(x_food * self.CASE, y_food * self.CASE, self.CASE, self.CASE, 8)

if __name__ == "__main__":
    SnakeGame()
