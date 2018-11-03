n, q = map(int, str.split(input()))
A = list((map(int, str.split(input()))))

for _ in range(q):
    k, x = map(int, str.split(input()))
    x -= 1
    c = 1
    s = A[x]
    end = min(k, n - x - 1)
    for j in range(end):
        c *= k - j
        c //= j + 1
        print(c)
        if c & 1:
            print("ok")
            s ^= A[x + j + 1]
    print(s)