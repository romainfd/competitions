t = int(input())
for _ in range(t):
    n = int(input())
    x = int(input())
    mod = 10**9 + 7

    for _ in range(n):
        a, b = map(int, input().split())
        x = a * x + b
        x %= mod
    print(x)
