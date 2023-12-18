class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x  # initialiser la position en x à 0
        self.y = y  # initialiser la position en y à 0

    # Accesseurs
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    # Mutateurs
    def set_x(self, nx):
        self.x = nx

    def set_y(self, ny):
        self.y = ny

    def deplacer(self, dx, dy):
        self.set_x(self.get_x() + dx)
        self.set_y(self.get_y() + dy)

p = Point()
p.deplacer(5,7)
print(f'p.x = {p.get_x()} - p.y = {p.get_y()}')