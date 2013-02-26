__auther__ = 'Minzhao Liu'
# Project Euler Problem 137
import numpy as np
import scipy as sp
import sympy
import time
import itertools as it
start = time.time()

phi2 = (np.sqrt(5) - 1)/2

def isrprime(a, b):
    minab = min(a, b)
    maxab = max(a, b)
    for i in range(2, minab + 1):
        if not a%i and not b%i :
            return False
    return True

# def findgolden(n):
count = 0
q = 2
lower = np.sqrt(2) - 1
upper = (np.sqrt(5) - 1)/2

# while count < 7:
#     lowerq = int(lower*q) + 1
#     upperq = int(upper * q) + 1
#     for p in range(lowerq, upperq):
#         if isrprime(p, q):
#             gold = p*q*1.0/(q**2 - p*q - p**2)
#             if gold == int(gold):
#                 count += 1
#                 print gold, count, p, q
#     q += 1
p = 1
while count < 15:
    q = (np.sqrt(5*p**2 + 4) + p)/2
    if q == int(q):
        count += 1
        print p, q, p*q, count
    p += 1

print "Time costs ", time.time() - start, " seconds"

# solve q^2 - pq - p^2 = 1
# refer to wolframalpha solver
# 7 sec
