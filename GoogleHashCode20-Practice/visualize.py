import numpy as np
import matplotlib.pyplot as plt

m, n = map(int, str.split(input()))
l = np.array(list(map(int, str.split(input()))))

fig, ax = plt.subplots(figsize=(10, 10))
ax.step(np.arange(n), l.cumsum())
ax.hlines(m, 0, len(l))
plt.title(f'M = {m}')
plt.show()
