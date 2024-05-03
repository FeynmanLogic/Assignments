from sympy import randprime, totient
import random
from time import time
import math

def keygenerate(x):
    while True:
        e = random.randint(2, x - 1)
        if math.gcd(e, x) == 1:
            break
    print("Public key:", e)
    d = pow(e, -1, x)
    print("This is log of e",math.log2(e))
    print("Private key:", d)
    print("This is log of n",math.log2(n))
    return e, d

def gennumbers():
    number1 = randprime(2**1000//3, 2**1000-1)
    number2 = randprime(2**1000//2, 2**1000-1)
    print("Number one is", number1)
    print("Number two is", number2)
    return number1, number2

number1, number2 = gennumbers()
n = number1 * number2
print("modulo is: ", n)
x = n - number1 - number2 + 1
print("Totient is:", x)
e, d = keygenerate(x)


msg = input("enter msg: ")
listmsg = list(msg)

def encrypt(listmsg, e, n):
    encrypttext = ""
    encryptlist = []
    for i in range(len(listmsg)):
        t = ord(listmsg[i])
        k = pow(t, e, n)
        encryptlist.append(k)
        encrypttext += str(k)
    return encrypttext, encryptlist

def decrypt(encryptlist, d, n):
    return ''.join([chr(pow(char, d, n)) for char in encryptlist])

encrypttext, encryptlist = encrypt(listmsg, e, n)
print("encrypted text is", encrypttext)
decrypttext = decrypt(encryptlist, d, n)
print("Decrypted text is", decrypttext)
