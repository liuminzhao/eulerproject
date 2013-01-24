__author__ = 'liuminzhao'

def ispalin(n):
    numstr = str(n)
    if numstr == numstr[::-1]:
        return True
    else :
        return False

total = 0

for i in range(1, 1000000):
    if ispalin(i) and ispalin(bin(i)[2:]):
        print i
        total += i

print total