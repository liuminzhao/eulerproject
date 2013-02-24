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

def isprime(x):
    return not [t for t in range(2,int(np.sqrt(x))+1) if not x%t]

def rad(n):
    base = sympy.factorint(n)
    return np.prod(base.keys())

count, total  = 0, 0
limit = 120000
radset = [0] + [rad(one) for one in range(1, limit+1)]

for c in range(4, limit):
    radc = radset[c]
    if radc < c/2:
        for a in range(1, c/2 + 1):
            b = c - a
            radb = radset[b]
            if radb < c/radc:
                rad = radset[a]*radb*radc
                if rad < c:
                    if isrprime(a, b):
                        count += 1
                        total += c
    if c%10000 == 0:
        print c
        print time.time() - start

print count, total
# for a in range(1, limit/2 + 1):
#     for b in range(a + 1, limit - a):
#         if isrprime(a, b):
#             rad = np.prod(sympy.factorint(a*b*(a+b)).keys())
#             if rad < a+b:
#                 print a, b, a+b
#                 count += 1
#                 total += a+b

print time.time() - start

# answer is 18407904 , but too slow 1552 sec
