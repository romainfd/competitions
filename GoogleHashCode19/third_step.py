import os
import numpy as np
from tqdm import tqdm

def compute_interest(tag1, tag2):
    """
    it computes the interest factor between two consecutive images
    :param tag1: tag of first image
    :param tag2: tag of second image
    :return: interest factor between the two images
    """
    inter = set(tag1).intersection(tag2)
    unique1 = 0
    unique2 = 0
    for tag in tag1:
        unique1 += not(tag in inter)
    for tag in tag2:
        unique2 += not(tag in inter)
    return min(len(inter), unique1, unique2)

n = int(input()) // 8
ids = [0]*n
tags = [0]*n
for i in tqdm(range(n)):
    photo = list(str.split(input(), " "))
    tmp = str.split(photo[0], ",")
    if len(tmp)>1:
        id = tmp[0]+" "+tmp[1]
    else:
        id = photo[0]
    ids[i] = id
    tags[i] = photo[3:]

graph = np.zeros((n,n), dtype = int)
for i in tqdm(range(n)):
    for j in range(i+1, n):
        interest = compute_interest(tags[i], tags[j])
        graph[i][j] = interest
        graph[j][i] = interest


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

    print("adj_list_ok")
    deg_one = np.argwhere(degree==1)

    to_process = set()
    processed = set()
    for x in range(n):
        if degree[x] > 0:
            to_process.add(x)

    for i in deg_one:
        i = i[0]
        print(i)
        if i in processed:
            continue
        cycle.append(i)
        processed.add(i)
        x = adj_lists[i][0]
        while degree[x] > 1 and x not in processed:
            cycle.append(x)
            processed.add(x)
            y = adj_lists[x][0] if adj_lists[x][0] != x else adj_lists[x][1]
            x = y
        if x not in processed:
            cycle.append(x)
            processed.add(x)

    print("deg_one over")

    to_process.difference_update(processed)
    while len(to_process) > 0:
        i = to_process.pop()
        cycle.append(i)
        processed.add(i)
        print(i)
        x = adj_lists[i][0]
        while x not in processed:
            cycle.append(x)
            processed.add(x)
            y = adj_lists[x][0] if adj_lists[x][0] != x else adj_lists[x][1]
            x = y
        to_process.difference_update(processed)

    write_output(cycle, dic)

def write_output(cycle, dic):
    example = 2

    with open("ex{}{}.txt".format(example, "_output"), 'w') as file:
        file.write("{}\n".format(len(cycle)))
        for x in cycle:
            file.write(dic[x])
            file.write('\n')

glouton_hamiltonien(graph, ids)
