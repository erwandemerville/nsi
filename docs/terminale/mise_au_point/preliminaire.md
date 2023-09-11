# Activité préliminaire

!!! quote "Source"
    Inspiré d'une activité du *Hachette NSI Terminale*.

## Ajouter des traces

La fonction suivante a été écrite par un élève de première suite à une consigne de son professeur pour implémenter l’**algorithme de recherche dichotomique**.

La **docstring**, présenté dans la fonction, spécifie ce qu'elle est censée faire.

```python
def recherche(t, v):
    ''' Renvoie l'indice de l'élément v dans le tableau t.
    Si l'élément n'est pas trouver, renvoie -1.
    :param t: (list) un tableau d'entiers
    :param v: (int) l'entier à chercher
    :return: (int) l'indice de l'élément s'il est trouvé, ou -1 sinon '''

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
    Qu’observe-t-on ? La fonction est-elle **correcte** ?
    2. Ajouter des instructions `print` pour afficher les valeurs des variables au cours de l’exécution. Pour vous aider, vous pouvez également utiliser un `assert` pour tester l'**invariant**, ainsi qu'un `assert` pour tester le **variant**.  
    On rappelle l'**invariant** de la recherche dichotomique : "La valeur `v` est comprise entre l'élément d'indice `gauche` et d'indice `droite`" :  
    ```python
    assert v >= t[gauche] and v <= t[droite] ### ajout invariant
    ```  
    Pour ce qui est du **variant**, il s'agit de `droite - gauche + 1` (quantité **positive et strictement décroissante**). Il faut vérifier que cette quantité **diminue à chaque itération de la boucle**.

    3. Identifier la ou les erreurs à l’aide de ces traces et les corriger.

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

    1. Copier le programme ci-dessus dans l’éditeur de texte de **Thonny** et ajouter une instruction qui appelle la fonction tri avec le tableau `[4, 2, 6, 7, 1, 8]`.
    2. Exécuter le programme. Qu’observe-t-on ?
    3. Lancer le programme avec le **débogueur** de **Thonny** (l'icône juste à droite de celle permettant d'exécuter un script).
    4. Identifier la ou les erreurs à l’aide du débogueur et les corriger.