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

import numpy
def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n/2, dtype=numpy.bool)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1
##########

def digitsum(n):
    ans = 0
    while 1:
        ans += n%10
        n /= 10
        if n == 0:
            return ans

# faster than      return sum([int(one) for one in str(n)])
def isrprime(a, b):
    minab = min(a, b)
    maxab = max(a, b)
    for i in range(2, minab + 1):
        if not a%i and not b%i :
            return False
    return True

def isprime(x):
    return not [t for t in range(2,int(np.sqrt(x))+1) if not x%t]

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
