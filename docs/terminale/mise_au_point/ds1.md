# Corrigé DS n°1

!!! success "Énoncé PDF"
    Vous pouvez télécharger ici l'**énoncé du DS n°1** au format *PDF* :

    <center style="font-size: 1.3em">
    [Télécharger l'énoncé du DS](pdf/ds1.pdf)
    </center>

---

## Un module `adn`

Les **molécules d'ADN** présentes dans les cellules vivantes contiennent l'**information génétique** et permettent le développement, le fonctionnement et la reproduction des êtres vivants. L'**ADN** est formé de **deux brins** qui sont une succession de **nucléotides** portant chacun une **base azotée**.

Les quatre **bases azotées** sont l'*adénine (A)*, la *thymine (T)*, la *cytosine (C)* et la *guanine (G)*.  
Elles s'associent deux par deux : *A* avec *T* d'une part, *C* avec *G* d'autre part. 

!!! note "Exercice 1"
    Le but de l'exercice est de définir un **module** `adn` contenant la **constante** et les **fonctions** suivantes :

    1. La constante `BASES_ASSOCIEES = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}`.
    2. La fonction `sequence_alea` qui prend en paramètre d'entrée un entier `n` positif et renvoie une **séquence d'ADN aléatoire** de longueur `n` sous la forme de **chaîne de caractères**.
    3. La fonction `complementaire` qui prend en paramètre d'entrée une **chaîne de caractères** `brin` et renvoie le **brin complémentaire** sous forme de **chaîne de caractères**.
    4. La fonction `proportionAT` qui prend en paramètre d'entrée une **chaîne** `brin` et renvoie la **proportion** de **bases** *A/T* présentes dans le **brin**. Le valeur renvoyée est donc un **flottant**.

    **Implémentez** ce module `adn`, en **documentant chaque fonction** à l'aide d'une **docstring** contenant *ce que fait la fonction*, la *liste de ses paramètres d'entrée et leur type* ainsi que le *type de la valeur de retour*.

!!! tip "Aide - Exercice 1"
    - Pour la fonction `sequence_alea`, vous pourrez utiliser la fonction `choice` du module `random`, qui renvoie une **valeur aléatoire dans une liste**.
    - Pour la fonction `proportionAT`, on calcule la **proportion** en divisant le **nombre de bases** *A* et *T* par la **longueur du brin** d'ADN.

??? tip "Correction - Exercice 1"
    Voici le **module** `adn` corrigé :

    ```python
    from random import choice  # importer fonction choice du module random

    # Définir constante BASES_ASSOCIEES :
    BASES_ASSOCIEES = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

    def sequence_alea(n: int) -> str:
        ''' Renvoie une séquence ADN aléatoire de longueur n
        sous la forme de chaîne de caractères.
        :param n: (int) taille de la séquence à générer
        :return: (str) une séquence ADN aléatoire '''
        
        res = ""
        bases = [key for key in BASES_ASSOCIEES]
        for _ in range(n):
            res += choice(bases)
        return res

    def complementaire(brin: str) -> str:
        ''' Renvoie le brin complémentaire du brin donné.
        :param brin: (str) un brin d'ADN
        :return: (str) le brin complémentaire '''
        
        res = ""
        for base in brin:
            res += BASES_ASSOCIEES[base]
        return res

    def proportionAT(brin: str) -> float:
        ''' Renvoie la proportion de bases A/T présentes dans le brin.
        :param brin: (str) un brin d'ADN
        :return: (float) proportion de bases A/T '''
        
        compteur = 0
        for base in brin:
            if base == 'A' or base == 'T':
                compteur += 1
        return compteur / len(brin)
    ```

!!! note "Exercice 2"
    On souhaite maintenant utiliser ce module `adn` (écrit dans un fichier `adn.py`).\newline

    Écrivez un **nouveau script** *Python* (incluant les **imports** nécessaires du module `adn`) qui réalise le programme suivant :

    - demande à l'utilisateur de saisir un nombre `n`,
    - génère `n` séquences d'ADN aléatoires de taille `10`,
    - **affiche** enfin la **plus grande proportion** de bases *A/T* parmi toutes les **séquences** générées, ainsi que la **séquence** associée.  
    Exemple d'affichage : `"séquence : ATCTCGCATA - proportion : 0.6"`.

    Pour rappel, la fonction `input` permet de demander à l'utilisateur de saisir une valeur, et de la récupérer sous la forme d'une **chaîne de caractères** (il sera donc peut-être nécessaire de convertir la valeur en `int` en utilisant la fonction `int()`).

    Il n'est pas nécessaire d'écrire une *docstring* ici.

??? tip "Correction - Exercice 2"
    Dans un **nouveau script** *Python*, il faut donc **importer le module** `adn` que nous avons créé afin d'utiliser ses **fonctions** dans notre programme.

    En l'occurence, j'ai fait le choix d'importer **uniquement** les **fonctions nécessaires**, c'est-à-dire `sequence_alea` et `proportionAT`.

    ```python
    from adn import sequence_alea, proportionAT

    n = int(input("Saisissez un nombre n : "))  # demander à l'utilisateur de saisir un nombre
    sequence_max = None  # initialiser la séquence avec le max de bases A/T à None
    proportion_max = 0  # initialiser la proportion max de bases A/T à 0
    for _ in range(n):  # itérer n fois
        sequence = sequence_alea(10)  # générer une séquence ADN de taille 10
        proportion = proportionAT(sequence)  # obtenir la proportion de bases A/T
        if proportion > proportion_max:  # si la proportion de bases A/T est supérieure au max actuel
            proportion_max = proportion  # on remplace la proportion max actuelle par celle que l'on a trouvé
            sequence_max = sequence  # on remplace l'ancienne séquence stockée par la nouvelle
    print(f'séquence : {sequence_max} - proportion : {proportion_max}')  # afficher résultat
    ```

    On peut également importer le module `adn` avec l'instruction `import adn`, auquel cas l'appel des **fonctions** du module sera de la forme `adn.<NOM_FONCTION>`, comme ceci :

    ```python
    import adn

    n = int(input("Saisissez un nombre n : "))
    sequence_max = None
    proportion_max = 0
    for _ in range(n):
        sequence = adn.sequence_alea(10)
        proportion = adn.proportionAT(sequence)
        if proportion > proportion_max:
            proportion_max = proportion
            sequence_max = sequence
    print(f'séquence : {sequence_max} - proportion : {proportion_max}')
    ```

## Mise au point et tests

