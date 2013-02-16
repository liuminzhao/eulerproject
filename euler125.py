import time
import numpy as np
start = time.time()
sq = [n**2 for n in range(0, 11000)]
sqcumsum  = np.cumsum(sq)

def ispalin(n):
    num = str(n)
    if num == num[::-1]:
        return True
    else:
        return False
total = []
count = 0
for i in range(len(sqcumsum)-1, 1, -1):
    for j in range(i-1):
        n = sqcumsum[i] - sqcumsum[j]
        if n < 10**8 :
            if ispalin(n):
                count += 1
                total.append(n)

print sum(set(total)), count
print time.time() - start

# slow but correct ; 
