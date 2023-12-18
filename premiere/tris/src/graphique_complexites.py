#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

''' Programme générant un graphique des différentes complexités algorithmiques. '''

# Fonctions de complexité
def constante(x):
    return np.ones_like(x)

def logarithmique(x):
    return np.log2(x)

def lineaire(x):
    return x

def quasi_lineaire(x):
    return x * np.log2(x)

def quadratique(x):
    return x**2

def exponentielle(x):
    return 2**x

def factorielle(x):
    return np.array([np.math.factorial(int(i)) if i <= 20 else np.inf for i in x])

def stirling_approximation(x):
    return np.sqrt(2 * np.pi * x) * (x / np.e)**x

# Plage des valeurs de n
x = np.linspace(1, 20, 500)

# Calcul des complexités pour chaque valeur de n
y_constante = constante(x)
y_logarithmique = logarithmique(x)
y_lineaire = lineaire(x)
y_quasi_lineaire = quasi_lineaire(x)
y_quadratique = quadratique(x)
y_exponentielle = exponentielle(x)
y_factorielle = stirling_approximation(x)

# Création du graphique
plt.figure(figsize=(12, 8))
plt.plot(x, y_constante, label="constante $O(1)$")
plt.plot(x, y_logarithmique, label="logarithmique $O(log~n)$")
plt.plot(x, y_lineaire, label="linéaire $O(n)$")
plt.plot(x, y_quasi_lineaire, label="quasi-linéaire $O(n~log~n)$")
plt.plot(x, y_quadratique, label="quadratique $O(n^2)$")
plt.plot(x, y_exponentielle, label="exponentielle $O(2^n)$")
plt.plot(x, y_factorielle, label="factorielle $O(n!)$")

# Configuration du graphique
plt.title("Complexités algorithmiques")
plt.xlabel("Taille de l'entrée (n)")
plt.ylabel("Nombre d'opérations")
plt.legend()
plt.grid(True)
plt.xlim(1, 20)
plt.ylim(0.1, 200)

# Affichage / sauvegarde du graphique
# plt.show()
plt.savefig('graphique_complexites.png', dpi=300, format='png')
