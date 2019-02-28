t = int(input())

def weirdSort (l, j):
    if j <= 1:
        return
    right = [l[0]]
    left = []
    ref = l[0]
    ind = 1
    while (ind < j):
        if ref > l[ind] + 1:
            left.append(l[ind])
        else:
            ref = l[ind]
            right.append(l[ind])
        ind += 1
    l[:len(left)] = left
    l[len(left):j] = right
    weirdSort(l,len(left))


for _ in range(t):
    n = int(input())
    l = list(map(int, str.split(input())))
    weirdSort(l, n)
    print(" ".join(map(str,l)))
