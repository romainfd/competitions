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

n = int(input())
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
    for j in tqdm(range(i+1, n)):
        interest = compute_interest(tags[i], tags[j])
        graph[i][j] = interest
        graph[j][i] = interest

print(ids)