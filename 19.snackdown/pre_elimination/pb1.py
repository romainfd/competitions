t = int(input())

for _ in range(t):
    n = int(input())
    row = list(map(lambda c: True if c == '#' else False, list(input())))

    # we find the first box to move
    i = 0
    while i < n and row[i]:
        i += 1
    if i == n:
        print(0)  # only boxes
    else:
        # first hole

        total_cost = 0
        not_enough_place = False
        # i est sur le premier trou
        d = 0
        while i < n and not not_enough_place:
            while i < n and not row[i]:
                i += 1
                d += 1
            if i == n:
                break  # boxes already on the left
            else:
                # first box to be moved
                j = 1
                c = 1
                while 2 * c > j:
                    if i + j >= n:
                        not_enough_place = True
                        break
                    elif row[i + j]:
                        # we have another box to move
                        total_cost += 2 * c - j  # we have to move it backward first
                        c += 1
                    j += 1

                # we found enough place for this batch
                total_cost += c * (d - 1) + ((c * (c + 1)) // 2)  # we can move them forward
                i += j
                d = d + c  # on le place sur le premier trou
        if not not_enough_place:  # all good !
            print(total_cost)
        else:
            print(-1)