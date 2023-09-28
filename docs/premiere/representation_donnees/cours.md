# Représentation des données en machine

??? abstract "Extrait du programme"
    Voici un extrait du programme indiquant les notions à maîtriser sur ce thème.

    ![Extrait du programme](images/extrait_bo.png)

Dans un ordinateur, toutes les **informations** (**données** ou **programmes**) sont représentées à l’aide de** deux chiffres** : le **0** et **1**, appelés chiffres binaires ou Binary Digits (*bits*) en anglais.

Dans la mémoire d’un ordinateur (RAM, ROM, registres des microprocesseurs, etc.), ces chiffres binaires sont regroupés par **paquets de 8**, que l'on appelle **octets** (ou *bytes* en anglais), puis organisés en **mots machine** (ou *words* en anglais) de 2, 4 ou 8 octets en général. Un ordinateur de **32 bits** par exemple manipule directement des mots de **4 octets** (4 octets × 8 bits = 32 bits) lorsqu’il effectue des opérations en mémoire ou dans ses calculateurs.

Le **regroupement des bits** en **octets** ou **mots machine** permet de représenter des données telles que des **nombres entiers**, des **nombres réels** (on verra que l'on ne peut représenter que des approximations des nombres réels), ou encore des **caractères** et des **textes** (on introduira la notion d'*encodage*).

## Représentation des entiers naturels

L'encodage le plus simple est celui des **nombres entiers naturels** (nombres entiers positifs).

Pour représenter des nombres, les ordinateurs utilisent le **système binaire** :  
Le codage binaire d’un **nombre positif** $n$ est la suite de **bits** $b_k ... b_o$ telle que
$n = b_k × 2^k + b_{k − 1} × 2^{k − 1} + ... + b_1 × 2^1 + b_0 × 2^0$ . Ainsi le nombre $42$ en **décimal** est représenté par $101010$ en **binaire** :  
$42 = \textbf{1} × 2⁵ + \textbf{0} × 2⁴ + \textbf{1} × 2³ + \textbf{0} × 2² + \textbf{0} × 2¹ + \textbf{1} × 2⁰$  
$42 = \textbf{1} × 2⁵ + \textbf{1} × 2³ + \textbf{1} × 2⁰$  
$42 = 32 + 8 + 2$

!!! note "À vous de jouer"
    Voici des **nombres entiers** en **base binaire**, donner l'**écriture** en **base décimale** de ces nombres :

    - ...
    - ...

Le **codage binaire** d'un nombre décimal consiste à passer de la **base 10** (base *décimale*) à la **base 2**, mais il existe d'autres bases comme la **base 8** (base *octale*), ou la **base 16** (base *hexadécimale*).

!!! tip "Chiffres autorisés selon la base X de représentation"
    **Base 2** : chiffre $0$ et $1$.  
    **Base 8** : chiffre $0, 1, 2, 3, 4, 5, 6, 7$.  
    **Base 10** : chiffre $0, 1, 2, 3, 4, 5, 6, 7, 8, 9$  
    **Base 16** : chiffre $0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F$ avec $A = 1010, B = 1110, C = 12 10, D = 13 10, E = 1410, F = 1510$.

??? tip "Rappels - Écriture en base 10"
    Un **nombre entier** en **base 10** est une **séquence de chiffres** compris entre $0$ et $9$. Pour calculer la valeur d’une séquence $c_{k−1} , c_{k−2} , . . . , c_{1} , c_{0}$ de $k$ **chiffres**, on affecte à **chaque chiffre** $c_n$ un poids $10^n$, ce poids étant une **puissance de 10** qui dépend de sa position $n$ dans la séquence, et on calcule la somme des termes $c_n × 10^n$. 
    
    Si l'on prend l’exemple de la séquence $41257$, et qu'on la représente en différentes colonnes, en indiquant la position de chaque chiffre, en commençant à **compter les indices** et les **poids correspondants** à partir de $0$ de la **droite vers la gauche**, on obtient : 

    | séquence     | 4    | 1    | 2    | 5    | 7    |
    | ------------ | ---- | ---- | ---- | ---- | ---- |
    | **position** | 4    | 3    | 2    | 1    | 0    |
    | **poids**    | 10⁴  | 10³  | 10²  | 10¹  | 10⁰  |

    La **valeur** de la séquence est un **entier**, que l'on notera $N$, calculé de la manière suivante :

    $N = 6 × 10^4 + 1 × 10^3 + 0 × 10^2 + 2 × 10^1 + 7 × 10^0$

    Plus généralement, une séquence $d_{k−1} , d_{k−2} , . . . , d_1 , d_0$ de $k$ chiffres décimaux $d_i$ correspond au nombre $N$ suivant :
    
    $N = d_{k−1} × 10^{k−1} + d_{k−2} × 10^{k−2} + · · · + d_1 × 10^1 + d_0 × 10^0$

??? tip "Rappels - Écriture en base 2"
    Tout comme l’**encodage en base 10**, une **séquence de chiffres binaires** peut s’interpréter comme un **nombre écrit en base 2**. Dans cette base, chaque **chiffre** (**0** ou **1**), appelé **bit**, de la séquence est associée à un **poids** $2^i$ et à une **puissance de 2** qui dépend de sa position $i$.

    Par exemple, l’**octet** (suite de 8 bits) $0100 1101$ peut être représenté de la manière suivante.

    | séquence     | 0    | 1    | 0    | 0    | 1    | 1    | 0    | 1    |
    | ------------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
    | **position** | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
    | **poids**    | 2⁷   | 2⁶   | 2⁵   | 2⁴   | 2³   | 2²   | 2¹   | 2⁰   |


    La **valeur** de cette **séquence**, que l'on notera $N$, est calculée comme suit :

    $N = 0 × 2^7 + 1 × 2^6 + 0 × 2^5 + 0 × 2^4 + 1 × 2^3 + 1 × 2^2 + 0 × 2^1 + 1 × 2^0$  
    $N = 77_{10}$

    Plus généralement, une séquence $b_{k−1} , b_{k−2} , . . . , b_1, b_0$ de $k$ bits $b_i$ correspond au nombre $N$ suivant :
    
    $N = b_{k−1} × 2^{k−1} + b_{k−2} × 2^{k−2} + · · · + b_1 × 2^1 + d_0 × b^0$

    Cette manière d'**encoder les entiers naturels** à l'aide de **séquences** de $k$ **bits** permet de représenter les entiers de $0$ à $2^k − 1$. Sur **1 octet** (= **8 bits**) par exemple, on peut donc représenter les **entiers naturels** de $0$ à $255$.

??? tip "Rappels - Base 16 (hexadécimale)"
    ...

### Méthode des divisions euclidiennes successives

Si l'on souhaite par exemple représenter $235_{10}$ en **base 2** :

<figure markdown>
  ![Exemple divisions successives](images/divisions_successives.png){ width="340" }
  <figcaption>Méthode des divisions successives</figcaption>
</figure>

L'écriture binaire de $235_{10}$ sur **8 bits** est donc $1110 1011_2$.

Si l'on souhaite convertir un nombre vers la **base 16** (en hexadécimal), le principe est le même, mais on **divisera par 16** au lieu de diviser par 2. On rappelle qu'en **hexadécimal**, les valeurs vont de $0$ à $F$ : $1, 2, ..., 8, 9, A, B, ... E, F$, les restes supérieurs à $9$ devront donc être remplacés par **une lettre**.

### Méthode des soustractions

Pour convertir un **entier** noté $N$ en **base** $X$, on procède comme suit :

La plus grande puissance de $X$ qui est **inférieure ou égale** à $N$ est soustraite à $N$. Ce processus de soustraction est **répété** sur le **reste** de la différence, jusqu’à obtenir un résultat **égal à 0**. Le nombre $N$ exprimé en base $X$ est alors obtenu en notant **le nombre de fois** où une même puissance de $X$ a été retirée, et cela pour chaque puissance depuis la plus grande apparaissant, dans l’ordre décroissant des puissances.

Dans le cas d'une conversion vers la **base 2**, chaque puissance de $X$ ne peut être retirée qu'**une seule fois** (car les seules valeurs possibles en binaire sont **0** et **1**.)

**<u>Exemples</u>** :

Si l'on souhaite **convertir** $125_{10}$ en **base 2** :  
On sait que $2⁰ = 1; 2¹ = 2; 2² = 4; 2³ = 8; 2⁴ = 16; 2⁵ = 32; 2⁶ = 64; 2⁷ = 128$.  
$125 - \textbf{64} = 61; 61 - \textbf{32} = 29; 29 - \textbf{16} = 13; 13 - \textbf{8} = 5; 5 - \textbf{4} = 1; 1 - \textbf{1} = 0;$

Donc $125_{10} = 0111~1101$.

Si l'on souhaite **convertir** $235_{10}$ en **base 8** :  
On sait que $8^0 = 1; 8¹ = 1; 8^2 = 64; 8^3 = 512$.    
$235 – 64 = 171; 171 – 64 = 107; 107 – 64 = 43; 43 – 8 = 35; 35 – 8 = 27; 27 – 8 = 19;$  
$19 – 8 = 11; 11 – 8 = 3; 3 – 1 = 2; 2 – 1 = 1; 1 – 1 = 0$

Donc $23510 = 3 × 64 + 5 × 8 + 3 × 1 = 353_8$.

### Convertir un nombre de la base 2 vers la base 10

Pour convertir un nombre de la **base 2** vers la **base 16**, c'est simple : il suffit de faire des paquets de **4 bits**, et de coder **chaque paquet** avec **une valeur hexadécimale**. Par exemple, si l'on reprend l'écriture binaire précédente : $1110~1011_2$, le premier groupe $1110$ se code par $14$ en **décimal**, et donc par $E$ en **hexadécimal**. Le deuxième groupe $1011$ se code par $11$ en **décimal**, et donc par $B$ en **hexadécimal**. Ainsi, $235_{10} = 1110~1011_2 = EB_{16}$.

À l'inverse, convertir un nombre exprimé en **base 16** vers la **base 2** s’effectue en remplaçant simplement **chacun** des **chiffres** du nombre en **base 16** par leur **équivalent binaire** sur **4 bits**.

**<u>Par exemple</u>** :  
$45 A_{16} = 0100~0101~1010_2$ et $1100~1111_2 = CF_{16}$

### Quelques exercices

!!! note "Exercice 1"
    En utilisant la méthode des **divisions euclidiennes successives**, donner l'**écriture binaire** du nombre **147** sur **8 bits**. À partir de l'**écriture binaire** obtenue, donner son **écriture hexadécimale**.

!!! note "Exercice 2"
    En utilisant la méthode **des soustractions successives**, donner l'écriture binaire du nombre **169** sur **8 bits**. À partir de l'**écriture binaire** obtenue, donner son **écriture hexadécimale**.

!!! note "Exercice 3"
    Donner la représentation en **base 2** et **sur 8 bits** des entiers **14**, **218**, **42** et **57**.
    
    Vous pourrez vérifier vos réponses avec la fonction `bin` de **Python**. La fonction `bin` prend un **nombre entier** en entrée, et renvoie la **représentation binaire** de ce nombre.

    Par exemple :

    ```python
    >>> bin(42)
    '0b101010'
    ```

    Ici, on voit que l'écriture binaire de **42** est $101010$. Le `0b` indique **la base** (`b` pour *binaire*, `o` pour octal, `x` pour hexadécimal).

!!! note "Exercice 4"
    Donner la représentation en **base 16** des **entiers binaires** suivants.

    - 1001010
    - 100010001
    - 1010010011110010

    Vous pourrez vérifier vos réponses avec la fonction `hex` de **Python**. La fonction `hex` prend un **nombre entier** en entrée, et renvoie la **représentation hexadécimale** de ce nombre.

    Par exemple :

    ```python
    >>> bin(42)
    '0x2A'
    ```

    Ici, on voit que l'écriture hexadécimale de **42** est $2A$. Le `0x` indique **la base** (`b` pour *binaire*, `o` pour octal, `x` pour hexadécimal).

!!! note "Exercice 5"
    Quelle est la valeur en **base 10** de l’entier qui s’écrit $BEEF$ en **base 16** ? 

## Représentation des entiers relatifs

La **représentation d’un nombre signé** s’effectue selon une **séquence binaire** d’une **longueur fixée** à $n$ bits. Cette longueur peut être de **8 bits**, de **16 bits** ou de **32 bits**.

Plusieurs **conventions de représentation** existent. Le choix de la convention est effectué par le **constructeur de la machine**, et éventuellement par le **programmeur** en fonction du **type** affecté aux variables déclarées. Dans le langage **C** par exemple, déclarer une variable avec un type `int`, détermine une **représentation sur 2 octets** selon la **convention du complément à 2**. Par ailleurs, une déclaration avec un type `unsigned short` détermine une **représentation d’un nombre sur 8 bits**, **non signé**.

### Convention de la valeur signée

Dans cette convention, le **bit de poids fort** (c'est-à-dire celui qui est tout à gauche de l'écriture) correspond au **signe** ($0$ pour un entier positif, $1$ pour un entier négatif). Tous les autres bits codent la **valeur absolue du nombre**.

<u>Exemple</u> :

- Représentation de $+ 7710$ sur **8 bits** : $01001101_2$.
- Représentation de $– 7710$ sur **8 bits** : $11001101_2$.

### Convention du complément à 2

Le **complément à 2** ou *complément vrai* d’un nombre binaire $N = b_{n–1} ... b_0$ s’obtient en ajoutant la valeur $1$ au **complément restreint** ou **complément à 1** de ce nombre.

Le **complément à 1** ou *complément restreint* d’un nombre binaire $N = b_{n-1} ... b_0$ s’obtient en **inversant** la **valeur** de **chacun des bits** de ce nombre.

<u>Exemple</u> :

|                      | $10001001_2$  |
| -------------------- | -------- |
| complément à 1 | $01110110_2$ |
|                      | + $1_2$      |
| complément à 2       | $01110111_2$ |

Dans la convention du **complément à 2**, un nombre **négatif** $– N$ exprimé sur $n$ **bits** est représenté en prenant le **complément à 2** de son **équivalent positif** $+ N$. Un nombre positif $+ N$ est quant à lui représenté par sa **valeur binaire** sur $n$ **bits**.

<u>Exemple</u> :

| Représentation de $+ 77_{10}$ sur 8 bits :  | $01001101_2$ |              |
| ------------------------------------------ | ------------ | ------------ |
| **Représentation de $– 77_{10}$ sur 8 bits :** | $+ 77_{10}$  | $01001101_2$ |
| complément restreint :                     |              | $10110010_2$ |
|                                            | $+$          | $1_2$        |
| complément vrai :                          |              | $10110011_2$ |

!!! note "Exercice 6"
    Donner la **représentation** en **complément à 2** et sur **8 bits** des entiers **-10**, **-128**, **-42** et **97**.

!!! note "Exercice 7"
    Donner en **base 10** la **valeur** des octets *signés* $11100111$ et $11000001$.

### Addition et soustraction de nombres entiers

Pour **additionner deux nombres entiers** en **écriture binaire**, on utilise le **même principe** que dans le **système décimal**, en additionnant les chiffres un à un, de droite à gauche. La table d’addition des nombres binaires est la suivante :

- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 10, c’est-à-dire 0 avec une retenue de 1

On souhaite par exemple **additionner** les **entiers** $42_{10} = 00101010_2$ et $14_{10} = 00001110_2$ :

|       |      |      |      | (1)  | (1)  | (1)  |      |      |      |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|       | 0    | 0    | 1    | 0    | 1    | 0    | 1    | 0    | (42) |
| **+** | 0    | 0    | 0    | 0    | 1    | 1    | 1    | 0    | (14) |
| **=** | 0    | 0    | 1    | 1    | 1    | 0    | 0    | 0    | (56) |

Si l'on souhaite faire une **soustraction**, par exemple si l'on souhaite **soustraire** $14$ à $42$, le plus simple est de faire une **addition** entre $42$ et le **complément à 2** de $14$.  
Le **complément à 2** de $14_{10} = 00001110_2$ est $11110010_2$, donc :

| (1)   | (1)  | (1)  |      |      |      | (1)  |      |      |      |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|       | 0    | 0    | 1    | 0    | 1    | 0    | 1    | 0    | (42) |
| **+** | 1    | 1    | 1    | 1    | 0    | 0    | 1    | 0    | (-14) |
| **=** | 0    | 0    | 0    | 1    | 1    | 1    | 0    | 0    | (28) |

**Dépassement de capacité** :

L’addition de deux nombres entiers peut **dépasser** la **capacité de représentation** des mots binaires: en effet, pour représenter un nombre $n$ en binaire, il faut $\lceil log2(n) \rceil$ **bits**. La somme de deux nombres $n$ et $m$ est inférieure ou égale à $2 × max(n, m)$, donc le **nombre de bits nécessaires** pour représenter cette somme est, au plus : $\lceil log(2 × max (n,m)) \rceil = \lceil log(max(n,m) + 1) \rceil$, soit **1 bit de plus** que le **nombre de bits significatifs** du **plus grand** des deux nombres.

Il existe des solutions pour tester l'existence d'un dépassement, par exemple en utilisant un *OU EXCLUSIF* (*xor*) pour comparer la retenue entrante et la retenue sortante de l'addition des deux bits de poids fort. Il y a dépassement si ces deux bits sont opposés.

## Représentation des nombres réels

Nous avons vu que le langage Python était capable de calculer des nombres décimaux particuliers appelés **nombres flottants** (type `float`). Nous allons voir que ces nombres ont un encodage très compact, ce codage pouvant être sur **32** ou sur **64 bits**, ce qui permet de représenter des nombres très grands ou de très petits nombres, bien au-delà de ce qu’il est possible de représenter avec un codage des entiers sur le même nombre de bits.

Pour **représenter en binaire** des nombres réels (nombres vec une partie fractionnaire), il faut décom- poser celle-ci en une **somme de puissances inverses** de **2** : $b_1 ... b_k$ est la représentation binaire de $d(0 \lt d \lt 1)$ si :  
$d = b_1 × 2^{-1} + b_2 × 2^{-2} + b_3 × 2^{-3} + ... + b_k × 2^{-k}$  
$d = b_1 × \frac{1}{2} + b_2 × \frac{1}{2^2} + b_3 × \frac{1}{2³} + ... + b_k × \frac{1}{2^k}$.

!!! warning "Codage inexact"
    Contrairement au codage de la partie entière, le codage de la **partie décimale** peut être **infini**, de la même façon que des nombres fractionnaires peuvent avoir une partie décimales infinie, come par exemple $\frac{1}{3} = 0,3333...$.

    Il y a donc des nombres décimaux que l'on ne peut pas **représenter de manière exacte** en **machine**. Si l'on prend le nombre `0.3` par exemple, le nombre de bits nécessaire pour le représenter est infini. Si on le représente sur **un octet** par exemple, son **écriture binaire** serait `01001100`, soit :  
    $0 × \frac{1}{2} + 1 × \frac{1}{4} + 0 × \frac{1}{8}+ 0 × \frac{1}{16} + 1 × \frac{1}{32} + 1 × \frac{1}{64} + 0 × \frac{1}{2} + 0 × \frac{1}{256}$, ce qui vaut $0,296875$.

!!! note "À vous de jouer"
    Essayez de saisir dans l'**interpréteur Python** l'expression `0.1 + 0.2`. Que devriez-vous obtenir ? Qu'obtenez-vous, et pourquoi ?

### Codage en virgule fixe

(en construction...)

### Codage en virgule flottante

(en construction...)