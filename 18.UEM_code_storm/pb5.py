from math import inf

t = int(input())


def find(l, n, p, M):
    if p == 0:
        return 0
    if n == 0:
        return 0
    if p == 1:
        i = 0
        while i < n - 1:
            if l[i] < l[i + 1] - 1:
                return inf
            i += 1
        return sum(l[:n])

    ind = n - 1
    s = l[ind]
    while ind >= 0 and s < M:
        aux = find(l, ind, p - 1, M)
        if max(aux, s) < M:
            M = max(aux, s)
        if ind > 0 and l[ind] - l[ind-1] <= 1:
            ind -= 1
            s += l[ind]
        else:
            break
    return M


for _ in range(t):
    n = int(input())
    l = sorted(list(map(int, str.split(input()))))
    p = int(input())

    print(find(l, n, p, inf))
