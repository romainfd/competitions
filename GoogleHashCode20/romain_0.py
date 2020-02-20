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
print(libraries)
