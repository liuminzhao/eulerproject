import numpy as np
import time
start = time.time()
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]
prime = primesfrom2to(10**8/2)
print len(prime)
last = len(prime) - 1
i = 0
count = 0
while prime[i] < 10**4:
    while prime[i]*prime[last] > 10**8:
        last -= 1
    count += last - i + 1
    i += 1
print count 
print time.time() - start
