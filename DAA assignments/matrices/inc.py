def matrix_multiply(A, B):
    n = len(A)
    m = len(B[0])
    C = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C



A = [[1, 2,3]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = matrix_multiply(A, B)
print(result)
