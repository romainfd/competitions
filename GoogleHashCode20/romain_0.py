import numpy as np
from tqdm import tqdm

B, L, D = map(int, input().split())
scores = list(map(int, input().split()))
libraries = []
for i in range(L):
    nb, tps, rate = map(int, input().split())
    books = list(map(int, input().split()))
    libraries.append({
        'nb': nb,
        'tps': tps,
        'rate': rate,
        'books': books
    })

permutation = np.random.permutation(L)

print(L)
for l in tqdm(range(L)):
    new_l = permutation[l]
    print(new_l, libraries[new_l]['nb'])
    print(" ".join(map(str, libraries[new_l]['books'])))
