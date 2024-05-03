from sympy import randprime, totient
import random
import math
from time import time

def keygenerate(x):
    while True:
        e = random.randint(2, x - 1)
        if math.gcd(e, x) == 1:
            break
    print("Public key:", e)
    d = pow(e, -1, x)
    print("Private key:", d)
    return e, d

def gennumbers(bit_length):
    number1 = randprime(2**(bit_length//2 - 1), 2**(bit_length//2) - 1)
    number2 = randprime(2**(bit_length//2 - 1), 2**(bit_length//2) - 1)
    print("Number one is", number1)
    print("Number two is", number2)
    return number1, number2

def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

def decrypt(ciphertext, d, n):
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Main code
bit_length = 1000  # Adjust the bit length as per your requirement
number1, number2 = gennumbers(bit_length)
n = number1 * number2
print("Modulo is:", n)
x = (number1 - 1) * (number2 - 1)
print("Totient is:", x)
e, d = keygenerate(x)
print("Public key is:", e)

message = input("Enter message: ")
ciphertext = encrypt(message, e, n)
print("Encrypted:", ciphertext)

decrypted_message = decrypt(ciphertext, d, n)
print("Decrypted:", decrypted_message)
