def compute_diagonal_sums(matrix, N):
    sums = []
    for i in range(- N + 1, N):
        sum = 0
        for j in range(max(0, -i), min(N, N - i)):
            sum += matrix[j][i + j]
        sums.append(sum)
    return sums


nb_cases = int(input())
for case in range(nb_cases):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split(" "))))
    diag_sums = compute_diagonal_sums(matrix, N)
    max_sum = max(diag_sums)
    print("Case #" + str(case + 1) + ": " + str(max_sum))
