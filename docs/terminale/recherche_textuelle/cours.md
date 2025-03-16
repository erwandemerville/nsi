# Cours - Algorithme de Boyer-Moore

!!! success ""
    L'**algorithme de Boyer-Moore** présent dans le **programme de terminale** est en réalité une **version simplifiée** de l'algorithme, appelée **algorithme de Boyer-Moore-Horspool**, qui consiste à ne garder que la **première table de saut** (règle du *mauvais caractère*).

    La **règle du bon suffixe** sera évoquée pour votre culture, mais n'est pas au programme.

## Rappel - Recherche textuelle naïve

Avant de voir l'algorithme de **Boyer-Moore**, rappelons la méthode de **recherche textuelle** "naïve", qui consiste à rechercher un *motif* dans un *texte* en **parcourant tout le texte** et en comparant le *motif* à chaque nouveau caractère rencontré.

!!! abstract "Algorithme de recherche d'un motif dans un texte"
    <div style="font-size:1.1em">
    **ALGORITHME** : recherche  
    **ENTRÉES** :  
    &emsp;&emsp;`texte` : texte dans lequel rechercher - **chaîne de caractères**  
    &emsp;&emsp;`motif` : motif à rechercher dans le texte - **chaîne de caractères**  
    **SORTIE** : position (*indice*) de la **première occurence** de `motif` dans `texte`, ou `-1`

    **DÉBUT ALGORITHME**  
    &emsp;&emsp;**POUR** i **ALLANT DE** 0 **À** longueur(texte) $-$ longueur(motif) :  
    &emsp;&emsp;&emsp;&emsp;j ← 0  
    &emsp;&emsp;&emsp;&emsp;**TANT QUE** j $<$ longueur(motif) **ET QUE** texte[i $+$ j] $=$ motif[j] :    
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;j ← j $+$ 1  
    &emsp;&emsp;&emsp;&emsp;**FIN TANT QUE**  
    &emsp;&emsp;&emsp;&emsp;**SI** j $=$ longueur(motif), **ALORS** :  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**Renvoyer** i  
    &emsp;&emsp;&emsp;&emsp;**FIN SI**  
    &emsp;&emsp;**FIN POUR**  
    &emsp;&emsp;**Renvoyer** -1  
    **FIN ALGORITHME**
    </div>

*Note* : On s'arrête à `longueur(tableau) - longueur(motif)` de manière à éviter de dépasser la **taille du texte** lors des comparaisons.

En langage *Python*, cet algorithme pourrait s'écrire ainsi :

```python
def recherche(texte: str, motif: str) -> 'list[int]':
    ''' Renvoie une liste des positions d'un motif dans un texte. '''
    
    res = []
    for i in range(len(texte) - len(motif) + 1):
        j = 0
        while j < len(motif) and texte[i + j] == motif[j]:
            j += 1
        if j == len(motif):
            res.append(i)
    return res
```

## Boyer-Moore-Horspool - Vidéo explicative

Voici une petite **vidéo** récapitulant le **principe** de fonctionnement de l'**algorithme de Boyer-Moore-Horspool** (version **simplifiée** de l'**algorithme de Boyer-Moore**).  
*Source de la vidéo : [https://www.youtube.com/watch?v=9OYJ8L9R1F0](https://www.youtube.com/watch?v=9OYJ8L9R1F0){ target="_blank" }*.

![type:video](src/video_BMH.mp4)

## Animation

Voici une animation montrant le fonctionnement de l'algorithme de **Boyer-Moore-Horspool**.
Vous pouvez changer le *texte*, le *motif* (*pattern*), ainsi que la *vitesse d'animation* (*Animation Speed*).

<center style="font-size: 1.4em">
[:octicons-link-external-16: Accéder à l'animation](https://cmps-people.ok.ubc.ca/ylucet/DS/BoyerMoore.html)
</center>

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
def boyer_moore(texte, motif):
    decale = decalage(motif)  # définir la table de décalage du motif
    i = len(motif) - 1  # variable de boucle de la première boucle (parcours du texte)
    while i < len(texte):  # tant qu'on a pas parcouru tout le texte
        j = 0  # variable de boucle de la deuxième boucle (parcours du motif)
        while j < len(motif) and texte[i - j] == motif[len(motif) - 1 - j]:  # tant qu'on a pas parcouru tout le motif et que les caractères correspondent
            j += 1  # on incrémente j

        # vérifier si on a parcouru tout le motif
        if j == len(motif):
            return i - len(motif) + 1  # renvoyer la position du motif dans le texte
        
        # décaler i en fonction de la table de décalage
        if texte[i] in decale:  # regarder si le caractère d'indice i du texte est dans le motif
            i += decale[texte[i]]  # si oui, on décale selon la valeur stockée dans la table de décalage
        else:  # sinon
            i += len(motif)  # on décale de la longueur du motif
    return -1
```

## Aller plus loin

Pour aller plus loin, vous pouvez consulter le notebook `Boyer_Moore_BS_Eleve.ipynb` ci-dessous présentant la **règle du bon suffixe**, ainsi que le notebook `Boyer_Moore_complet.ipynb` implémentant l'**algorithme de Boyer-Moore complet**, utilisant à la fois la **règle du mauvais caractère** et la **règle du bon suffixe**.

!!! success "Notebooks"
    - [Boyer Moore avec la règle du bon suffixe](https://capytale2.ac-paris.fr/web/c/c676-5756802) - découverte de la règle du **bon suffixe**
    - [Boyer Moore complet](https://capytale2.ac-paris.fr/web/c/f0a8-5756846) - algorithme de **Boyer-Moore** avec la **règle du mauvais caractère** et la **règle du bon suffixe**

Voici également une petite **vidéo** expliquant le principe de la **règle du bon suffixe** :

<iframe width="560" height="315" src="https://www.youtube.com/embed/YGejqMcfu98?si=GYhF6-mvBowpg-j1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>