# Exercices sur les piles

!!! tip "Classe `Pile`"
    Pour réaliser les exercices suivants, vous pouvez réutiliser une classe `Pile` déjà créée.

    Si besoin, vous pouvez [télécharger ce fichier `pile.py`](src/pile.py) implémentant une classe `Pile` avec les **opérations de base** (*méthodes* de la classe) suivantes :

    - `est_vide()` : renvoie `True` si la *pile* est vide, `False` sinon,
    - `empiler(elt)` : ajouter l'*élément* donné au *sommet* de la *pile*,
    - `depiler()` : retire et renvoie l'*élément* situé au *sommet* de la *pile*,
    - `obtenir_element()` : renvoie l'élément situé au sommet de la *pile* sans le retirer.

    Pour utiliser cette classe `Pile` dans un nouveau programme, placez ce fichier `pile.py` dans le même répertoire que votre nouveau programme, et ajoutez en tête de votre fichier :

    ```python
    from pile import Pile
    ```

!!! note "Exercice 1"
    On souhaite utiliser une **pile** pour vérifier si une **expression arithmétique** est **bien parenthésée**. Écrire une fonction `bien_parenthesee(chaine)` qui renvoie `True` si l'expression est **bien parenthésée**, `False` sinon.

    Par exemple :  
    `bien_parenthesee("(1 + 3) * (6 + 7)")` renverra `True`.  
    `bien_parenthesee("(6 + (4 * 5) - (2 + 1)")` renverra `False`.

    ```python
    def bien_parenthesee(txt):
        ''' Renvoie True si l'expression donnée est bien parenthésée, False sinon.
        :param txt: (str) une expression arithmétique
        :return: (bool) True ou False '''
        
        ...
    ```

!!! tip "Aide exercice 1"
    En cas de difficulté, vous pouvez jeter un oeil à la *partie 3* du [TD/TP papier sur les piles](docs/LES_PILES.pdf). Vous y trouverez une proposition d'**algorithme** écrit en *pseudo-code*.

{% if exercices.terminale.pilesfiles.exercices.exo1 %}
??? tip "Correction exercice 1"

    ```python
    def est_bien_parenthesee(chaine):
        pile = Pile()
        for c in chaine:
            if c == "(":
                pile.empiler(c)
            elif c == ")":
                if pile.est_vide():
                    return False
        return pile.est_vide()
    ```
{% endif %}

!!! note "Exercice 2"
    L'écriture polonaise inverse des expressions arithmétiques place l'opérateur après ses opérandes. Cette notation ne nécessite aucune parenthèse ni aucune règle de priorité. Ainsi, l'expression polonaise inverse décrite par la chaîne de caractères `1 2 3 * + 4 *` désigne l'expression traditionnellement notée $(1 + 2 \times 3) \times 4$. 

    La valeur d'une telle expression peut être calculée facilement en utilisant une **pile** pour stocker **les résultats intermédiaires**. Pour cela, on observe un à un les éléments de l'expression et on effectue les actions suivantes:
    
    - si on voit un nombre, on le place sur la pile;
    - si on voit un opérateur binaire, on récupère les deux nombres au sommet de la pile, on leur applique l'opérateur, et on replace le résultat sur la pile.
  
    Si l'expression était bien écrite, il y a bien toujours deux nombres sur la pile lorsque l'on voit un opérateur, et à la fin du processus il reste exactement un nombre sur la pile, qui est le résultat.
    
    **Écrire** une **fonction** prenant en **paramètre** une **chaîne de caractères** représentant une expression en **notation polonaise inverse** composée d'**additions** et de **multiplications** de **nombres entiers** et **renvoyant la valeur de cette expression**. On supposera que les éléments de l'expression sont séparés par des **espaces**.
    
    *Attention* : cette fonction ne doit pas renvoyer de résultat si l'expression est mal écrite.

    ```python
    def polonaise(liste):
        ''' Renvoie la valeur d'une expression polonaise inverse.
        :liste: (lst) une expresion sous forme d'une liste
        :return: (int ou float) résultat de l'expression '''

        ...
    ```

!!! tip "Aide exercice 2"
    En cas de difficulté, vous pouvez jeter un oeil à la *partie 4* du [TD/TP papier sur les piles](docs/LES_PILES.pdf). Vous y trouverez une proposition d'**algorithme** écrit en *pseudo-code*.

{% if exercices.terminale.pilesfiles.exercices.exo2 %}
??? tip "Correction exercice 2"
    On **itère** sur les **éléments obtenus** en **découpant la chaîne** au niveau des **espaces**. 
    On isole d'abord les cas des opérateurs, qui sont les plus faciles à identifier, et on suppose que tout ce qui n'est pas `+` ou `*` est un **entier** (cette branche échouera si on trouve encore autre chose dans l'expression).
    
    À la fin, on **dépile** le **dernier élément** et on **vérifie** que la **pile** est bien **vide** avant de **renvoyer ce résultat**. Si à un moment donné, il était **impossible de dépiler**, alors le programme aura de toute façon **échoué**.
    
    ```python
    def eval_polonaise_inverse(s):
        pile = Pile()
        for e in s.split(" "):
            if e == "+" or e == "*":
                x = pile.depiler()
                y = pile.depiler()
                z = x + y if e == "+" else x * y
                pile.empiler(z)
            else:
                pile.empiler(int(e))
        res = pile.depiler()
        assert pile.est_vide()
        return res
    ```
{% endif %}