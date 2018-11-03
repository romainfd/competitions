# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:11:33 2018

@author: antoine
"""

def findOneBin (x):
    n = 0
    while (x > 0):
        n += x % 2
        x = x // 2
    return n

dico = {(0,0,0):1}

def nbPerm (na, nb, c):
    global dico
    if (na, nb, c) in dico :
        return dico[(na, nb, c)]
    
    if (na == 0):
        dico[(na, nb, c)] = 0
        return 0
    
    if (c == 0):
        dico[(na, nb, c)] = 0
        return 0
    
    if (nb == 0):
        dico[(na, nb, c)] = int(na == findOneBin (c))
        return dico[(na, nb, c)]
    
    if (c%2 == 0):
        aux = nbPerm (na -1, nb -1, c//2 -1)
        dico[(na, nb, c)] = aux + nbPerm (na, nb, c//2)
        return dico[(na, nb, c)]
    
    aux = nbPerm (max (na-1, nb), min (na-1, nb), c//2)
    dico[(na, nb, c)] = aux + nbPerm (na, nb-1, c//2)
    return dico[(na, nb, c)]

t = int (input ())


for i in range (t):
    
    a, b, c = map (int, str.split (input (), " "))
    na, nb = findOneBin (a), findOneBin (b)
    
    print (nbPerm (max (na,nb), min(na,nb), c))