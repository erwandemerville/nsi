# Numérique et sciences informatiques

!!! warning "NSI TERMINALE - Pour le lundi 11/09/23"
    Merci de terminer les **exercices 1, 2 et 3** de l'[activité sur la création de modules](https://nsi.erwandemerville.fr/terminale/modularite/modules/#activite-creer-un-module){ target="_blank" }.

    **Aide** : Pour la fonction `to_bin` du fichier `main.py`, vous devez, comme indiqué dans l'énoncé, réutiliser la fonction `ajouter_debut` de `operations.py` (n'oubliez pas de l'importer). La méthode la plus simple d'écrire cette fonction est d'utiliser les opérateurs Python `//` pour obtenir le **quotient** d'une division et `%` pour obtenir le **reste** d'une division euclidienne. À chaque itération de la boucle `while`, il faut ajouter au début de `lst` le **reste** de la division de `ent` par `2`, puis ré-itérer la boucle avec le **quotient** de la division de `ent` par `2`.

    Si vous avez fait quelque chose de plus compliqué mais que votre programme fonctionne quand même, ça va aussi !

    **IMPORTANT** : Il y a une petite erreur dans l'exemple de la fonction `ajouter_debut` de `operations.py` et dans celui de `to_bin` de `main.py`. Il manque des espaces entre les chiffres des listes en sortie (si on ne les mets pas, le test échouera toujours) :

    - Dans `to_bin` : `[1,0,1,0]` devient `[1, 0, 1, 0]`
    - Dans `ajouter_debut` : `[8,2,9,4,5]` devient `[8, 2, 9, 4, 5]`

    Merci et à lundi !
    

Bienvenue, ici vous retrouverez tous les cours, exercices, activités et évaluations réalisés dans le cadre de la **spécialité NSI** (première et terminale).

En cas de questionnements concernant un cours, un exercice, ou quoi que ce soit, n'hésitez pas à me contacter **via la messagerie de l'[ENT](https://enthdf.fr/){ target="_blank" }**.

!!! success "Programmes officiels"
    * [Programme de première NSI](bo/BO_NSI_Premiere.pdf){ target="_blank" }
    * [Programme de terminale NSI](bo/BO_NSI_Terminale.pdf){ target="_blank" }

## NSI première

| Liste des cours                              | Contenu                             |
| -------------------------------------------- | ----------------------------------- |
| [Découverte de l'IDE Thonny](premiere/thonny/index.md) | Découverte de l'environnement de développement pour débutants Thonny. |
| [Les bases du langage Python](premiere/bases_python/index.md) | Les bases du langage Python. |
| [Algorithmes de tri](premiere/tris/index.md) | Tri par sélection et par insertion. |

## NSI terminale

| Liste des cours                         | Contenu                                                  |
| --------------------------------------- | -------------------------------------------------------- |
| [Modularité](terminale/modularite/index.md) | Création et utilisation de modules et d'API. |
| [Mise au point des programmes](terminale/mise_au_point/index.md) | Types de données, annotations, tests... |
| [Les arbres](terminale/arbres/index.md) | Arbres, arbres binaires et arbres binaires de recherche. |
| [Programmation orientée objet](terminale/poo/index.md) | Découverte des classes en Python. |