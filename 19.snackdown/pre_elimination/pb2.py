t = int(input())

for _ in range(t):
    n, m = map(int, str.split(input(), " "))
    table1 = sorted(filter(lambda x: x != 0, list(map(int, str.split(input(), " ")))))
    table2 = sorted(filter(lambda x: x != 0, list(map(int, str.split(input(), " ")))))
    res = "Alice" if table1 != table2 else "Bob"
    print(res)
