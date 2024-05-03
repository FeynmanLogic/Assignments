from sympy import randprime,totient
from time import time
def gennumbers():
    number1=randprime(2**1024-1000,2**1024-1)
    number2=randprime(2**1024-1010,2**1024-1)
    print("Number one is",number1)
    print("Number two is",number2)
    return number1,number2
number1,number2=gennumbers()
print("Totient of first number is",totient(number1))
print("RSA modulus is",number1*number2)
starttime=time()
x=totient(number1*number2)
endtime=time()
print("Phi(n) is",x)
print("Time taken to do this",endtime-starttime)