t = int(input())

for _ in range(t):
    n, m = map(int, str.split(input(), " "))
    table1 = sorted(list(map(int, str.split(input(), " "))))
    table2 = sorted(list(map(int, str.split(input(), " "))))
    print(table1, table2)
    res = "Alice" if table1 != table2 else "Bob"
    print(res)
