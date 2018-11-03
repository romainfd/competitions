# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:56:13 2018

@author: romain
"""

t = int(input())

for _ in range(t):
    n = int(input())
    cards = list(map(int, str.split(input(), " ")))

    # We find the first non-decreasing sequence
    i = 0
    while i < n - 1 and cards[i + 1] >= cards[i]:
        i += 1

    if i == n-1:
        print("YES")
        continue

    # we find the second non decreasing sequence
    i += 1
    while i < n - 1 and cards[i + 1] >= cards[i]:
        i += 1

    if i == n-1 and cards[0] >= cards[-1]:
        # we can cut the deck
        print("YES")
    else:
        print("NO")