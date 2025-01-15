# Implémentation d'un arbre binaire de recherche

L'implémentation d'un **arbre binaire de recherche** peut se faire de la même façon que celle d'un **arbre binaire** classique. On va ici réutiliser notre **classe** `Arbre` créée lors de [l'activité précédente](implementation_arbres.md){: target="_blank" }.

Cette activité sera divisée en deux parties, qui consisteront à :

* écrire des méthodes permettant de vérifier si un **arbre binaire** est un **arbre binaire de recherche**,
* écrire une méthode de **recherche** et d'**insertion** dans un **arbre binaire de recherche**.

*Note* : Par la suite, pour simplifier la rédaction, on utilisera parfois le terme "arbre" pour désigner un arbre binaire.

!!! abstract "Opérations de base"
    En plus des opérations $est\_vide$, $est\_feuille$, $gauche$, $droite$, $racine$, $valeur\_racine$ et $parcours\_infixe$ déjà vues, on définit ici de **nouvelles opérations**.

    **Trois opérations** visant à vérifier si l'**arbre binaire** est un **arbre binaire de recherche** :
    
    * $maximum : Arbre \rightarrow Int$ : Renvoie la **valeur maximale** parmi les **valeurs** des **noeuds** d'un **arbre binaire NON vide**.
    * $minimum : Arbre \rightarrow Int$ : Renvoie la **valeur minimale** parmi les **valeurs** des **noeuds** d'un **arbre binaire NON vide**.
    * $est\_ABR :~Arbre \rightarrow Bool$ : Renvoie *True* si un **arbre binaire** est un **arbre binaire de recherche**, *False* sinon.
    
    Dans le cas où l'arbre binaire est un **arbre binaire de recherche**, les opérations de **recherche** et d'**insertion** sont ainsi définies :
    
    * $rechercher :~Arbre \times Element \rightarrow Bool$ : Renvoie *True* s'il existe un **noeud de l'arbre binaire de recherche** contenant la **valeur donnée**, *False* sinon.
    * $inserer :~Arbre \times Element \rightarrow Arbre$ : Insère un **nouveau noeud** de **valeur donnée** à sa **bonne position dans l'arbre binaire de recherche**.

---

Pour cette activité, on écrira **toutes les opérations sous la forme de méthodes**. 

??? info "Rappel concernant la création et l'appel de méthodes"
    Une **méthode** est une **fonction** définie **à l'intérieur d'une classe**.
    Elle prend toujours un paramètre **self**, puis éventuellement d'autres paramètres :

    ```python
    class Arbre:
        def __init__(self, valeur_racine=None, gauche=None, droite=None):
        	# Une méthode spéciale : le constructeur de la classe
            ...
    
        def gauche(self: 'Arbre') -> 'Arbre':
        	# Renvoie le sous-arbre gauche de l'arbre
            ...

        def droite(self: 'Arbre') -> 'Arbre':
        	# Renvoie le sous-arbre droit de l'arbre
            ...
            
        def est_vide(self: 'Arbre') -> bool:
        	# Renvoie True si l'arbre est vide, False sinon
            ...
            
        def est_present(self: 'Arbre', val: 'int|str') -> bool:
        	# Renvoie True s'il existe un noeud de valeur val dans l'arbre, False sinon
            ...
    ```
    Lors de l'**appel à une méthode**, on ne donne pas d'argument pour le paramètre **self** car il correspond à l'**adresse de l'objet** sur lequel **elle est appelée**.<br />
    Si l'on souhaite par exemple savoir si le **sous-arbre gauche** d'un **arbre binaire** dont l'adresse est stockée dans une **variable** `ab` est **vide**, il faudra écrire :
    ```python
    ab.gauche().est_vide()
    ```
    Si l'on souhaite maintenant savoir si le **sous-arbre droit** d'un **arbre binaire** dont l'adresse est stockée dans une **variable** `ab` contient un **noeud de valeur 42**, il faudra écrire :
    ```python
    ab.droite().est_present(42)
    ```

!!! success "À télécharger"
    Récupérez le fichier suivant :

    * [abr.py](src/abr.py){: target="_blank" } - Classe `Arbre` à compléter représentant un **arbre binaire** avec les nouvelles méthodes relatives aux **arbres binaires de recherche**.
    
    ??? info "Si vous souhaitez utiliser les fonctions de dessin avec *Graphviz*"
    
        Ce n'est pas obligatoire, mais si vous souhaitez, comme pour l'activité précédente, pouvoir afficher un dessin de votre arbre, les fichiers à avoir sur votre machine sont toujours les mêmes :
    
        * [dessin.py](src/dessin.py){: target="_blank" } - Quelques fonctions annexes utilisées pour dessiner un arbre avec le module `Graphviz`. (Vous n'avez pas besoin d'ouvrir ou de modifier ce fichier.)
    
        Si vous utilisez les **machines du *lycée*** (sinon, voir [cette page](implementation_arbres.md) pour la procédure pour installer *Graphviz* chez vous) :
    
        * [windows_graphviz.zip](src/windows_graphviz.zip){: target="_blank" } - Décompressez l'archive **dans le répertoire où se trouvent vos fichiers Python**. Vous devez avoir `abr.py`, `dessin.py` et un dossier `Graphviz` au même endroit.<br />Contient les exécutables de *Graphviz*.

    	---

        Pour utiliser les fonctions de `dessin.py`, vous devez également **dé-commenter** la **première ligne** `from dessin import dessiner` du fichier `abr.py`, qui a été commentée pour éviter les erreurs.

??? tip "Correction complète"
    Voici une **correction complète** des **méthodes** et **fonctions** du fichier `abr.py`.

    <center style="font-size:1.4em">
    [Télécharger le fichier `abr_corr.pu`](src/abr_corr.py)
    </center>

!!! info "Important"
    Ici, on a fait le choix de travailler avec une structure **immuable**.<br />
    En l'occurence, la méthode `inserer` **renvoie** un **nouvel arbre binaire de recherche**, et **ne modifie pas** directement l'arbre sur lequel elle est appelée.

!!! info "Tester son programme avec le module *doctest*"
    Plusieurs tests ont été rédigés dans la **docstring** du **constructeur** de la classe. Rien ne vous empêche de rajouter davantage de tests si vous le souhaitez.

    Pour tester votre programme, vous avez simplement à **exécuter celui-ci**, et s'il n'y a pas d'erreurs, il ne se passera **rien**. S'il y a des erreurs, vous obtiendrez des détails sur les tests qui n'ont pas fonctionné.
    
    Pour activer le mode "verbeux" et obtenir encore plus de détails sur les erreurs, vous pouvez passer le paramètre `verbose` à `True` (sur la toute dernière ligne du programme).

## Maximum et minimum

Pour pouvoir écrire une **méthode** permettant de définir si un **arbre binaire est un arbre binaire de recherche**, on se propose d'abord d'écrire **deux méthodes** permettant de déterminer la **valeur minimale** et la **valeur maximale** des **noeuds** d'un **arbre binaire** de manière générale.

Ces deux fonctions :

* ne sont **définies** que pour des **arbres binaires non vides**, comme indiqué dans les **CU** (**C**onditions d'**U**tilisation) de la fonction,
* nécessitent d'identifier **un cas de base** et **plusieurs cas récursifs**.

Vous pourrez utiliser les fonctions `min` et `max` de **Python**, qui renvoient respectivement le **minimum** et le **maximum** parmi plusieurs éléments, ou parmi les éléments d'une liste/d'un tuple.

!!! note "Exercice 1"
    Écrire le **code Python** des méthodes `minimum` et `maximum`.

??? tip "Aide - Exercice 1"
    Vous pouvez distinguer les **4 cas suivants** :

    * Le cas où l'arbre donné **est une feuille** (= **sous-arbres gauche** et **droit vides**), qui est le **cas de base**
    * Le cas où le **sous-arbre gauche uniquement est vide**
    * Le cas où le **sous-arbre droit uniquement est vide**
    * Le cas où **les deux sous-arbres sont NON vides**

??? tip "Encore plus d'aide - Exercice 1"
    Voici une partie du code, **à compléter**.

    ```python
    def minimum(self: 'Arbre') -> int:
    ''' Renvoie la valeur minimale des noeuds de l'arbre
    :CU: L'arbre n'est PAS vide '''
    
    if self.est_feuille():
        ...
    elif self.gauche().est_vide():
        return min(self.valeur_racine(), self.droite().minimum())
    elif self.droite().est_vide():
        ...
    else:
        ...
    ```

??? tip "Solution - Exercice 1"
    ```python
    def minimum(self: 'Arbre') -> int:
    ''' Renvoie la valeur minimale des noeuds de l'arbre
    :CU: L'abre n'est PAS vide '''

    if self.est_feuille():
        return self.valeur_racine()
    elif self.gauche().est_vide():
        return min(self.valeur_racine(), self.droite().minimum())
    elif self.droite().est_vide():
        return min(self.valeur_racine(), self.gauche().minimum())
    else:
        return min(self.gauche().minimum(), self.valeur_racine(), self.droite().minimum())

    def maximum(self: 'Arbre') -> int:
    ''' Renvoie la valeur maximale des noeuds de l'arbre
    :CU: L'arbre n'est PAS vide '''

    if self.est_feuille():
        return self.valeur_racine()
    elif self.gauche().est_vide():
        return max(self.valeur_racine(), self.droite().maximum())
    elif self.droite().est_vide():
        return max(self.valeur_racine(), self.gauche().maximum())
    else:
        return max(self.gauche().maximum(), self.valeur_racine(), self.droite().maximum())
    ```

## La méthode `est_abr`

On peut maintenant écrire une méthode qui permet de vérifier qu'un **arbre binaire** créé avec la classe `Arbre` soit un **arbre binaire de recherche**.

Un **arbre binaire est un arbre binaire de recherche si** :

* l'**arbre est vide** ou **est une feuille**,

OU BIEN

* si le **sous-arbre gauche** n'est **pas vide**, les *éléments* des **noeuds** du **sous-arbre gauche** sont tous $\leq$ à l'*élément* de la **racine**, ET
* si le **sous-arbre droit** n'est **pas vide**, les *éléments* des **noeuds** du **sous-arbre droit** sont tous $>$ à l'*élément* de la **racine**, ET
* les **sous-arbres gauches** et **droit** sont **également** des **arbres binaires de recherche**.

La fonction `est_abr` **renvoie donc *False*** si l'**une de ces conditions** n'est **pas remplie**, et renvoie *True* sinon.

!!! note "Exercice 2"
    Écrire le **code Python** de la méthode `est_abr`.

??? tip "Aide - Exercice 2"
    Le cas où l'**arbre est vide** ou l'**arbre est une feuille** est le **cas de base**, non récursif. Dans ce cas-là, on considère que l'arbre **est un arbre binaire de recherche**. On renverra donc *True* si l'on se trouve dans l'un de ces deux cas.

    Il ne reste plus qu'à vérifier les trois autres conditions évoquées précédemment. Une solution est de **vérifier**, pour **chaque condition**, si elle n'**est pas remplie**, et de renvoyer *False* le cas échéant. Une fois que les trois conditions ont été vérifiées, on renvoie donc *True*.

??? tip "Encore plus d'aide - Exercice 2"
    Voici une partie du code, **à compléter**.

    ```python
    def est_ABR(self: 'Arbre') -> bool:
    ''' Renvoie True si l'arbre binaire est un arbre binaire de recherche, False sinon. '''
    
    if self.est_vide() or self.est_feuille():
        return ...
    else:
        if not self.gauche().est_vide() and self.gauche().maximum() > self.valeur_racine():
            return ...
        if ... and ... :
            return ...
        if ... or ... :
            return ...
        return ...
    ```

??? tip "Solution - Exercice 2"

    ```python
    def est_ABR(self: 'Arbre') -> bool:
    ''' Renvoie True si l'arbre binaire est un arbre binaire de recherche, False sinon. '''
    
    if self.est_vide() or self.est_feuille():
        return True
    else:
        if not self.gauche().est_vide() and not self.gauche().maximum() <= self.valeur_racine():
            return False
        if not self.droite().est_vide() and not self.droite().minimum() > self.valeur_racine():
            return False
        if not self.gauche().est_ABR() or not self.droite().est_ABR():
            return False
        return True
    ```

Une autre solution plus simple pour vérifier si un arbre binaire **est un arbre binaire de recherche** est de vérifier **si la liste des valeurs des noeuds visités en ordre infixe est triée**.

!!! note "Exercice 3"
    Complétez le corps de la méthode `est_ABR_v2`.

??? tip "Aide - Exercice 3"
	Il suffit simplement de vérifier que la liste `lst_valeurs` soit **triée** en la **parcourant** et en vérifiant que **chaque élément** soit **supérieur** à l'**élément qui le précède**. Si l'on se rend compte qu'un élément est inférieur à son prédecesseur, on renvoie *False*. Sinon, on renvoie *True*.

??? tip "Solution - Exercice 3"

    ```python
    def est_ABR_v2(self: 'Arbre') -> bool:
    ''' Renvoie True si l'arbre binaire est un arbre binaire de recherche, False sinon.
    Autre version, vérifiant si la liste des noeuds visités en ordre infixe est triée dans l'ordre croissant. '''
    
    lst_valeurs = self.parcours_infixe()  # Récupérer la liste des valeurs des noeuds visités en parcours infixe
    for i in range(len(lst_valeurs) - 1):
        if not lst_valeurs[i] <= lst_valeurs[i + 1]:
            return False
    return True
    ```

## Recherche dans un arbre binaire de recherche

!!! warning "À savoir pour le bac"
    L'algorithme de **recherche** dans un **arbre binaire de recherche** fait partie des algorithmes à maîtriser pour le baccalauréat.

Comme cela a été vu dans les [exercices](exercices_abr.md), la **rercherche** dans un **arbre binaire de recherche** se déroule de la manière suivante.

!!! info "Déroulement `rechercher`"
    **Précondition** : l'**arbre donné** est un **arbre binaire de recherche**.
    L'algorithme `rechercher` se déroule comme suit :

    * Si l'**arbre binaire est vide** : on renvoie *Faux*.
    * Sinon (*l'arbre binaire n'est pas vide*):
        * Si la **valeur** de la **racine de l'arbre** est **égale** à l'**élément recherché** : on renvoie *Vrai*.
        * Sinon, si l'**élément recherché** est **inférieur ou égal** à la **valeur** de la **racine de l'arbre**, `rechercher` l'élément dans le **sous-arbre gauche**.
        * Sinon, on `rechercher` l'élément dans le **sous-arbre droit**.

!!! note "Exercice 4"
    En vous aidant du déroulement décrit ci-dessus, écrire le **code Python** de la méthode `rechercher`.<br />
    *Remarque* : On aura pas besoin de rajouter une condition dans le code pour vérifier si l'arbre binaire est bien un arbre binaire de recherche, car cela a été **spécifié** en tant que **précondition** (ou *CU*, pour *condition d'utilisation*) :<br /> `''' :CU: self.est_ABR() == True '''`

??? tip "Solution - Exercice 4"

    ```python
    def rechercher(self: 'Arbre', elt: 'int|str') -> bool:
    ''' Recherche l'élément elt dans l'arbre, renvoie True s'il est trouvé, False sinon.
    :CU: self.est_ABR() == True '''
    
    if self.est_vide():
        return False
    elif self.valeur_racine() == elt:
        return True
    elif elt <= self.valeur_racine():
        return self.gauche().rechercher(elt)
    else:
        return self.droite().rechercher(elt)
    ```

## Insertion dans un arbre binaire de recherche

!!! warning "À savoir pour le bac"
    L'algorithme d'**insertion** dans un **arbre binaire de recherche** fait partie des algorithmes à maîtriser pour le baccalauréat.

Enfin, l'**insertion dans un arbre binaire de recherche** est assez similaire à la **recherche**.

!!! info "Déroulement `inserer`"
    **Précondition** : l'**arbre donné** est un **arbre binaire de recherche**.
    L'algorithme `inserer` se déroule comme suit :

    * Si l'**arbre binaire est vide** : on renvoie une **nouvelle feuille** contenant l'**élément à insérer**.
    * Sinon (*l'arbre binaire n'est pas vide*):
        * Si l'**élément à insérer** est **inférieur ou égal** à la **valeur** de la **racine de l'arbre**, `inserer` l'élément dans le **sous-arbre gauche**. On **renvoie** l'arbre résultant de cette insertion.
        * Sinon, `inserer` l'élément dans le **sous-arbre droit**. On **renvoie** l'arbre résultant de cette insertion.

!!! note "Exercice 5"
    En vous aidant du déroulement décrit ci-dessus, écrire le **code Python** de la méthode `inserer`. **Attention**, `inserer` doit toujours **renvoyer un objet de type `Arbre`**.<br />
    *Remarque* : Ici également, on aura pas besoin de rajouter une condition dans le code pour vérifier si l'arbre binaire est bien un arbre binaire de recherche.

??? tip "Solution - Exercice 5"

    ```python
    def inserer(self: 'Arbre', elt: 'int|str') -> 'Arbre':
    ''' Insère l'élément elt dans l'arbre 
    :CU: self.est_ABR() == True '''
    
    if self.est_vide():
        return Arbre(elt, Arbre(), Arbre())
    elif elt <= self.valeur_racine():
        return Arbre(self.valeur_racine(), self.gauche().inserer(elt), self.droite())
    else:
        return Arbre(self.valeur_racine(), self.gauche(), self.droite().inserer(elt))
    ```

## Trier une liste avec un arbre binaire de recherche

!!! note "Exercice 6"
    Compléter la **fonction** `trier` qui prend une **liste d'éléments** et **renvoie une nouvelle liste** contenant les mêmes éléments, mais **triés** par **ordre croissant**. Vous devez pour cela utiliser un **arbre binaire de recherche** et la méthode `parcours_infixe`.

    **Attention** : Il s'agit d'une **fonction placée en dehors de la classe**, et non pas d'une **méthode** de `Arbre`.

??? tip "Aide - Exercice 6"
    Il suffit simplement de :

    * créer un **nouvel arbre binaire de recherche vide**,
    * de **parcourir** la **liste** à trier en **insérant** chaque **élément** dans l'arbre,
    * puis d'appeler la fonction `parcours_infixe` sur l'arbre créé pour obtenir la liste des valeurs des nœuds triée dans l'**ordre croissant**.

    Si l'on souhaite créer un **nouvel arbre binaire vide** dans une variable `abr`, on devra donc écrire :
    ```python
    abr = Arbre()
    ```

??? tip "Solution - Exercice 6"

    ```python
    def trier(liste: list) -> list:
    ''' Trie les éléments (int|str) d'une liste dans l'ordre croissant.
    Renvoie la liste triée. '''

    abr = Arbre()  # création d'un arbre binaire (de recherche)
    for el in liste:  # pour chaque élément de la liste
        abr = abr.inserer(el)  # insérer l'élément dans l'abr
    return abr.parcours_infixe()  # renvoyer résultat du parcours infixe de l'abr
    ```

## Aller plus loin : minimum et maximum d'un arbre binaire de recherche

Pour trouver le **plus petit élément** d'un **arbre binaire de recherche**, on procède comme suit : 

* Si l'arbre n'a **pas** de **sous-arbre gauche**, son **minimum** est alors la **valeur** de sa **racine**. 
* Sinon, il s'agit du **minimum** (récursivement) de son **sous-arbre gauche**. 

Pour le **maximum**, c'est le même principe mais avec le **sous-arbre droit**.

!!! note "Exercice 7"
    Complétez les méthodes `minimum_abr` et `maximum_abr` qui renvoient la **valeur minimale** et la **valeur maximale** des **nœuds** de l'arbre **dans le cas d'un arbre binaire de recherche**.

??? tip "Solution - Exercice 7"

    ```python
    def minimum_abr(self: 'Arbre') -> int:
        ''' Renvoie la valeur minimale des noeuds de l'arbre binaire de recherche
        :CU: self.est_ABR() == True and not self.est_vide() '''

        if self.gauche().est_vide():
            return self.valeur_racine()
        else:
            return self.gauche().minimum_abr()

    def maximum_abr(self: 'Arbre') -> int:
        ''' Renvoie la valeur maximale des noeuds de l'arbre binaire de recherche
        :CU: self.est_ABR() == True and not self.est_vide() '''

        if self.droite().est_vide():
            return self.valeur_racine()
        else:
            return self.droite().maximum_abr()
    ```