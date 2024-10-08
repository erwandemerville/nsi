class A:
    nb = 0  # création d'un attribut de classe nb

    def __init__(self, x):
        ''' Constructeur de la classe A. Création d'un objet de type A. '''
        
        A.nb = A.nb + 1  # incrémenter l'attribut de classe nb
        self.x = x  # création d'un attribut d'instance x

    @classmethod
    def get_nb(cls):
        ''' Méthode de classe qui renvoie l'attribut de classe nb. '''

        return A.nb

    @classmethod
    def nouveau(cls):
        ''' Méthode de classe qui renvoie l'attribut de classe nb. '''
        
        return cls(10)

print(f"objets = {A.get_nb()}")

a = A(8)
print(f"a.x = {a.x} - objets = {A.get_nb()}")

b = A.nouveau()
print(f"b.x = {b.x} - objets = {A.get_nb()}")