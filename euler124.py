import sympy as sp
import time
import numpy as np
begin = time.time()
def rad(n):
    base = sp.factorint(n)
    return np.prod(base.keys())
limit = 100000
radn = [(rad(n), n) for n in range(1, limit + 1)]

a = sorted(radn)

print a[9999]
print time.time() - begin
