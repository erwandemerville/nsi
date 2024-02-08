# Cours - Algorithme de Boyer-Moore

!!! success ""
    L'**algorithme de Boyer-Moore** présent dans le **programme de terminale** est en réalité une **version simplifiée** de l'algorithme, appelée **algorithme de Boyer-Moore-Horspool**, qui consiste à ne garder que la **première table de saut** (règle du *mauvais caractère*).

    La **règle du bon suffixe** sera évoquée pour votre culture, mais n'est pas au programme.

## Vidéo récapitulative

Voici une petite **vidéo** récapitulant le **principe** de fonctionnement de l'**algorithme de Boyer-Moore-Horspool** (version **simplifiée** de l'**algorithme de Boyer-Moore**).  
*Source de la vidéo : [https://www.youtube.com/watch?v=9OYJ8L9R1F0](https://www.youtube.com/watch?v=9OYJ8L9R1F0){ target="_blank" }*.

![type:video](src/video_BMH.mp4)

## Animation

Voici une animation montrant le fonctionnement de l'algorithme de **Boyer-Moore-Horspool**.
Vous pouvez changer le *texte*, le *motif* (*pattern*), ainsi que la *vitesse d'animation* (*Animation Speed*).

<embed type="text/html" src="https://cmps-people.ok.ubc.ca/ylucet/DS/BoyerMoore.html" width="700" height="700"> 

## L'algorithme

La **table des sauts** (ou *table de décalage*) peut être **créée** avec l'**algorithme** suivant, ici écrit en *Python* :

```python
def decalage(motif):
    Dec = {}
    for i in range(len(motif) - 1):
        Dec[motif[i]] = len(motif) - 1 - i
    return Dec
```

À présent, on peut écrire l'**algorithme de Boyer-Moore-Horspool** de la manière suivante :

```python
def BMH(texte, motif):
    D = decalage(motif)  # création de la table des décalages
    i = len(motif) - 1  # stocker indice du dernier caractère du motif
    while i < len(texte):  # parcourir le texte
        b = True  # initialiser b à True
        for j in range(len(motif) - 1):  # parcourir le motif
            if texte[i - j] != motif[len(motif) - j - 1]:  # Comparer un caractère du motif avec un caractère du texte
                b = False  # si un caractère ne correspond pas, b passe à False
        if b:  # si b est resté à True, alors on a trouvé le motif
            return True  # on renvoie True
        # sinon :
        if texte[i] in D.keys():  # si le caractère i est dans le motif
            i = i + D[texte[i]]  # on décale le motif de la valeur (de la table de sauts D) associée au caractère présent à l'indice i du texte
        else:  # sinon
            i = i + len(motif)  # on décale le motif de la longueur du texte
    return False  # motif non trouvé : on renvoie False
```

## Aller plus loin

Pour aller plus loin, vous pouvez consulter le notebook `Boyer_Moore_BS_Eleve.ipynb` ci-dessous présentant la **règle du bon suffixe**, ainsi que le notebook `Boyer_Moore_complet.ipynb` implémentant l'**algorithme de Boyer-Moore complet**, utilisant à la fois la **règle du mauvais caractère** et la **règle du bon suffixe**.

!!! success "Notebooks"
    - [Boyer_Moore_BS.ipynb](src/Boyer_Moore_BS_Eleve.ipynb) - découverte de la règle du **bon suffixe**
    - [Boyer_Moore_complet.ipynb](src/Boyer_Moore_complet_Eleve.ipynb) - algorithme de **Boyer-Moore** avec la **règle du mauvais caractère** et la **règle du bon suffixe**