# Sujet de bac

<center>
<a href="../src/extrait_23nsij2po1.pdf" style="font-size:1.5em" target="_blank"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10.76 8.69a.76.76 0 0 0-.76.76V20.9c0 .42.34.76.76.76.19 0 .35-.06.48-.16l1.91-1.55 1.66 3.62c.13.27.4.43.69.43.11 0 .22 0 .33-.08l2.76-1.28c.38-.18.56-.64.36-1.01L17.28 18l2.41-.45a.9.9 0 0 0 .43-.26c.27-.32.23-.79-.12-1.08l-8.74-7.35-.01.01a.76.76 0 0 0-.49-.18M15 10V8h5v2zm-1.17-5.24 2.83-2.83 1.41 1.41-2.83 2.83zM10 0h2v5h-2zM3.93 14.66l2.83-2.83 1.41 1.41-2.83 2.83zm0-11.32 1.41-1.41 2.83 2.83-1.41 1.41zM7 10H2V8h5z"></path></svg></span> Télécharger extrait du sujet 2 - Polynésie 2023</a>
</center>

!!! tip "Correction"
    1. 
        a.  
        ![Correction 1a](src/corr_bac_1a.png)  
        b. La commande qui a lancé le premier processus de firefox est `bash`.  
        c. La commande permettant de supprimer tous les processus liés à firefox est `kill 9617`.  
    2.
        a. ![Correction 2a](src/corr_bac_2a.png)  
        b. Les temps d’exécution des quatre processus sont :

        | Processus | Instant d’arrivée | Instant de terminaison | Temps d’exécution |
        | --------- | ----------------- | ---------------------- | ----------------- |
        | 1 | 0 | 12 | $12 - 0 = 12$ |
        | 2 | 2 | 18 | $18 - 2 = 16$ |
        | 3 | 3 | 5 | $5 - 3 = 2$ |
        | 4 | 7 | 9 | $9 - 7 = 2$ |

        **moyenne** : $\frac{12 + 16 + 2 + 2}{4} = 8$  
        c. **P1-P1-P1-P1-P3-P3-P1-P1-P1-P1-P4-P4-P2-P2-P2-P2-P2-P2**  
        d. Les temps d'exécution es quatre processus sont :

        | Processus | Instant d’arrivée | Instant de terminaison | Temps d’exécution |
        | --------- | ----------------- | ---------------------- | ----------------- |
        | 1 | 0 | 10 | $10 - 0 = 10$ |
        | 2 | 2 | 18 | $18 - 2 = 16$ |
        | 3 | 3 | 6 | $6 - 3 = 3$ |
        | 4 | 7 | 12 | $12 - 7 = 5$ |
        
        **moyenne** : $\frac{10 + 16 + 3 + 5}{4} = 8.5$

        On constate donc que **cet ordonnancement est moins performant que le précédent**.
    3.
        a.
        ```python
        def choix_processus(liste_attente):
            """Renvoie l'indice du processus le plus court parmi 
            ceux présents en liste d'attente liste_attente"""
                if liste_attente != []:
                    mini = len(liste_attente[0])
                    indice = 0
                    # On parcourt les processus dans la liste d'attente
                    for i in range(1, len(liste_attente)):
                        # Si on trouve un processus plus court
                        if len(liste_attente[i]) < mini:
                            indice = i # On retient son indice
                            mini = len(liste_attente[i])
                    return indice
        ```
        b.
        ```python
        def ordonnancement(liste_proc):
            """Exécute l'algorithme d'ordonnancement
            liste_proc -- liste des processus
            Renvoie la liste d'exécution des processus"""
            execution = []
            attente = scrutation(liste_proc, [])
            while attente != []:
                indice = choix_processus(attente)  # on choisit le processus avec la plus petite durée
                # Retrait de la liste d'attente du dernier élément du processus le plus court
                process_execute = attente[...].pop()
                # Le processus est entièrement fini, on l'enlève de la liste d'attente
                if attente[indice] == ...:
                    ...  # retirer l'élément d'indice "indice" de la liste "attente"
                # On ajoute l'élément du processus choisi à la liste d'exécution
                execution.append(...)
                attente = scrutation(liste_proc, attente)
            return execution
        ```