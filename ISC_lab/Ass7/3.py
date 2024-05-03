from sympy import randprime
from time import time
starttime=time()
number2=randprime(2**2000-3110,2**2000-1)
endtime=time()
print(number2)
print("Time required to generate this is",endtime-starttime)