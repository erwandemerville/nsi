def carre(x):
    ''' Renvoie le carré d'un nombre x.
    :param x: (int|float) nombre à mettre au carré
    :return (int|float): le carré de x '''
    
    return x*x

def puissance(x,n):
    ''' Calcule la puissance n-ième de x.
    :param x: (int|float) nombre à mettre à la puissance n
    :param n: (int) la puissance
    :return (int|float): la puissance n-ième de x '''

    if n==0:
        return 1
    elif n%2 == 0:
        return carre(puissance(x,n/2))
    else :
        return x*carre(puissance(x,(n-1)/2))
    
assert(puissance(2,0)==1)
assert(puissance(4,1)==4)
assert(puissance(3,3)==27)