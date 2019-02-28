import numpy as np
import os

def glouton_hamiltonien(dist_matrix, dic):
    """
    Select edges with biggest weight and sort them in order to get a cycle
    :param dist_matrix: Distance matrix
    :return: Text file corresponding to slideshow
    """
    n = dist_matrix.shape[0]
    degree = np.zeros(n, dtype = int)
    mat = np.reshape(dist_matrix, (1, n*n))[0]
    print(mat)
    new_ind = np.argsort(mat)[::-1]
    print(new_ind)
    selected_edges = set()
    i = 0
    while i < n*n and mat[new_ind[i]] > 0:
        x, y = new_ind[i] // n, new_ind[i] % n
        if degree[x] < 2 and degree[y] < 2 and (min(x,y), max(x,y)) not in selected_edges:
            degree[x] += 1
            degree[y] += 1
            selected_edges.add((min(x,y), max(x,y)))
        i += 1
    print(selected_edges)
    cycle = []

    adj_lists = {}
    for x, y in selected_edges:
        if x not in adj_lists.keys():
            adj_lists[x] = []
        adj_lists[x].append(y)
        if y not in adj_lists.keys():
            adj_lists[y] = []
        adj_lists[y].append(x)

    deg_one = np.argwhere(degree==1)

    to_process = set()
    processed = set()
    for x in range(n):
        if degree[x] > 0:
            to_process.add(x)

    for i in deg_one:
        if i in processed:
            continue
        cycle.append(i)
        processed.add(i)
        x = adj_lists[i][0]
        while degree[x] > 1:
            cycle.append(x)
            processed.add(x)
            y = adj_lists[x][0] if adj_lists[x][0] != x else adj_lists[x][1]
            x = y
        cycle.append(x)
        processed.add(x)

    to_process.difference_update(processed)
    while len(to_process) > 0:
        i = to_process.pop()
        cycle.append(i)
        processed.add(i)
        x = adj_lists[i][0]
        while x not in processed:
            cycle.append(x)
            processed.add(x)
            y = adj_lists[x][0] if adj_lists[x][0] != x else adj_lists[x][1]
            x = y
        to_process.difference_update(processed)

    write_output(cycle, dic)

def write_output(cycle, dic):
    example = os.environ['NB']

    with open("ex{}{}.txt".format(example, "output"), 'w') as file:
        file.write("{}\n".format(len(cycle)))
        for x in cycle:
            file.write(dic[x])

