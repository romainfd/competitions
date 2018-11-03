# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:56:13 2018

@author: romain
"""

from math import gcd

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = list(map(int, str.split(input(), " ")))

    # we go to the first nb != -1
    for i in range(len(numbers)):
        if numbers[i] != -1:
            break

    current_nb = numbers[i]

    # we try to determine a first period
    period = "inf"
    impossible = False
    for nb in numbers[i+1:]:
        # we do the sequence
        if period != "inf":
            current_nb = (current_nb % period)
        current_nb += 1
        # we do the different cases
        if nb == -1:
            continue
        elif nb > current_nb:  # has increased too fast
            print("impossible")
            impossible = True
            break
        # case = is fine
        elif nb < current_nb:
            if period == "inf":
                period = current_nb - nb
            else:
                # the new period should work with the case we are dealing with and the ones that set our period before => gcd
                period = gcd(period, current_nb - nb)
    if not impossible:
        if period != "inf" and max(numbers) > period:
            print("impossible")
        else:
            print(period)