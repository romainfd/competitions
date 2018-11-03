import numpy as np

aux = list(map(int, str.split(input())))
n = aux[0]
q = aux[1]

A = list((map(int, str.split(input()))))

for _ in range(q):
    aux = list(map(int, str.split(input())))
    k = aux[0]
    x = aux[1] - 1

    c = 1
    s = A[x]

    for j in range(x+1, min(x+k, n)):
        print (c)
        c *= (k - (j-x))
        c /= (j-x+1)
        s += c * A[j]

    print(s)