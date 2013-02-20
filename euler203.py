import numpy as np
import sympy as sp
import time
start = time.time()

def issquarefree(n):
    index = sp.factorint(n).values()
    if any([one >= 2 for one in index]):
        return False
    else:
        return True
squarefree = [1, 2]
total = 3
pascal = np.array([1, 2])
n = 3
while n <= 50:
    tmp = np.append([0], pascal[:(len(pascal)-1)])
    if n%2 : 
        pascal = np.add(pascal, tmp)
    else:
        pascal = np.append(np.add(pascal, tmp), pascal[len(pascal)-1]*2)
    n += 1
    for i in pascal:
        if i not in squarefree:
            if issquarefree(i):
                squarefree.append(i)
                total += i
print squarefree, total

print time.time() - start
