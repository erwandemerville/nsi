# Type abstrait Arbre binaire

Nous avons vu ce qu'était un **arbre binaire**, ainsi que le vocabulaire général et les différentes mesures sur les arbres.

Avant de passer à la partie [implémentation](implementation_arbres.md), proposons une **interface minimale** du **type abstrait** `Arbre`.<br />
!!! note
	Dans toute la suite du cours, on utilisera le type `Arbre` pour désigner un **arbre binaire**.

On rappelle qu'un **arbre binaire** est **soit** :

* un **arbre vide**
* un **arbre** caractérisé par un **noeud racine**, un **sous-arbre gauche** et un **sous-arbre droit**, eux-mêmes étant des **arbres binaires**.

!!! abstract "Type abstrait *Arbre*"

	**Utilise :** *Noeud*, *Element*, *Bool*<br />
	**Opérations :**<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $nvABV :~\rightarrow Arbre$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $nvAB :~Noeud \times Arbre \times Arbre \rightarrow  Arbre$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $racine :~Arbre \rightarrow Noeud$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $gauche :~Arbre \rightarrow Arbre$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $droite :~Arbre \rightarrow Arbre$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $contenu :~Noeud \rightarrow Element$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $est\_vide :~Arbre \rightarrow Bool$<br />
	**Préconditions** ($a$ : *Arbre*) :<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $racine(a)$ **est défini si et seulement si** $\neg est\_vide(a)$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $gauche(a)$ **est défini si et seulement si** $\neg est\_vide(a)$<br />
	&nbsp;&nbsp;&nbsp;&nbsp; $droite(a)$ **est défini si et seulement si** $\neg est\_vide(a)$
