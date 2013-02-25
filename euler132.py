__auther__ = 'Minzhao Liu'
# Project Euler Problem 132
import numpy as np
import scipy as sp
import sympy
import time
import itertools as it
start = time.time()

def A(n):
    ans = 2
    x = 11
    while x%n :
        x = 10*(x%n) + 1
        ans += 1
    return ans 

def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = np.ones(n/2, dtype=np.bool)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = False
    return 2*np.nonzero(sieve)[0][1::]+1


primes = primesfrom3to(1000000)
count = 0
total = 0
i = 3
limit = 10**9
while count < 40:
    if not limit%A(primes[i]):
        count += 1
        total += primes[i]
        print primes[i], A(primes[i]), count
    i += 1
print total
print "Time costs ", time.time() - start, " seconds"
 
# 1832 sec too slow
