import numpy as np
from tqdm import tqdm

M, N = map(int, input().split())
nbs = np.array(list(map(int, input().split())))


def start_and_grow(slices_order):
    s = 0
    i = 0
    ids = []
    while i < N:
        slice_id = slices_order[i]
        if s + nbs[slice_id] <= M:
            s += nbs[slice_id]
            ids.append(slice_id)
        i += 1
    return s, ids


taken = []
max_so_far = 0
permutation = np.array(range(N-1, -1, -1))
for _ in tqdm(range(int(N * np.sqrt(N)))):
    nb_slices, slices = start_and_grow(permutation)
    if nb_slices > max_so_far:
        max_so_far = nb_slices
        taken = slices
    permutation = permutation[np.random.permutation(N)]


print(len(taken))
print(" ".join(map(str, taken)))
