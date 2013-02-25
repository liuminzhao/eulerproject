__auther__ = 'Minzhao Liu'
# Project Euler Problem 129
import numpy as np
import scipy as sp
import sympy
import time
start = time.time()
def isrprime(a, b):
    minab = min(a, b)
    maxab = max(a, b)
    for i in range(2, minab + 1):
        if not a%i and not b%i :
            return False
    return True

def A(n):
    ans = 2
    x = 11
    while x%n :
        x = 10*(x%n) + 1
        ans += 1
    return ans 
n = 1000001
while A(n) <= 1000000:
    n += 2
    while not isrprime(n, 10):
        n += 2
    if n%10000 == 1:
        print n
print n
print time.time() - start

