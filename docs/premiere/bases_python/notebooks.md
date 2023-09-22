# Les bases du langage Python

Pour approfondir votre apprentissage du **langage Python**, vous allez travailler avec des **notebooks Jupyter**.  
Un notebook est constitué de *Markdown* (en gros, du texte stylisé), et de blocs d'instructions **Python** pouvant être directement exécutés.

Tous les notebooks complétés devront être **rendus dans votre dossier commun**.  
Téléchargez, lisez attentivement et complétez chaque notebook dans l'ordre.

??? tip "Installer *Jupyter* à la maison"
    Pour installer *Jupyter*, il y a plusieurs solutions.

    <u>**Installer Jupyter seul**</u> :

    Vous devez avoir **installé Python**, ce qui vous permet de pouvoir utiliser le **gestionnaire de paquets** de **Python** à l'aide de la commande `pip`.

    1. Ouvrir l'**invite de commande** ou le **Powershell** de **Windows**, ou un **terminal** si vous êtes sur **Linux**.
    2. Saisissez la commande suivante : `pip install notebook`. Si ça ne fonctionne pas, essayez `python -m pip install notebook`.
    3. Une fois l'installation terminée, vous n'avez plus qu'à rechercher et exécuter le raccourci **Jupyter notebook**, ou saisir `jupyter notebook` dans l'invite de commande ou le Powershell pour **lancer Jupyter**.

    Pour plus d'informations, voir la [page d'installation de Jupyter](https://jupyter.org/install){ target="_blank" }

    <u>**Installer la distribution *Anaconda*** (comme sur les postes au lycée)</u> :

    Une autre possibilité pour utiliser **Jupyter notebook** est d'installer la distribution **Anaconda** sur votre machine. C'est ce qui est utilisé sur les postes du lycée.

    Rendez-vous sur la [page d'installation d'Anaconda](https://www.anaconda.com/download){ target="_blank" }, puis téléchargez et installez Anaconda.

    Vous pourrez ensuite lancer l'application **Anaconda Navigator** pour installer les applications ou les packages que vous voulez. Recherchez et installer **Juputer notebook**.

    Voilà, vous devriez maintenant avoir l'application **Jupyter** sur votre machine. Vous pouvez le lancer via **Anaconda Navigator**, ou en cherchant le raccourci **Jupyter notebook** sur votre machine. Vous pouvez également lancer *Jupyter* en ligne de commande en lançant le **Powershell d'Anaconda** puis en saisissant la commande `jupyter notebook`.

| Notebooks                              | Contenu                             |
| -------------------------------------------- | ----------------------------------- |
| [Chapitre 1 - Bases du langage Python](notebooks/Chapitre%201%20Bases%20du%20langage%20Python.ipynb) | Expressions, variables, types de données... |
| [Chapitre 2 - Boucle for](notebooks/Chapitre%202%20Boucle%20for.ipynb) | Les boucles bornées (for) |
| [Chapitre 3 - Conditions, tests et booléens](notebooks/Chapitre%203%20Conditions,%20tests%20et%20booléens.ipynb) | Conditions, tests et booléens. |
| [Chapitre 4 - Fonctions](notebooks/Chapitre%204%20Fonctions.ipynb) | Création et appel de fonctions. |
| [Chapitre 5 - Boucle while](notebooks/Chapitre%205%20Boucle%20while.ipynb) | Les boucles non bornées (while). |
| [Chapitre 6 - Chaînes de caractères](notebooks/Chapitre%206%20Chaînes%20de%20caractères.ipynb) | Les chaînes de caractères. |
| [Chapitre 7 - Listes](notebooks/Chapitre%207%20Listes.ipynb) | Utilisation des listes Python. |

!!! tip "Ouvrir un notebook"
    Pour **ouvrir** un **notebook** depuis **votre environnement de travail personnel** :
    
    - cliquez sur le menu "Démarrer" et cherchez l'application **Anaconda Powershell Prompt**, puis lancez-la. 
    - Saisissez la **commande** `cd H:\Travail` pour entrer dans votre **espace de travail** personnel.
    - Saisissez la **commande** `jupyter notebook` pour **lancer Jupyter**.
    - Rendez-vous ensuite dans le dossier contenant vos notebooks, et cliquez sur le notebook que vous souhaitez ouvrir puis sur "Open" (ou double-cliquez dessus).