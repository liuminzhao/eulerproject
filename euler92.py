__author__ = 'liuminzhao'

n = 4
def chain(n):
    while True:
        if n == 1 or n == 89:
            return n
        else:
            n = sum([int(one)**2 for one in str(n)])

count = 0
for i in range(1, 10000000):
    if chain(i) == 89:
        count += 1
    if i%10000 == 0:
        print i
print count

# should create 1: 81*7 key dict , reduce the time dramatically