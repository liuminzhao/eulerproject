__author__ = 'liuminzhao'

count = 9

n = 2

p = 9 - int(10**(float(n-1)/n))

while p > 0:
    count += p
    n += 1
    p = 9 - int(10**(float(n-1)/n))

print count