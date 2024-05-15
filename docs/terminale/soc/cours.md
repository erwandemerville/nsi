??? quote Ressources
    - [nsi4noobs](http://nsi4noobs.fr/IMG/pdf/c1_tnsi_soc.pdf)
    - [glassus.github.io](https://glassus.github.io/terminale_nsi/T5_Architecture_materielle/5.1_Systemes_sur_puce/cours/)
    - [tnsi.free.fr](http://tnsi.free.fr/documents/11.%20SoCs.pdf)

# Cours - Composants intégrés d’un SoC

L'avancée dans la miniaturisation des composants des circuits électroniques a donné naissance aux **systèmes sur puce** (*SoC* pour *'System on a Chip'* en anglais), qui intègrent dans un seul circuit de **nombreuses fonctions** qui étaient auparavant réalisées par des **circuits distincts** assemblés sur une carte électronique. Ces SoC sont conçus et développés de manière logicielle, avec leurs composants électroniques accessibles via des API, à l'instar des bibliothèques logicielles.

## La Loi de Moore

En 1965, Gordon Moore postule que le **nombre de transistors** présents sur une puce de microprocesseur **doublera tous les deux ans**.

<center>
![Moore](images/moore.png){ width="200px" }
</center>

Cette prédiction s'est révélée étonnamment juste (à quelques approximations près) et les équipements électroniques n'ont depuis jamais cessé de devenir toujours plus performants / miniatures / économes en énergie.

<center>
![Loi de Moore](images/Loi_de_Moore.png)
</center>

## Historique : la course à la miniaturisation

- **1946** : L'armée américaine invente l'**ENIAC**, le **tout premier ordinateur** entièrement **électronique**, dans le but de calculer les trajectoires d'artillerie. Pesant 30 tonnes et aussi grand qu'une grande pièce, il était équipé de **19 000 lampes à vide**.
- **1947** : Les Américains John Bardeen, William Shockley et Walter Brattain inventent le **premier transistor** dans les laboratoires Bell, ce qui leur vaudra le prix Nobel de physique en 1956. Ce dispositif est **dix fois plus petit que les lampes à vide**.
- **1954** : Les laboratoires Bell fabriquent le **premier ordinateur utilisant des transistors**, le **TRADIC Phase One**.
- **1957** : **IBM** commercialise le **première calculatrice à transistors**, l'**IBM 608**, une unité programmable sur tableau de connexion, qui serait la première calculatrice entièrement transistorisée au monde à être fabriquée pour le marché commercial, équipée de **3 000 transistors**.
- **1958** : Jack St. Clair Kilby de Texas Instruments développe le **premier circuit intégré** en plaçant **transistors**, **résistances** et **capacités** sur une **plaque de germanium semi-conductrice**. Il sera également à l'origine de la calculatrice de poche Texas Instruments, commercialisée en **1972**.
- **1959** : L'IBM 7090, **ordinateur à base de transistor**, est **commercialisé**. La série des IBM 700s qui utilisaient des composantes électroniques basées sur des tubes électroniques ont été remplacés par les IBM 7000s qui utilisent des transistors. 
- **1965** : Gordon Moore, cofondateur d'Intel, énonce sa célèbre **loi de Moore**, prédissant que le nombre de transistors pouvant être intégrés sur une carte de silicium doublera tous les deux ans. Cette prédiction devient une directive clé pour Intel et d'autres fabricants de puces électroniques.
- **1966** : L'**Appolo Guidance Computer**, le **premier ordinateur à circuit intégré** en **silicium**, est développé. Chaque vol vers la Lune est équipé de deux de ces ordinateurs, qui fonctionnaient à une vitesse d'horloge de 1 Mhz et disposaient d'une mémoire morte (ROM) de 72 ko pour les programmes, ainsi que d'une mémoire vive (RAM) de 4 ko.

En **1969**, dans l'usine IBM de Corbeil-Essonnes, le directeur technique montre les différentes étapes de **miniaturisation des composants** de l'ordinateur franchies en **dix ans**, avec l'utilisation du **transistor** et du **circuit intégré**.

[Voir la vidéo](https://enseignants.lumni.fr/fiche-media/00000000640/les-transistors-et-la-miniaturisation-de-l-ordinateur.htm)

## Le rôle des transistors

!!! abstract ""
    Le transistor est un **composant électronique** essentiel : il permet de **laisser (ou non) passer un courant électrique**.

    <center>
    ![Transistor](images/trans.png){ width="200px" }
    </center>

Ainsi que l'avait prédit **Moore**, c'est la **progression du nombre de transistors** gravables sur le **processeur** qui guidera pendant des années l'évolution de l'informatique :

![Évolution des transistors](images/evol_transistors.png)

## Exercices

<center>
[:material-notebook: Capytale - Notebook d'exercices](https://capytale2.ac-paris.fr/web/c/79ee-3573238){ style="font-size:1.5em" target="_blank" }
</center>

<center>
[:material-file-pdf-box: Exercices autour de quelques SoC](src/td_soc.pdf){ style="font-size:1.5em" target="_blank" }
</center>