import numpy as np

def strassen_multiply(A, B):
    n = A.shape[0]
    

    if n == 1:
        return A * B
    

    A11 = A[:n//2, :n//2]
    A12 = A[:n//2, n//2:]
    A21 = A[n//2:, :n//2]
    A22 = A[n//2:, n//2:]
    B11 = B[:n//2, :n//2]
    B12 = B[:n//2, n//2:]
    B21 = B[n//2:, :n//2]
    B22 = B[n//2:, n//2:]
    

    P1 = strassen_multiply(A11 + A22, B11 + B22)
    P2 = strassen_multiply(A21 + A22, B11)
    P3 = strassen_multiply(A11, B12 - B22)
    P4 = strassen_multiply(A22, B21 - B11)
    P5 = strassen_multiply(A11 + A12, B22)
    P6 = strassen_multiply(A21 - A11, B11 + B12)
    P7 = strassen_multiply(A12 - A22, B21 + B22)

    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    C = np.zeros((n, n))
    C[:n//2, :n//2] = C11
    C[:n//2, n//2:] = C12
    C[n//2:, :n//2] = C21
    C[n//2:, n//2:] = C22
    
    return C
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = strassen_multiply(A, B)
print(C)
