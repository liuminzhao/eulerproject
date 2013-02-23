import numpy as np
import scipy as sp
import sympy
import time
import itertools as it
import math 
start = time.time()

def ncr(n, r):
    return math.factorial(n)/math.factorial(r)/math.factorial(n-r)

ans = 0
for i in range(2, 101):
    l = ncr(9 + i -1, i)
    ans += (l*(102-i)-9)
print ans + 9*i

print time.time() - start
