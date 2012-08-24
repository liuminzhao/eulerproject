count = 0

n  = 23 

import math

def ncr(n, r):
    return math.factorial(n)/math.factorial(r)/math.factorial(n-r)

while n <= 100:
    for i in range(n):
        if ncr(n, i) > 1000000 :
            count += 1
    n += 1

print(count)
