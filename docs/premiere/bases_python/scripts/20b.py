def produit(a, b):
    resultat = 1
    for _ in range(b):
        resultat = resultat * a
    return resultat

resultat = produit(5, 6)  # appeler produit sur 5 et 6 et stocker la valeur de retour dans resultat
print(resultat)  # afficher le résultat