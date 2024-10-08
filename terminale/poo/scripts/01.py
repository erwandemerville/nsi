class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x  # initialiser la position en x à 0
        self.y = y  # initialiser la position en y à 0

    def deplacer(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

p1 = Point(5, 3)  # création d'une instance de la classe avec arguments
p2 = Point()  # création d'une autre instance sans arguments
print(f'p1.x = {p1.x} - p1.y = {p1.y}')
print(f'p2.x = {p2.x} - p1.y = {p2.y}')
p2.deplacer(3, 2)
print('Après déplacement :')
print(f'p1.x = {p1.x} - p1.y = {p1.y}')
print(f'p2.x = {p2.x} - p1.y = {p2.y}')