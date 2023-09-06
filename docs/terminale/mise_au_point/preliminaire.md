# Activité préliminaire

!!! quote "Sources"
    > Hachette NSI Terminale

## Ajouter des traces

La fonction suivante a été écrite par un élève de première suite à une consigne de son professeur pour implémenter l’algorithme de recherche dichotomique.

```python
def recherche(t, v):
    gauche = 0
    droite = len(t)
    while gauche < droite:
        milieu = (gauche+droite) // 2
        if t[milieu] < v:
            gauche = milieu
        else:
            droite = milieu
    return droite
```

!!! note "Exercice 1"
    1. Tester la fonction recherche avec le tableau `[2, 3, 4, 6, 7]` et la valeur **5**.
    Qu’observe-t-on ?
    2. Ajouter des instructions `print` pour afficher les valeurs des variables au cours de l’exécution. On pourra également utiliser `assert` pour tester des invariants.
    1. Identifier la ou les erreurs à l’aide de ces traces et les corriger.

## Utiliser un débogueur

L’implémentation suivante de l’algorithme de **tri par sélection** contient elle aussi des erreurs.

```python
def tri(t):
    for i in range(len(t)):
        jmin = i
        for j in range(i, len(t)):
            if t[j] <= t[jmin]:
                jmin = j
        if jmin != i:
            t[i] = t[jmin]
            t[jmin] = t[i]
```

!!! note "Exercice 2"
    Nous allons utiliser un outil de mise au point appelé débogueur (ou debugger en anglais).

    1. Copier le programme ci-dessus dans l’éditeur de texte de Thonny et ajouter une instruction qui appelle la fonction tri avec le tableau `[4, 2, 6, 7, 1, 8]`.
    2. Exécuter le programme. Qu’observe-t-on ?
    3. Lancer le programme avec le débogueur de **Thonny**.
    4. Identifier la ou les erreurs à l’aide du débogueur et les corriger.