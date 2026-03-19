# Devoir surveillé corrigé - Les piles et les files

!!! success ""
    <center style="font-size:1.3em">
    [:material-cursor-default-click: Accéder au sujet de DS](docs/ds_piles_files.pdf)
    </center>

## Partie 1

!!! quote ""
    Source de la correction : [https://fabricenativel.github.io/Terminale/Annales/Corriges/22-NSIJ1PO1/#exercice-4](https://fabricenativel.github.io/Terminale/Annales/Corriges/22-NSIJ1PO1/#exercice-4)

!!! note "Exercice 1"
    Recopier sur la copie les lignes 6 et 8 en complétant les points de suspension.

??? tip "Correction exercice 1"

    ```python linenums="1" hl_lines="6 8"
    def est_triee(self):
        if not self.est_vide():
            e1 = self.depiler() 
            while not self.est_vide():
                e2 = self.depiler()
                if e1 > e2 :
                    return False
                e1 = e2
        return True
    ```

!!! note "Exercice 2"
    a. Donner la valeur renvoyée par l’appel `A.est_triee()`.  
    b. Donner le contenu de la pile `A` après l'exécution de cette instruction.

??? tip "Correction exercice 2"
    a. L'appel `A.est_triee()` renvoie `False` (le sommet de la pile `4` est supérieur à l'élément situé en dessous, le test ci-dessus ligne 6 est donc validé et `est_triee` renvoie `False`).  
    b. Après cet appel la pile `A` contient `[1,2]`, en effet seuls les deux premiers éléments ont été dépilés.

!!! note "Exercice 3"
    Recopier sur la copie les lignes 9 et 11 en complétant les points de suspension.

??? tip "Correction exercice 3"

    ```python linenums="1" hl_lines="9 11"
    def depileMax(self):
        assert not self.est_vide(), "Pile vide"
        q = Pile()
        maxi = self.depiler()
        while not self.est_vide():
            elt = self.depiler()
            if maxi < elt:
                q.empiler(maxi)
                maxi = elt
            else:
                q.empiler(elt)
        while not q.est_vide():
            self.empiler(q.depiler())
        return maxi
    ```

!!! note "Exercice 4"
    a. Donner le contenu des piles `B` et `q` à la fin de chaque itération de la boucle `while` de la ligne 5.  
    b. Donner le contenu des piles `B` et `q` avant l’exécution de la ligne 14.  
    c. Donner un exemple de pile qui montre que l'ordre des éléments restants n’est pas préservé après l’exécution de `depileMax`.

??? tip "Correction exercice 4"
    a.

    - Itération n° 1 : `B = [9, -7, 8]` et `q = [4]` (on a trouvé un nouveau maximum : `12`, on empile l'ancien dans la sauvegarde)
    - Itération n° 2: `B = [9, -7]` et `q = [4, 8]` (`8` n'est pas un nouveau maximum, on l'empile donc dans la sauvegarde)
    - Itération n° 3: `B = [9]` et `q = [4, 8, -7]`
    - Itération n° 3: `B = []` et `q = [4, 8, -7, 9]`

    b. Le contenu de la pile de sauvegarde `q` est empilé dans la pile de départ donc à la ligne 14, `B = [9, -7, 8, 4]` et `q = []`.

    c. On peut prendre l'exemple de la pile `[5, 2, 3]` :

    - Itération n°1 : `B = [5]` et `q = [2]` (`2` n'étant pas un nouveau maximum on l'a empilé et conservé `3` comme maximum courant)
    - Itération n°2 : `B = []` et `q = [2,3]` (`3` est empilé un nouveau maximum a été trouvé)
    - Dans la seconde boucle `while` on obtient alors `B = [3,2]` l'ordre n'est pas conservé.

!!! note "Exercice 5"
    a. Donner les contenus successifs des piles `B` et `q` :

    - avant la ligne 3,
    - avant la ligne 5,
    - à la fin de l’exécution de la fonction `traiter` lorsque la fonction `traiter` est appliquée sur la pile `B` contenant `[1, 6, 4, 3, 7, 2]`.

    b. Expliquer le traitement effectué par cette méthode.

??? tip "Correction exercice 5"
    a. Contenu des piles `B` et `q` :

    - avant la ligne 3 : `B = [1, 6, 4, 3, 7, 2]` et `q = []`
    - avant la ligne 5 : `B = []` et `q = [7, 6, 4, 3, 2, 1]`
    - à la fin de l'exécution de traiter() : `B = [1, 2, 3, 4, 6, 7]` et `q = []`

    b. Cette méthode permet de ranger par ordre croissant les éléments de la pile (la plus grande valeur se situe au sommet de la pile).

## Partie 2

!!! quote ""
    Source de la correction : [https://nsimeyroneinc.github.io/NSITerm/Annales/Corriges/23-NSIJ1G11/#exercice-3-6-points](https://nsimeyroneinc.github.io/NSITerm/Annales/Corriges/23-NSIJ1G11/#exercice-3-6-points)

!!! note "Exercice 1"
    **Recopier** et **compléter**, sur votre copie, les `...` des lignes **3 et 4** de la fonction `ajout(f)` qui permet de tirer au hasard une couleur et de l’ajouter à une séquence.
    La fonction `ajout` prend en paramètre la séquence `f` ; elle renvoie la séquence `f` modifiée (qui intègre la couleur ajoutée au format *chaîne de caractères*).

    ```python
    def ajout(f):
        couleurs = ("bleu", "rouge", "jaune", "vert")
        indice = randint(...,...)
        enfiler(...,...)
        return f
    ```

??? tip "Correction exercice 1"
    ```python linenums="1" hl_lines="3 4"
    def ajout(f):
        couleurs = ("bleu", "rouge", "jaune", "vert")
        indice = randint(0, 3)
        enfiler(f, couleur[indice])
        return f
    ```

!!! note "Exercice 2"
    **Écrire** la fonction `vider` qui prend en paramètre une séquence `f` et **la vide sans la renvoyer**.

??? tip "Correction exercice 2"
    ```python linenums="1"
    def vider(f):
        while not est_vide(f):
            defiler(f)
    ```

!!! note "Exercice 3"
    **Recopier** et **compléter**, sur la copie, les `...` des lignes **4 à 10** de la fonction `affich_seq(sequence)` ci-dessous :

    ```python linenums="1"
    def affich_seq(sequence):
        stock = creer_file_vide()
        ajout(sequence)
        while not est_vide(sequence) :
            c = ...
            ...
            time.sleep(0.5)
            ...
        while ... :
            ...
    ```

??? tip "Correction exercice 3"

    ```python linenums="1" hl_lines="5 6 8-10"
    def affich_seq(sequence):
        stock = creer_file_vide()
        ajout(sequence)
        while not est_vide(sequence):
            c = defiler(sequence)
            affichage(c)
            time.sleep(0.5)
            enfiler(stock, c)
        while not est_vide(stock):
            enfiler(sequence, defiler(stock))   
    ```

!!! note "Exercice 4"
    a. Afin d’obtenir la fonction `tour_de_jeu(sequence)` correspondant au comportement décrit ci-dessus, **recopier le script ci-dessous** et :
        - **Compléter** le `...`
        - **Choisir** parmi les **propositions de syntaxes suivantes** lesquelles correspondent aux **ZONES A, B, C, D, E et F** figurant dans le script et les y remplacer (il ne faut donc en choisir que six parmi les onze) :
            - `vider(sequence)`
            - `defiler(sequence)`
            - `enfiler(sequence,c_joueur)`
            - `enfiler(stock,c_seq)`
            - `enfiler(sequence, defiler(stock))`
            - `enfiler(stock, defiler(sequence))`
            - `affich_seq(sequence)`
            - `while not est_vide(sequence):`
            - `while not est_vide(stock):`
            - `if not est_vide(sequence):`
            - `if not est_vide(stock):`
        $~$
        ```python
        def tour_de_jeu(sequence):
            |ZONE A|
            stock = creer_file_vide()
            while not est_vide(sequence) :
                c_joueur = saisie_joueur()
                c_seq = |ZONE B|
                if c_joueur ... c_seq:
                    |ZONE C|
                else:
                    |ZONE D|
            |ZONE E|
                |ZONE F|
        ```
    $~$
    b. Proposer une modification pour que la fonction se répète si le joueur trouve toutes les couleurs de la séquence (dans ce cas, une nouvelle couleur est ajoutée) ou s’il se trompe (dans ce cas, la séquence est vidée et se voit ajouter une nouvelle couleur). On pourra ajouter des instructions qui ne sont pas proposées dans la question a.

??? tip "Correction exercice 4"
    a.

    ```python linenums="1" hl_lines="2 6-8 10-12"
    def tour_de_jeu(sequence):
        affich_seq(sequence)  # ZONE A
        stock = creer_file_vide()
        while not est_vide(sequence):
            c_joueur = saisie_joueur()
            c_seq = defiler(sequence)  # ZONE B
            if c_joueur == c_seq:
                enfiler(stock, c_seq)  # ZONE C
            else:
                vider(sequence)  # ZONE D
        while not est_vide(stock):  # ZONE E
            enfiler(sequence, defiler(stock))  # ZONE F
    ```

    b.
    Voici une solution possible à l'aide d'une boucle `while True` (permettant de répéter la fonction indéfiniment) :

    ```python linenums="1" hl_lines="2 12"
    def tour_de_jeu_modifie(sequence):
        while True:
            affich_seq(sequence)
            stock = creer_file_vide()
            while not est_vide(sequence):
                c_joueur = saisie_joueur()
                c_seq = defiler(sequence)
                if c_joueur == c_seq:
                    enfiler(stock, c_seq)
                else:
                    vider(sequence)
                    vider(stock)
            while not est_vide(stock):
                enfiler(sequence, defiler(stock))
    ```