def compte_a_rebours(n):
    if n <= 0:
        print("Fin du compte à rebours!")
    else:
        print(n)
        compte_a_rebours(n - 1)

compte_a_rebours(10)