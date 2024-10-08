class A:
    nb = 0  # création d'un attribut de classe nb

    def __init__(self, x):
        ''' Constructeur de la classe A. Création d'un objet de type A. '''

        self.x = x  # création d'un attribut d'instance x
        A.nb = A.nb + 1  # incrémenter l'attribut de classe nb

print("A : nb = ", A.nb)  # afficher l'attribut de classe

a = A(3)  # création d'une nouvelle instance de A
print("A : nb = ", A.nb)  # afficher l'attribut de classe
print("a : x = ", a.x, " nb = ", a.nb)  # afficher les attributs de a

b = A(6)  # création d'une nouvelle instance de A
print("A : nb = ", A.nb)  # afficher l'attribut de classe
print("a : x = ", a.x, " nb = ", a.nb)  # afficher les attributs de a
print("b : x = ", b.x, " nb = ", b.nb)  # afficher les attributs de b

c = A(8)  # création d'une nouvelle instance de A
print("A : nb = ", A.nb)  # afficher l'attribut de classe
print("a : x = ", a.x, " nb = ", a.nb)  # afficher les attributs de a
print("b : x = ", b.x, " nb = ", b.nb)  # afficher les attributs de b
print("c : x = ", c.x, " nb = ", c.nb)  # afficher les attributs de c