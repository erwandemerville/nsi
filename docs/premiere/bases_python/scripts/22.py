mot_de_passe = "secret"
essais_restants = 3

while essais_restants > 0:
    tentative = input("Entrez le mot de passe : ")
    
    if tentative == mot_de_passe:
        print("Accès autorisé !")
        break  # Sortir de la boucle
    else:
        essais_restants -= 1
        print(f"Mot de passe incorrect. Il vous reste {essais_restants} essais.")

if essais_restants == 0:
    print("Nombre maximal d'essais atteint. Accès refusé.")