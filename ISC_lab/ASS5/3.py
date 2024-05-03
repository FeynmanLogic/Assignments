import numpy as np  

def matrix_multiply(A, B):
    result = [[sum(a * b for a, b in zip(A_row, B_col))
               for B_col in zip(*B)]
              for A_row in A]
    return result

def decrypt(inversematrix, S, n):
    textlist = list(S)
    something = [[0] for _ in range(n)]
    i = 0
    decrypt = ''
    while i < len(textlist) - 1:
        for j in range(n):
            something[j][0] = ord(textlist[i + j]) - 65
        decryptmatrix = matrix_multiply(inversematrix, something)
        for j in range(n):
            decrypt += chr((decryptmatrix[j][0] % 26) + 65)
        i += n

    print("Decrypted text is")
    print(decrypt)
    

    with open('output2.txt', 'w') as output_file:
        output_file.write(decrypt)

def encrypt(matrix, inversematrix, text, n):
    text = text.replace(' ', '').upper()
    textlist = list(text)

    if len(textlist) % n != 0:
        textlist += ['X'] * (n - len(textlist) % n)

    S = ''
    something = [[0] for _ in range(n)]
    i = 0
    while i < len(textlist):
        for j in range(n):
            something[j][0] = ord(textlist[i + j]) - 65
        encryptmatrix = matrix_multiply(matrix, something)
        for j in range(n):
            S += chr((encryptmatrix[j][0] % 26) + 65)
        i += n

    print("Encrypted text is")
    print(S)
    with open("encrypt.txt", "w") as file:
        file.write(S)
    print("Encryption done, now we do decryption")
    decrypt(inversematrix, S, n)

print("Enter n size")
n = int(input("Here: "))
with open('input2.txt', 'r') as file:
    matrix_line = file.readline().strip().split()
    matrix = [list(map(int, matrix_line[i:i + n])) for i in range(0, len(matrix_line), n)]

    inverse_matrix_line = file.readline().strip().split()
    inversematrix = [list(map(int, inverse_matrix_line[i:i + n])) for i in range(0, len(inverse_matrix_line), n)]

    text = file.readline().strip()

encrypt(matrix, inversematrix, text, n)
