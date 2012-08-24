k=7
x=[]

import math

def fn(n):
    x = str(n)
    total = 0
    for i in range(len(x)):
        total += math.factorial(int(x[i]))
    return total

for i in range(10**k):
    if fn(i) == i:
        x.append(i)
        print(i)

print(sum(x)-3)
