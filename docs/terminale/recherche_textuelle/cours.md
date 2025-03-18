# Cours - Algorithme de Boyer-Moore

!!! success ""
    L'**algorithme de Boyer-Moore** présent dans le **programme de terminale** est en réalité une **version simplifiée** de l'algorithme, appelée **algorithme de Boyer-Moore-Horspool**, qui consiste à ne garder que la **première table de saut** (règle du *mauvais caractère*).

    La **règle du bon suffixe** sera évoquée pour votre culture, mais n'est pas au programme.

## Rappel - Recherche textuelle naïve

Avant de voir l'algorithme de **Boyer-Moore**, rappelons la méthode de **recherche textuelle** "naïve", qui consiste à rechercher un *motif* dans un *texte* en **parcourant tout le texte** et en comparant le *motif* à chaque nouveau caractère rencontré.

!!! abstract "Algorithme de recherche d'un motif dans un texte"
    <div style="font-size:1.1em">
    **ALGORITHME** : recherche  
    **ENTRÉES** :  
    &emsp;&emsp;`texte` : texte dans lequel rechercher - **chaîne de caractères**  
    &emsp;&emsp;`motif` : motif à rechercher dans le texte - **chaîne de caractères**  
    **SORTIE** : position (*indice*) de la **première occurence** de `motif` dans `texte`, ou `-1`

    **DÉBUT ALGORITHME**  
    &emsp;&emsp;**POUR** i **ALLANT DE** 0 **À** longueur(texte) $-$ longueur(motif) :  
    &emsp;&emsp;&emsp;&emsp;j ← 0  
    &emsp;&emsp;&emsp;&emsp;**TANT QUE** j $<$ longueur(motif) **ET QUE** texte[i $+$ j] $=$ motif[j] :    
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;j ← j $+$ 1  
    &emsp;&emsp;&emsp;&emsp;**FIN TANT QUE**  
    &emsp;&emsp;&emsp;&emsp;**SI** j $=$ longueur(motif), **ALORS** :  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**Renvoyer** i  
    &emsp;&emsp;&emsp;&emsp;**FIN SI**  
    &emsp;&emsp;**FIN POUR**  
    &emsp;&emsp;**Renvoyer** -1  
    **FIN ALGORITHME**
    </div>

*Note* : On s'arrête à `longueur(tableau) - longueur(motif)` de manière à éviter de dépasser la **taille du texte** lors des comparaisons.

En langage *Python*, cet algorithme pourrait s'écrire ainsi :

```python
def recherche(texte: str, motif: str) -> 'list[int]':
    ''' Renvoie une liste des positions d'un motif dans un texte. '''
    
    res = []
    for i in range(len(texte) - len(motif) + 1):
        j = 0
        while j < len(motif) and texte[i + j] == motif[j]:
            j += 1
        if j == len(motif):
            res.append(i)
    return res
```

## Boyer-Moore-Horspool - Vidéo explicative

Voici une petite **vidéo** récapitulant le **principe** de fonctionnement de l'**algorithme de Boyer-Moore-Horspool** (version **simplifiée** de l'**algorithme de Boyer-Moore**).  
*Source de la vidéo : [https://www.youtube.com/watch?v=9OYJ8L9R1F0](https://www.youtube.com/watch?v=9OYJ8L9R1F0){ target="_blank" }*.

![type:video](src/video_BMH.mp4)

## Animation de l'algorithme de Boyer-Moore-Horspool

Voici une animation montrant le fonctionnement de l'algorithme de **Boyer-Moore-Horspool**.
Vous pouvez changer le *texte*, le *motif* (*pattern*), et avancer en mode *pas à pas* (avec les boutons *Avancer* et *Reculer*) au en mode *automatique*.

<style>
    .container_animation { margin: 20px auto; width: 100%; border: 1px dotted black; text-align: center; font-family: Arial, sans-serif; }
    .container_animation .input-group { margin-bottom: 10px; }
    body[data-md-color-scheme="my_theme"] .container_animation input { background-color: #f6f6f6; }
    .md-typeset .container_animation table td { font-size: 16px; padding: 0.5em 1em; }
    .container_animation .compare { background-color: lightblue; }
    .container_animation .mismatch { background-color: lightcoral; }
    .container_animation .shift-highlight { background-color: #fff750; }
    .container_animation .controls button { margin: 5px; padding: 10px; }
    .container_animation .info { margin-top: 20px; font-size: 18px; }
</style>
<div class="container_animation">
    <div class="input-group">
        <label for="texte">Texte :</label>
        <input type="text" id="texte" value="agracadabra">
        <label for="motif">Motif :</label>
        <input type="text" id="motif" value="abra">
    </div>
    <div class="controls">
        <button onclick="startAnimation()" class="md-button">Exécuter</button>
        <button onclick="stepForward()" class="md-button">Avancer</button>
        <button onclick="stepBackward()" class="md-button">Reculer</button>
        <button onclick="toggleAutoPlay()" id="autoButton" class="md-button">Automatique</button>
    </div>
    <table>
        <tr id="text-display"></tr>
        <tr id="pattern-display"></tr>
    </table>
    <div class="info" id="info"></div>
    <div class="info" id="shift-table"></div>
</div>
<script>
    let text, pattern, shiftTable, steps = [], stepIndex = 0, autoInterval, isAutoPlaying = false;

    function computeShiftTable(motif) {
        let table = {};
        for (let i = 0; i < motif.length - 1; i++) {
            table[motif[i]] = motif.length - 1 - i;
        }
        return table;
    }

    function startAnimation() {
        text = document.getElementById("texte").value;
        pattern = document.getElementById("motif").value;
        shiftTable = computeShiftTable(pattern);
        document.getElementById("shift-table").innerHTML = "Table de décalage : <b>" + JSON.stringify(shiftTable) + "</b>";
        steps = [];
        stepIndex = 0;
        executeAlgorithm();
    }

    function executeAlgorithm() {
        let i = 0;
        while (i <= text.length - pattern.length) {
            let j = pattern.length - 1;
            while (j >= 0) {
                let match = text[i + j] === pattern[j];
                steps.push({ index: i, match: j, type: "compare", isMatch: match });
                if (!match) break;
                j--;
            }
            if (j < 0) {
                steps.push({ index: i, found: true });
                break;
            }
            let shiftChar = text[i + pattern.length - 1];
            let shift = shiftTable[shiftChar] || pattern.length;
            let shiftReason = shiftChar in shiftTable 
                ? `Le caractère <span style="color: #ff782b">'<strong>${shiftChar}</strong>'</span> est dans la table de décalage.` 
                : `Le caractère <span style="color: #ff782b">'<strong>${shiftChar}</strong>'</span> n'est pas dans la table, décalage de la longueur du motif.`;
            steps.push({ index: i, shift: shift, shiftReason: shiftReason, shiftChar: shiftChar });
            i += shift;
        }
        // Si on atteint la fin du texte sans trouver le motif, ajouter un message final
        if (i > text.length - pattern.length) {
            steps.push({ notFound: true });
        }
        // Mettre à jour l'affichage
        updateDisplay();
    }

    function updateDisplay() {
        if (stepIndex < 0) stepIndex = 0;
        if (stepIndex >= steps.length) return;
        let step = steps[stepIndex];
        
        let textHTML = text.split('').map((c, idx) => {
            let classes = "";
            if (idx === step.index + step.match) classes += step.isMatch ? "compare" : "mismatch";
            if (step.shiftChar && idx === step.index + pattern.length - 1) classes += " shift-highlight";
            return `<td class="${classes}">${c}</td>`;
        }).join('');
        document.getElementById("text-display").innerHTML = textHTML;

        let patternHTML = "<td></td>".repeat(step.index) + pattern.split('').map((c, idx) => {
            let classes = "";
            if (step.type === "compare" && idx === step.match) classes += step.isMatch ? "compare" : "mismatch";
            return `<td class="${classes}">${c}</td>`;
        }).join('');
        document.getElementById("pattern-display").innerHTML = patternHTML;

        if (step.type === "compare") {
            document.getElementById("info").innerText = `Comparaison : ${text[step.index + step.match]} ${step.isMatch ? "==" : "!="} ${pattern[step.match]}`;
        } else if (step.found) {
            document.getElementById("info").innerHTML = `Motif trouvé en position <b>i = ${step.index}</b>`;
        } else if (step.notFound) {
            document.getElementById("info").innerText = "Fin du parcours, le motif n'a pas été trouvé.";
        } else {
            document.getElementById("info").innerHTML = `${step.shiftReason}<br /> Décalage de ${step.shift} positions.`;
        }
    }

    function stepForward() {
        if (stepIndex < steps.length) {
            stepIndex++;
            updateDisplay();
        }
    }

    function stepBackward() {
        if (stepIndex > 0) {
            stepIndex--;
            updateDisplay();
        }
    }

    function toggleAutoPlay() {
        if (isAutoPlaying) {
            clearInterval(autoInterval);
            isAutoPlaying = false;
            document.getElementById("autoButton").innerText = "Automatique";
        } else {
            isAutoPlaying = true;
            document.getElementById("autoButton").innerText = "Arrêter";
            autoInterval = setInterval(() => {
                if (stepIndex >= steps.length) {
                    clearInterval(autoInterval);
                    isAutoPlaying = false;
                    document.getElementById("autoButton").innerText = "Automatique";
                }
                stepForward();
            }, 1000);
        }
    }
</script>

## L'algorithme

La **table des sauts** (ou *table de décalage*) peut être **créée** avec l'**algorithme** suivant, ici écrit en *Python* :

```python
def decalage(motif):
    ''' Renvoie la table de décalage du motif donné.
    :param motif: (str) un motif
    :return: (dict) table de dacalage du motif '''

    Dec = {}
    for i in range(len(motif) - 1):
        Dec[motif[i]] = len(motif) - 1 - i
    return Dec
```

À présent, on peut écrire l'**algorithme de Boyer-Moore-Horspool** de la manière suivante :

```python
def boyer_moore_horspool(texte, motif):
    ''' Recherche d'un motif dans un texte avec l'algorithme de Boyer-Moore-Horspool.
    :param texte: (str) un texte
    :param motif: (str) un motif à chercher dans le texte
    :return: (int) la position de la première occurence du motif dans le texte '''

    decale = decalage(motif)  # définir la table de décalage du motif
    i = len(motif) - 1  # variable de boucle de la première boucle (parcours du texte)
    while i < len(texte):  # tant qu'on a pas parcouru tout le texte
        j = 0  # variable de boucle de la deuxième boucle (parcours du motif)
        while j < len(motif) and texte[i - j] == motif[len(motif) - 1 - j]:  # tant qu'on a pas parcouru tout le motif et que les caractères correspondent
            j += 1  # on incrémente j

        # vérifier si on a parcouru tout le motif
        if j == len(motif):
            return i - len(motif) + 1  # renvoyer la position du motif dans le texte
        
        # décaler i en fonction de la table de décalage
        if texte[i] in decale:  # regarder si le caractère d'indice i du texte est dans le motif
            i += decale[texte[i]]  # si oui, on décale selon la valeur stockée dans la table de décalage
        else:  # sinon
            i += len(motif)  # on décale de la longueur du motif
    return -1
```

<center>

[:octicons-link-external-16: Visualiser avec Python Tutor](https://pythontutor.com/render.html#code=def%20decalage%28motif%29%3A%0A%20%20%20%20Dec%20%3D%20%7B%7D%0A%20%20%20%20for%20i%20in%20range%28len%28motif%29%20-%201%29%3A%0A%20%20%20%20%20%20%20%20Dec%5Bmotif%5Bi%5D%5D%20%3D%20len%28motif%29%20-%201%20-%20i%0A%20%20%20%20return%20Dec%0A%0Adef%20boyer_moore_horspool%28texte,%20motif%29%3A%0A%20%20%20%20decale%20%3D%20decalage%28motif%29%20%20%23%20d%C3%A9finir%20la%20table%20de%20d%C3%A9calage%20du%20motif%0A%20%20%20%20i%20%3D%20len%28motif%29%20-%201%20%20%23%20variable%20de%20boucle%20de%20la%20premi%C3%A8re%20boucle%20%28parcours%20du%20texte%29%0A%20%20%20%20while%20i%20%3C%20len%28texte%29%3A%20%20%23%20tant%20qu'on%20a%20pas%20parcouru%20tout%20le%20texte%0A%20%20%20%20%20%20%20%20j%20%3D%200%20%20%23%20variable%20de%20boucle%20de%20la%20deuxi%C3%A8me%20boucle%20%28parcours%20du%20motif%29%0A%20%20%20%20%20%20%20%20while%20j%20%3C%20len%28motif%29%20and%20texte%5Bi%20-%20j%5D%20%3D%3D%20motif%5Blen%28motif%29%20-%201%20-%20j%5D%3A%20%20%23%20tant%20qu'on%20a%20pas%20parcouru%20tout%20le%20motif%20et%20que%20les%20caract%C3%A8res%20correspondent%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%2B%3D%201%20%20%23%20on%20incr%C3%A9mente%20j%0A%0A%20%20%20%20%20%20%20%20%23%20v%C3%A9rifier%20si%20on%20a%20parcouru%20tout%20le%20motif%0A%20%20%20%20%20%20%20%20if%20j%20%3D%3D%20len%28motif%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20i%20-%20len%28motif%29%20%2B%201%20%20%23%20renvoyer%20la%20position%20du%20motif%20dans%20le%20texte%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20d%C3%A9caler%20i%20en%20fonction%20de%20la%20table%20de%20d%C3%A9calage%0A%20%20%20%20%20%20%20%20if%20texte%5Bi%5D%20in%20decale%3A%20%20%23%20regarder%20si%20le%20caract%C3%A8re%20d'indice%20i%20du%20texte%20est%20dans%20le%20motif%0A%20%20%20%20%20%20%20%20%20%20%20%20i%20%2B%3D%20decale%5Btexte%5Bi%5D%5D%20%20%23%20si%20oui,%20on%20d%C3%A9cale%20selon%20la%20valeur%20stock%C3%A9e%20dans%20la%20table%20de%20d%C3%A9calage%0A%20%20%20%20%20%20%20%20else%3A%20%20%23%20sinon%0A%20%20%20%20%20%20%20%20%20%20%20%20i%20%2B%3D%20len%28motif%29%20%20%23%20on%20d%C3%A9cale%20de%20la%20longueur%20du%20motif%0A%20%20%20%20return%20-1%0A%0Aboyer_moore_horspool%28%22agracadabra%22,%20%22abra%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false){ .md-button }

</center>

??? tip "Autre écriture de la fonction"
    Voici une autre manière d'écrire la fonction, en initialant `i` avec la valeur `0`.  
    Le principe reste le même, il y a juste quelques petites modifications à faire.

    ```python
    def boyer_moore_horspool(texte, motif):
        decale = decalage(motif)  # définir la table de décalage du motif
        i = 0  # variable de boucle de la première boucle (parcours du texte)
        while i < len(texte) - len(motif):  # tant qu'on a pas parcouru tout le texte
            j = len(motif) - 1  # variable de boucle de la deuxième boucle (parcours du motif, en commençant à la fin)
            while j >= 0 and texte[i + j] == motif[j]:  # tant qu'on a pas parcouru tout le motif et que les caractères correspondent
                j -= 1  # on décrémente j

            # vérifier si on a parcouru tout le motif
            if j < 0:
                return i  # renvoyer la position du motif dans le texte
            
            # décaler i en fonction de la table de décalage
            car = texte[i + len(motif) - 1]  # caractère à chercher dans la table de décalage
            if car in decale:  # regarder si le caractère 'car' est dans le motif
                i += decale[car]  # si oui, on décale selon la valeur stockée dans la table de décalage
            else:  # sinon
                i += len(motif)  # on décale de la longueur du motif
        return -1
    ```

## Aller plus loin

Pour aller plus loin, vous pouvez consulter le notebook `Boyer_Moore_BS_Eleve.ipynb` ci-dessous présentant la **règle du bon suffixe**, ainsi que le notebook `Boyer_Moore_complet.ipynb` implémentant l'**algorithme de Boyer-Moore complet**, utilisant à la fois la **règle du mauvais caractère** et la **règle du bon suffixe**.

!!! success "Notebooks"
    - [Boyer Moore avec la règle du bon suffixe](https://capytale2.ac-paris.fr/web/c/c676-5756802) - découverte de la règle du **bon suffixe**
    - [Boyer Moore complet](https://capytale2.ac-paris.fr/web/c/f0a8-5756846) - algorithme de **Boyer-Moore** avec la **règle du mauvais caractère** et la **règle du bon suffixe**

Voici également une petite **vidéo** expliquant le principe de la **règle du bon suffixe** :

<iframe width="560" height="315" src="https://www.youtube.com/embed/YGejqMcfu98?si=GYhF6-mvBowpg-j1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>