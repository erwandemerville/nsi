import unittest

class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def longueur(self):
        return self._longueur

    def largeur(self):
        return self._largeur

    def changer_longueur(self, longueur):
        self._longueur = longueur

    def changer_largeur(self, largeur):
        self._largeur = largeur
        
    def est_carre(self):
        return self.longueur() == self.largeur()


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r = Rectangle(10,5)

    def test_longueur(self):
        self.assertEqual(self.r.longueur(), 10)

    def test_largeur(self):
        self.assertEqual(self.r.largeur(), 5)

    def test_changer_longueur(self):
        self.r.changer_longueur(8)
        self.assertEqual(self.r.longueur(), 8)

    def test_changer_largeur(self):
        self.r.changer_largeur(8)
        self.assertEqual(self.r.largeur(), 8)
        
    def test_est_carre(self):
        self.r.changer_longueur(5)
        self.assertTrue(self.r.est_carre())

if __name__ == '__main__':
    unittest.main()
