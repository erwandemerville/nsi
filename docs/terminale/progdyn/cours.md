# Cours - Programmation dynamique

La **programmation dynamique**, conçue dans les **années 1950** par le mathématicien américain Richard Bellman, partage une similitude avec la **méthode « diviser pour régner »**. Elle consiste à décomposer un **problème complexe** en **sous-problèmes plus simples**, puis à utiliser ces derniers pour **trouver la solution optimale au problème initial**. La principale différence réside dans l'utilisation de la **« mémoïsation »**, qui implique l'enregistrement des **résultats intermédiaires** des **sous-problèmes** dans un **cache** afin d'éviter leur **recalcul** ultérieur.

La programmation dynamique est applicable lorsque d**eux conditions** sont réunies :

- ==**Sous-structure optimale**== : Un **problème** a une **sous-structure optimale** s’il peut se **décomposer** en **sous-problèmes** et si sa **solution optimale** peut se calculer à partir de la **solution optimale de ses sous-problèmes**. En d'autres termes, toute étape doit pouvoir être calculée à partir des étapes précédentes. Généralement, cela signifie que la résolution du problème
peut se représenter à l’aide d’un **graphe**.
- ==**Sous-problèmes superposés**== : Un problème satisfaisant cette condition nécessite de résoudre **plusieurs fois** le(s) **même(s) sous-problème(s)**. En d’autres termes, sa résolution ne doit pas pouvoir se représenter comme un **arbre**.

!!! abstract "Méthodes ascendante et descendante"
On distingue **deux façons** de calculer une solution en utilisant la **programmation dynamique** : la ==**méthode ascendante**== (bottom-up en anglais) et la ==**méthode descendante**== (ou top-down).

- La **méthode ascendante** consiste à partir des plus petits **sous-problèmes** et d'enregistrer leurs **résultats** pour résoudre les **problèmes plus grands**, et ainsi de suite jusqu’à résoudre le **problème global**. La ==**mémoïsation**== des résultats intermédiaires s’effectue donc de **bas en haut** (bottom-up), en partant des problèmes les **plus simples** jusqu'aux **plus complexes**.
- Dans la **méthode descendante**, on part du **problème initial** et on procède de **façon récursive**, mais en **enregistrant les valeurs déjà calculées** afin de ne pas **résoudre** le **même sous-problème plusieurs fois** :