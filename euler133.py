__auther__ = 'Minzhao Liu'
# Project Euler Problem 133
import numpy as np
import scipy as sp
import sympy
import time
import itertools as it
start = time.time()

# R(n) % p == pow(10, n, p) == 1

prime= [x for x in range(7,100000) if not [t for t in range(2,int(np.sqrt(x))+1) if not x%t]]

total = 2 + 3 + 5

def A(n):
    ans = 2
    x = 11
    while x%n :
        x = 10*(x%n) + 1
        ans += 1
    return ans 

for i in prime:
    Ai = A(i)
    base = sympy.factorint(Ai).keys()
    if base == [2] or base == [5] or base == [2, 5]:
        continue
    else:
        total += i

print total 

print "Time costs ", time.time() - start, " seconds"

# 80 sec 453647705
