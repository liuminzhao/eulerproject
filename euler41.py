__author__ = 'liuminzhao'

import math

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

x = list(itertools.permutations("7654321"))

for num in x:
    tmp = ""
    for i in range(7):
        tmp += num[i]
    tmp = int(tmp)
    if isprime(tmp):
        print tmp
        break