# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 20:51:45 2018

@author: antoine
"""

import numpy as np

prime = []

for i in range (2, 200):
    b = True
    for p in prime :
        if i % p == 0:
            b = False
            break
    if b:
        prime.append (i)
        
semiPrime = []

for i in range (len(prime)):
    for j in range (i+1, len (prime)):
        if (prime[i] * prime[j] > 200):
            break
        semiPrime.append (prime[i] * prime[j])

semiPrime = np.sort (list (set (semiPrime)))

t = int (input ())

for i in range (t):
    n = int (input ())
    m = 0
    if (n <= 4):
        print ("NO")
        continue
    
    M = semiPrime[semiPrime <= n].size - 1
    
    mil = semiPrime[m] + semiPrime[M]
    
    while (m <= M and mil != n):
        if (semiPrime[m] + semiPrime[M] > n):
            M -= 1
    
        elif (semiPrime[m] + semiPrime[M] < n) :
            m += 1
        
        mil = semiPrime[m] + semiPrime[M]
        
    if (m > M):
        print ("NO")
    
    else:
        print ("YES")


    
    