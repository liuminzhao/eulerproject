__auther__ = 'Minzhao Liu'
# Project Euler Problem 130
import numpy as np
import scipy as sp
import sympy
import time
start = time.time()

def A(n):
    ans = 2
    x = 11
    while x%n :
        x = 10*(x%n) + 1
        ans += 1
    return ans 

def isprime(x):
    return not [t for t in range(2,int(np.sqrt(x))+1) if not x%t]

n = 3
count = 0
total = 0
while count < 25:
    while not n%5 or isprime(n):
        n += 2
    if not (n-1)%A(n):
        print 'This is', n
        total += n 
        count += 1
    n += 2
print total 
print time.time() - start
