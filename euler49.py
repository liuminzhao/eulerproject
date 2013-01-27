__author__ = 'liuminzhao'

import math

prime= [x for x in range(1000,10000) if not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]]

def number(n):
    num = str(n)
    ans = []
    for i in range(len(num)):
        ans.append(int(num[i]))
    return sorted(ans)



for i in range(len(prime)):
    for j in range(i+1, len(prime)-1):
        a = prime[i]
        b = prime[j]
        c = 2*b - a
        if c in prime and number(a)==number(b) and number(a)==number(c):
            print a, b, c
