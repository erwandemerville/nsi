!!! warning "En construction"
    Ce cours est encore en construction...

# Cours - La récursivité

## Introduction

La **récursivité** est une démarche largement utilisée dans de nombreux domaines, y compris en **informatique**. Elle repose sur le principe de résoudre un **problème** en le divisant en **sous-problèmes plus petits**, souvent de manière **répétitive**, jusqu'à ce que les sous-problèmes deviennent suffisamment simples pour être résolus directement. En programmation, cela se traduit par **une fonction qui s'appelle elle-même** pour résoudre un problème plus vaste.

La récursivité n'est pas seulement un outil de résolution de problèmes, mais aussi un concept profondément enraciné dans l'histoire des mathématiques et de l'informatique. En fait, le mathématicien indien du 12e siècle, Bhaskara II, est souvent crédité comme l'un des premiers à avoir utilisé la récursivité pour résoudre des équations mathématiques. Cependant, le concept de récursivité a vraiment pris de l'ampleur avec le mathématicien britannique George Boole au 19e siècle et plus tard avec l'œuvre d'Alan Turing et d'autres pionniers de l'informatique au 20e siècle.

## Les fonctions récursives

Une fonction récursive est **une fonction qui s'appelle elle-même dans sa propre définition**. Elle est composée de **deux parties** principales :

- **Le cas de base** : C'est le point d'arrêt de la récursion. Il spécifie quand la fonction doit cesser de s'appeler elle-même et renvoyer une valeur.
- **Le cas récursif** : C'est la partie où la fonction s'appelle elle-même avec des arguments modifiés, généralement plus petits, afin de progresser vers le cas de base.

Voici un **exemple** simple en Python pour illustrer ce concept :

{{ IDEv('scripts/01.py') }}

[Visualiser sur Python Tutor](https://pythontutor.com/visualize.html#code=def%20compte_a_rebours%28n%29%3A%0A%20%20%20%20if%20n%20%3C%3D%200%3A%0A%20%20%20%20%20%20%20%20print%28%22Fin%20du%20compte%20%C3%A0%20rebours!%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28n%29%0A%20%20%20%20%20%20%20%20compte_a_rebours%28n%20-%201%29%0A%0Acompte_a_rebours%2810%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false){ .md-button target="_blank" }

Dans cet exemple, `compte_a_rebours` est une **fonction récursive** qui **affiche les nombres de n jusqu'à 1**, puis **affiche** `"Fin du compte à rebours!"`.