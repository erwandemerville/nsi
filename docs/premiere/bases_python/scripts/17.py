nb = int(input("Saisissez votre âge : "))
if nb < 5:
    print("Vous êtes un bébé.")
elif nb < 12:
    print("Vous êtes un enfant.")
elif nb < 18:
    print("Vous êtes un ado")
elif nb < 40:
    print("Vous êtes un adulte")
elif nb < 60:
    print("Vous êtes un vieil adulte")
else:
    print("Vous êtes un vieillard.")