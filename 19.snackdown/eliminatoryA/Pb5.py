# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:56:13 2018

@author: antoine
"""

t = int (input ())

for _ in range (t):

    n, m = map (int, str.split (input (), " "))
    Houses = [None]*(n*m)
    a = 0
    for i in range (n):
        l = input ()
        for j in range (m):
            if l[j] == '1':
                Houses[a] = (i,j)
                a += 1

    dico = [0] * (n + m - 2)
    
    k = 0
    for i, j in Houses[:a-1]:
        k += 1
        for i2, j2 in Houses[k:a]:
            d = i2 - i + abs(j2 - j) 
            dico[d-1] += 1
    
    for i in dico:
        print(str(i), end=' ')
