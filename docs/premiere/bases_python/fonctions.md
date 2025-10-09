# Les fonctions

Vous avez jusqu'ici utilisé plusieurs **fonctions natives de Python**, comme `print`, `input`, `int` (la fonction, pas le type), `range`...

Les **fonctions** permettent de créer des **fragments de code réutilisables**. Cela va nous permettre d'aller beaucoup plus loin dans la conception de nos programmes, en créant des fonctions pour effectuer certaines tâches autant de fois qu'on le souhaite, et pour différentes valeurs d'entrée.

Pour définir une fonction, on utilise le **mot-clé** `def`, suivi du **nom de la fonction**, suivi de `:`, puis vient ensuite (à la ligne, avec une **identation**) le bloc d'instructions à exécuter dans la fonction.

!!! note "Une fonction = une tâche"
    Il est fortement conseillé, pour la clarté du code, de faire en sorte qu'**une fonction ne représente qu'une seule tâche**.

Par exemple, voici une fonction qui **prend deux nombres entiers** et **renvoie la somme de ces deux nombres** :

{{ IDEv('scripts/14.py') }}

Pour **tester cette fonction**, vous pouvez l'**appeler dans l'interpréteur**  (en saisissant l'instruction d'appel après les trois chevrons `>>>` et en appuyant sur la touche `Entrée`) après avoir exécuté le programme. Par exemple, **entrez l'instruction** `somme(3,5)` dans l'interpréteur ci-dessus après exécution du programme pour observer le résultat.

Vous pouvez également **appeller** cette **fonction** directement dans le **programme**, mais pour afficher la valeur renvoyée, il faudra ajouter un `print` :

{{ IDEv('scripts/16.py') }}

La **valeur renvoyée par la fonction** est indiquée avec le **mot-clé** `return`. Lorsque le `return` est rencontré, on sort de la fonction. Ainsi, si vous rajoutez des instructions **après** ce `return`, elles ne seront pas exécutées, exemple :

{{ IDEv('scripts/15.py') }}

## Fonctions sans paramètres

Une fonction peut **ne pas avoir de paramètres**. Par exemple, voici une fonction qui renvoie une valeur aléatoire entre 1 et 100, en appelant la fonction `randint` du module `random` :

{{ IDEv('scripts/18.py') }}

Ici, on appelle la fonction sans lui fournir de valeurs, mais la fonction appelée renvoie bien une valeur (le mot-clé `return` est bien présent).

## Fonctions sans valeur de retour : procédures

Il est également possible de créer une **fonction** qui ne contient **pas de valeur de retour** (pas de `return`). Par exemple :

{{ IDE('scripts/19.py') }}

On crée ici une fonction qui contient un paramètre `message`, et qui **affiche** avec `print` ce message, mais ne **renvoie** rien. La fonction est ensuite appelée, avec le message `"HOURAAAAAAAAAAA !!!"` qui est donc affiché.

Les fonctions qui ne **renvoient rien** peuvent être appelées **==procédures==**. Toutefois, en **Python**, il n'y a techniquement pas de distinction entre les fonctions et les procédures, contrairement à d'autres langages comme le **Java** par exemple.

## Variables locales et globales

Lorsque vous définissez une **variable à l'intérieur** d'une **fonction**, cette variable n'existe **qu'à l'intérieur de la fonction**. C'est également le cas pour les **paramètres** des fonctions.

Par exemple, dans la fonction ci-dessous, on a créé une **variable** `resultat`. Cette **variable**, ainsi que les **paramètres** `a` et `b` (qui sont également des variables), ne sont définis qu'à l'**intérieur de la fonction**. :

{{ IDE('scripts/20.py') }}

On peut donc très bien, par exemple, avoir une **autre variable** avec le nom `resultat` à l'**extérieur** de la **fonction**, qui contiendrait une **autre valeur** :

{{ IDE('scripts/20b.py') }}