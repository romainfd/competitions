import numpy as np

N, M, K, mod = list(map(int, str.split(input())))

gamma = np.zeros((min(50, N*(N+1)//2)+1, int(N*N/2 + N + 2)), int)
gamma[0,:] = np.ones (int(N*N/2 + N + 2))

for n in range(1, int(N*N/2 + N + 2)):
    for k in range (1, min(50, N*(N+1)//2) + 1):
        gamma[k,n] = (gamma[k-1,n-1] + gamma[k, n-1]) % mod

f = np.zeros((M+1, N+1, N+1, K+1), int)

f[0,1:,1:,0] = np.ones((N,N))
f[1,1:,1:,1] = np.ones((N,N))

for k in range (1, K+1):
    print(k)
    for m in range (k, M+1):
        for j in range(N, 0, -1):
            for i in range(j, 0, -1):
                if k == 1 and m - 1 <= (j-i)*(N-j) + N - i:
                    f[m, j, i, 1] = gamma[m - 1, (j-i)*(N-j) + N - i]
                elif k > 1:
                    for mp in range(m - k + 1):
                        aux = 0
                        for jp in range(j + 1, N + 1):
                            aux += np.sum(f[m - mp - 1, jp, j + 1:jp + 1, k - 1])
                        aux %= mod
                        f[m, j, i, k] += gamma[mp, (j - i) * (N - j) + N - i] * aux
                f[m, j, i, k] %= mod

print (np.sum(f[M, :, :, K]) % mod)