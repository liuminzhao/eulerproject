__author__ = 'liuminzhao'

def isrprime(a, b):
    minab = min(a, b)
    maxab = max(a, b)
    for i in range(2, minab + 1):
        if not a%i and not b%i :
            return False
    return True

count = 0
for d in range(5, 12001):
    for n in range(d/3 + 1, d/2 + 1):
        if isrprime(d, n) :
            count += 1
    if d%1000 ==0 :
        print d
        
print count

# too slow 
