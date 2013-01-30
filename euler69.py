__author__ = 'liuminzhao'

import math
prime= [x for x in range(2,50) if not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]]
def isprime(x):
    return not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]


def isrprime(a, b):
    minab = min(a, b)
    maxab = max(a, b)
    for i in range(2, minab + 1):
        if not a%i and not b%i :
            return False
    return True

def countprime(n):
    count = 1
    for i in range(2, n):
        if isrprime(n, i):
            count += 1
    return count

rate = 0
want = 1

target = [one for one in range(2, 10001) if not isprime(one)]

for i in target:
    tmp = float(i)/countprime(i)
    if tmp > rate:
        rate = tmp
        want = i
    if i%10000 == 0:
        print i

print want, rate

### bad idea

## borrow from online
prime= [x for x in range(2,50) if not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]]

n = 1000000
tmp = 1
i = 0
for i in prime:
    if tmp * i > n:
        break
    else:
        tmp *= i
print tmp