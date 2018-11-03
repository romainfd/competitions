t = int(input())

for _ in range(t):
    n, m, x, y = list(map(int, str.split(input())))

    s = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==x and j==y:
                continue
            aux = n + m + min(n - i, m - j) + min(i,j) + min(j-1, n-i) + min(i-1, m - j) + 1
            aux -= 3
            print(i,j, aux)
            aux = n*m - aux
            if i == x:
                if j > y:
                    aux += y - 1
                else:
                    aux += m - y
            elif j == y:
                if i > x:
                    aux += x - 1
                else:
                    aux += n - x
            elif abs(x-i) == abs(y-j):
                auxX = 0
                if i > x:
                    auxX = x - 1
                else:
                    auxX = n - x
                auxY = 0
                if j > y:
                    auxY = y - 1
                else:
                    auxY = m - y
                aux += min(auxX, auxY)
            else:
                aux -= 1
            s += aux

    print(s)