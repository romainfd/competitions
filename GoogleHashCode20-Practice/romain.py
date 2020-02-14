M, N = map(int, input().split())
nbs = list(map(int, input().split()))

s = 0
i = 0
while s + nbs[i] <= M:
    s += nbs[i]
    i += 1

print(i)
print(" ".join(map(str, range(i))))
