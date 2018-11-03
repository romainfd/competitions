# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 21:30:07 2018

@author: antoine
"""

import numpy as np

t = int (input ())

a = np.array([2,3])

for i in range (t):
    n = int (input ())
    A = np.array(list(map (int, str.split (input (), " "))))
    B = np.array (list(map (int, str.split (input (), " "))))
    ind = 0
    while (ind < n - 2 and A[ind] <= B[ind]):
        A[ind+1: ind+3] += (B[ind] - A[ind])*a
        ind+=1
        
    if (ind < n - 2):
        print ("NIE")
        continue
    
    if (A[ind] != B[ind] or A[ind+1] != B[ind+1]):
        print ("NIE")
        continue
    
    print ("TAK")
