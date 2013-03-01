__auther__ = 'Minzhao Liu'
# Project Euler Problem 140
import numpy as np
import scipy as sp
import sympy
import time
import itertools as it
start = time.time()

# A(x) = (x + 3x**2)/(1-x-x**2)
# (2p*q - 3q**2)/(q**2 - pq - p**2) is integer
# (3q^2 - 2pp)/(q**2 - pq - p**2) is integer 
#　or q**2 - pq - p**2 == 1
# (k-3)q^2 + (2-k)pq - kp^2 = 0 ; k > 3

# (a - 3) y^2 + (2 - a) x y - a x^2 == 0 ; a = k 
# y = (sqrt(5 a^2-16 a+4) x+a x-2 x)/(2 (a-3))

possa = []
for a in range(5, 10000):
    tmp = np.sqrt(5*a**2-16*a+4)
    if tmp == int(tmp):
        possa.append(a)

count = 0
q = 2
goldset = []

# while count < 20:
#     p = (np.sqrt(5*q**2 - 4) - q)/2
#     if p == int(p):
#         gold = (3*q**2 - 2*p*q)/(q**2 - p*q - p**2) - 3
#         if gold not in goldset:
#             count += 1
#             print p, q, gold, count, 'type1'
#             goldset.append(gold)
#     for a in possa:
#         p = (np.sqrt(5*a**2 - 16*a + 4) - a + 2) * q *1.0/(2*(a - 3))
#         if p == int(p):
#             gold = (3*q**2 - 2*p*q)/(q**2 - p*q - p**2) - 3
#             if gold not in goldset:
#                 count += 1
#                 print p, q, gold, count, 'type2'
#                 goldset.append(gold)
#     q += 1

a1, b1 = 1, 2
a2, b2 = 2, 5
while count < 40:
    p, q = a1, b1
    gold = (3*q**2 - 2*p*q)/(q**2 - p*q - p**2) - 3
    if gold not in goldset:
        count += 1
        print gold, count
        goldset.append(gold)
    p, q = a2, b2
    gold = (3*q**2 - 2*p*q)/(q**2 - p*q - p**2) - 3
    if gold not in goldset:
        count += 1
        print gold, count
        goldset.append(gold)
    a1, b1 = a1 + b1, a1 + 2*b1
    a2, b2 = a2 + b2, a2 + 2*b2

goldset =  sorted(goldset)
print goldset, goldset[19], sum(goldset[:30])


print "Time costs ", time.time() - start, " seconds"

# found the rule somehow
# 0.07 s 
