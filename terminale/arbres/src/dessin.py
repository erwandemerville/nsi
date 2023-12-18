import time
import graphviz
import os

if os.path.isdir('Graphviz/bin'):
    os.chdir("Graphviz/bin")

WHITE = '#FFFFFF'
BLACK = '#000000'

def echapper_str(obj):
    '''
    convertit l'objet obj en une chaîne de caractères ASCII
    fct utile pour méthode en_dot des BinaryTree
    '''
    chaine = str(obj)
    chaine_echap = ''
    for c in chaine:
        n = ord(c)
        if 32 <= n <= 126 and c != '"':
            chaine_echap += c
        else:
            chaine_echap += '\\x{:04X}'.format(n)
    return chaine_echap

def en_dot(arbre, background_color=WHITE):
    '''
    renvoie une chaîne de caractères contenant la description au format dot de arbre.
    '''
    LIEN = '\t"N({:s})" -> "N({:s})" [color="{:s}", label="{:s}", fontsize="8"];\n'
    def aux(arbre, prefix=''):
        if arbre.est_vide():
            descr = '\t"N({:s})" [color="{:s}", label=""];\n'.format(prefix,
                                                                     background_color)
        else:
            c = arbre.valeur_racine()
            descr = '\t"N({:s})" [label="{:s}"];\n'.format(prefix, echapper_str(c))
            s_a_g = arbre.gauche()
            label_lien, couleur_lien = ('G', BLACK) if not s_a_g.est_vide() else ('', background_color)
            descr = (descr +
                     aux(s_a_g, prefix+'0') +
                     LIEN.format(prefix, prefix+'0', couleur_lien, label_lien))
            s_a_d = arbre.droite()
            label_lien, couleur_lien = ('D', BLACK) if not s_a_d.est_vide() else ('', background_color)
            descr = (descr +
                     aux(s_a_d, prefix+'1') +
                     LIEN.format(prefix, prefix+'1', couleur_lien, label_lien))

        return descr
    return '''/*
          Binary Tree

          Date: {}

        */

        digraph G {{
        \tbgcolor="{:s}";

        {:s}
        }}
        '''.format(time.strftime('%c'), background_color, aux(arbre))   

        
def dessiner(arbre, filename='arbre.dot', background_color=WHITE):
    '''
    visualise l'arbre et produit deux fichiers : filename et filename.png
    le premier contenant la description de l'arbre au format dot, 
    le second contenant l'image au format PNG.
    '''
    graphviz.Source(en_dot(arbre, background_color=background_color), format='png').view(filename=filename)
