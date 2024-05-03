import numpy as np  

def matrix_multiply(A, B):
    result = [[sum(a * b for a, b in zip(A_row, B_col))
               for B_col in zip(*B)]
              for A_row in A]
    return result

def decrypt(inversematrix, S):
    textlist = list(S)
    something = [[0], [0]]
    i = 0
    decrypt = ''
    while i < len(textlist) - 1:
        something[0][0] = ord(textlist[i]) - 65
        something[1][0] = ord(textlist[i + 1]) - 65
        encryptmatrix = matrix_multiply(inversematrix, something)
        char1 = chr((encryptmatrix[0][0] % 26) + 65)
        char2 = chr((encryptmatrix[1][0] % 26) + 65)

        decrypt = decrypt + char1 + char2
        char1 = ''
        char2 = ''

        i = i + 2
    print("Decrypted text is")
    print(decrypt)
    
    # Write decrypted text to output file
    with open('output.txt', 'w') as output_file:
        output_file.write(decrypt)

def encrypt(matrix, inversematrix, text):
    x = []

    print(matrix)
    inversematrix = inversematrix
    plaintext = text
    plaintext = plaintext.replace(' ', '').upper()
    textlist = list(plaintext)

    i = 0
    char1 = ''
    char2 = ''
    S = ''

    something = [[0], [0]]
    if len(textlist) % 2 != 0:
        textlist.append('X')
    while i < len(textlist) - 1:
        something[0][0] = ord(textlist[i]) - 65
        something[1][0] = ord(textlist[i + 1]) - 65
        encryptmatrix = matrix_multiply(matrix, something)
        char1 = chr((encryptmatrix[0][0] % 26) + 65)
        char2 = chr((encryptmatrix[1][0] % 26) + 65)

        S = S + char1 + char2
        char1 = ''
        char2 = ''

        i = i + 2

    print("Encrypted text is")
    print(S)
    with open("encrypt.txt","w") as file:
        file.write(S)
    print("Encryption done, now we do decryption")
    decrypt(inversematrix, S)

with open('input.txt', 'r') as file:
    
    matrix_line = file.readline().strip().split()
    matrix = [list(map(int, matrix_line[i:i+2])) for i in range(0, len(matrix_line), 2)]

    
    inverse_matrix_line = file.readline().strip().split()
    inversematrix = [list(map(int, inverse_matrix_line[i:i+2])) for i in range(0, len(inverse_matrix_line), 2)]

    
    text = file.readline().strip()

encrypt(matrix, inversematrix, text)
