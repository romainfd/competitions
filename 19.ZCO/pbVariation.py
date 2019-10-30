# Code created by Romain Fouilland for problem:
# https://www.codechef.com/ZCOPRAC/problems/ZCO15002

n, k = map(int, str.split(input()))
values = list(map(int, str.split(input())))

values.sort()

count = 0
index_plus_k = 1
for i, val in enumerate(values):
    while index_plus_k < n and values[index_plus_k] < val + k:
        index_plus_k += 1
    count += n - index_plus_k

print(count)
