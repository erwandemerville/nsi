individus = [("Alice", 7, 1, 1941), ("Bob", 9, 12, 1909), ("Charles", 14, 12, 1965), ("Delphine", 11, 1, 1938)]

for e in individus:
    print(f'Nom : {e[0]}, né(e) le {e[1]}/{e[2]}/{e[3]}')

print('-----')

for nom, jour, mois, annee in individus:
    print(f'Nom : {nom}, né(e) le {jour}/{mois}/{annee}')
