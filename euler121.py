import numpy as np
import scipy as sp
import sympy
import time
import itertools as it
start = time.time()

n = 15
a = range(1, n + 1)
total = 0
for i in range(1, n/2 + 1):
    b =  list(it.combinations(a, i))#        print b
    c =  sum([np.prod(one) for one in b])#        print c
    total += c
den = np.prod(range(2, n+2))
print total+1, den
ans= (total+1)*1.0/den
print int(1/ans)
print time.time() - start
