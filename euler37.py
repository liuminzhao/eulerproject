__author__ = 'liuminzhao'

import math

prime= [x for x in range(2,1000000) if not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]]

def istrun(n):
    num = str(n)
    l = len(num)
    if l == 1:
        return False
    else:
        for i in range(l - 1):
            left = int(num[(i+1):])
            right = int(num[:(i+1)])
            if not left in prime or not right in prime:
                return False
        return True

count = 0

total = 0

i = 4

while count < 11:
    if istrun(prime[i]):
        count += 1
        total += prime[i]
        print prime[i]
    i += 1

print total
