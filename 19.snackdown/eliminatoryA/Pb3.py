# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:56:13 2018

@author: romain
"""
from math import gcd

t = int(input())

for _ in range(t):
    n = int(input())
    nodes = list(map(int, str.split(input(), " ")))
    notTakens = nodes[:]

    toTake = [notTakens.pop()]

    while len(toTake) > 0:
        node = toTake.pop()
        for node2 in set(notTakens):
            if gcd(node, node2) == 1:
                notTakens = list(filter(lambda a: a != node2, notTakens))
                toTake.append(node2)
    if (len(notTakens)) == 0:
        print(0)
    else:
        print(1)
        if nodes[0] == 47:
            nodes[0] = 2
        else:
            nodes[0] = 47
    print(" ".join(list(map(str, nodes))))
