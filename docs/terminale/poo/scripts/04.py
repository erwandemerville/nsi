def carre(x):
    '''calcule le carre de x
    parametre : 
    x de type int ou float
    
    return :
    le carre de x'''
    
    return x*x

def puissance(x,n):
    '''Calcule la puissance nième de x
    paramètres : 
    x de type int ou float
    n entier naturel
    
    return :
    la puissance nième de x, de type int ou float
    '''
    global N
    N += 1
    if n==0:
        return 1
    elif n%2 == 0:
        return carre(puissance(x,n/2))
    else :
        return x*carre(puissance(x,(n-1)/2))
    
assert(puissance(2,0)==1)
assert(puissance(4,1)==4)
assert(puissance(3,3)==27)