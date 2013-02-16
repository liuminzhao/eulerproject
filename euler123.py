# r = 2na mod a**2 for n is odd
import time
b = time.time()
import numpy
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]
n = 1000000
prime = primesfrom2to(n)
i = 1
while 1:
    if 2*i*prime[i-1]%prime[i-1]**2 > 10**10:
        print i
        break
    i += 2

print time.time()-b

