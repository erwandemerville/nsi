import math

class Cercle:
    ''' Définition d'une classe Cercle. '''

    @staticmethod
    def aire(rayon):
        ''' Méthode statique pour calculer l'aire d'un cercle à partir du rayon. '''

        return math.pi * rayon ** 2

mon_cercle = Cercle(5)  # création d'une instance de la classe Cercle

# Utilisation de la méthode statique pour calculer l'aire,
# elle peut être appelée directement via la classe ou via l'instance.
aire_du_cercle = Cercle.aire(5)  # OU BIEN mon_cercle.aire(5)

print(f"L'aire d'un cercle avec un rayon de 5 est {aire_du_cercle}")