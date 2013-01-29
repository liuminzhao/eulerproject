__author__ = 'liuminzhao'

import math
def isprime(x):
    return not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]

p = 1
n = 1
i = 1
count = 0

while p > .1 :
    i += 1
    for j in range(4):
        n +=  2*(i-1)
        if isprime(n):
            count += 1
    p = float(count) / float(1 + 4*(i-1))

print i*2 - 1

#### slow
#n_prime, d, avg, n = 0, 1, 1, 2;
#
#while avg >= 0.10:
#    n_prime += isprime(d + n) + isprime(d + n*2) + isprime(d + n*3)
#    d += n*4
#    n += 2
#    avg = float(n_prime) / (2 * n)
#
#print "Answer to PE58 = ",n-1