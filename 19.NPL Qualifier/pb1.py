t = int(input())

for _ in range(t):
    path = input()
    visited = set()
    ordered = []
    for c in path:
        if c not in visited:
            visited.add(c)
            ordered.append(c)
    print("".join(ordered))
