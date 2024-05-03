import random
import numpy as np
def generate_random_matrix(size):
    matrix = [[random.randint(0,25) for _ in range(size)] for _ in range(size)]
    return matrix
size=int(input("Enter size of a matrix to be generated: "))
print("Generate a random matrix, if inverse exists, it can be used as valid hill cipher key")
random_matrix = generate_random_matrix(size)
for row in random_matrix:
    print(row)

np_matrix = np.array(random_matrix)
determinant = np.linalg.det(np_matrix)
if determinant!=0:
    print("Valid")
else:
    print("Invalid")