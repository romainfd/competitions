t = int(input())

for _ in range(t):
    digits = list(map(int, list(input())))

    if len(digits) == 1:
        nb=digits[0]
        print(min(nb, 9 - nb))
    else:
        s = sum(digits)
        if s <= 9:
            print(9 - s)
        else:
            print(min(s % 9, 9 - (s % 9)))
