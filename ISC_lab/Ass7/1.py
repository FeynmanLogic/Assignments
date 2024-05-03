from sympy import isprime,primerange,randprime
n=13
if (isprime(n)):
    print("given numbere isprime")
print("Generating elements between 10 and 30")
a=list(primerange(10,30))
print(a)
print("Returning random prime number between 10 and 30")
ran=randprime(10,30)
print(ran)
