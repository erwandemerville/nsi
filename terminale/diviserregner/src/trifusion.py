def fusion(t0, t1):
    if not t0:
        return t1
    if not t1:
        return t0

    if t0[0] < t1[0]:
        return [t0[0]] + fusion(t0[1:], t1)
    else:
        return [t1[0]] + fusion(t0, t1[1:])
    
def tri_fusion(tab):
    # Si la taille du tableau est inférieure ou égale à 1, il est déjà trié
    if len(tab) <= 1:
        return tab

    # Diviser le tableau en deux moitiés
    milieu = len(tab) // 2
    t1 = tab[:milieu]
    t2 = tab[milieu:]

    # Trier récursivement les deux moitiés
    t1_trie = tri_fusion(t1)
    t2_trie = tri_fusion(t2)

    # Fusionner les deux moitiés triées
    resultat = fusion(t1_trie, t2_trie)

    return resultat

print(tri_fusion([0, 25, 36, 41, 1, 465, 2, 3, 987]))