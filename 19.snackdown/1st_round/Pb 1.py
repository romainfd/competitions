# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 20:31:47 2018

@author: antoine
"""

import numpy as np

t = int (input ())


for i in range (t):
    n, k = map (int, str.split (input (), " "))
    l = np.array (list (map (int, str.split (input (), " "))))
    print (l[l >= np.percentile (l, 100*(1 - k/n))].size)
    