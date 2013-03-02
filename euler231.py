__auther__ = 'Minzhao Liu'
# Project Euler Problem 231
import numpy as np
import scipy as sp
import sympy
import time
import itertools as it
start = time.time()

def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = np.ones(n/2, dtype=np.bool)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = False
    return 2*np.nonzero(sieve)[0][1::]+1

primes = primesfrom3to(20000000)

primes = np.append([2], primes)

limit = 20000000

part = 5000000

count = [0]*(len(primes))

for ind in range(len(primes)):
    p = primes[ind]
    d = int(np.log(limit)/np.log(p))
    total = 0
    for i in range(1, d + 1):
        t = p**i
        total += limit/t - part/t - (limit - part)/t
    count[ind] = total 

print sum([p * n for p, n in zip(primes, count)])

print "Time costs ", time.time() - start, " seconds"

# 25 sec
