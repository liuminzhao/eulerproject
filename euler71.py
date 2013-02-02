__author__ = 'liuminzhao'
def isrprime(a, b):
    minab = min(a, b)
    maxab = max(a, b)
    for i in range(2, minab + 1):
        if not a%i and not b%i :
            return False
    return True

for d in range(1000000, 10, -1):
    if (3*d - 1)%7 == 0:
        n = (3*d - 1)/7
        if isrprime(d, n) :
            print n, d
            break

