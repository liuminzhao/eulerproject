__author__ = 'liuminzhao'

import math

prime= [x for x in range(2,1000000) if not [t for t in range(2,int(np.sqrt(x))+1) if not x%t]]

# fast prime generator
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


def isprime(x):
    return not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]

import itertools

x = list(itertools.permutations("87654321"))

for num in x:
    tmp = ""
    for i in range(8):
        tmp += num[i]
    tmp = int(tmp)
    if isprime(tmp):
        print tmp
        break

import sympy

sympy.factorint(100)

# letter score
for i in range(len(namelist)):
    total += (i + 1) * sum([ord(char) - 64 for char in namelist[i]])

# gcd
from fractions import gcd
