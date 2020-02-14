import numpy as np

m, n = map(int, str.split(input()))

l = np.array(list(map(int, str.split(input()))))


def greedy_max(pizzas, sup, ind_max, selected):
    ind = len(pizzas[pizzas <= sup][:ind_max]) - 1
    while ind >= 0:
        selected.append(ind)
        sup -= pizzas[ind]
        ind_max = ind
        ind = len(pizzas[pizzas <= sup][:ind_max]) - 1
    return selected


output = greedy_max(l, m, n, [])

print(len(output))
print(" ".join(map(str, np.sort(output))))
