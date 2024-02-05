# Cours - Algorithme de Boyer-Moore

!!! success ""
    L'**algorithme de Boyer-Moore** présent dans le **programme de terminale** est en réalité une **version simplifiée** de l'algorithme, appelée **algorithme de Boyer-Moore-Horspool**, qui consiste à ne garder que la **première table de saut** (règle du *mauvais caractère*).

    La **règle du bon suffixe** sera évoquée pour votre culture, mais n'est pas au programme.

## Vidéo récapitulative

Voici une petite **vidéo** récapitulant le **principe** de fonctionnement de l'**algorithme de Boyer-Moore-Horspool** (version **simplifiée** de l'**algorithme de Boyer-Moore**).  
*Source de la vidéo : [https://www.youtube.com/watch?v=9OYJ8L9R1F0](https://www.youtube.com/watch?v=9OYJ8L9R1F0){ target="_blank" }*.

![type:video](src/video_BMH.mp4)

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
    while i < len(texte):
        b = True
        for j in range(len(motif) - 1):
            if texte[i - j] != motif[len(motif) - j - 1]:
                b = False
        if b:
            return True
        if texte[i] in D.keys():
            i = i + D[texte[i]]
        else:
            i = i + len(motif)
    return False
```