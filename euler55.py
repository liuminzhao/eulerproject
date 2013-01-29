__author__ = 'liuminzhao'

def isPalin(n):
    num = str(n)
    if n == int(num[::-1]):
        return True
    else:
        return False

def isLychrel(n):
    count = 1
    n = n + int(str(n)[::-1])
    while count <= 50:
        if isPalin(n):
            return False
        else:
            n = n + int(str(n)[::-1])
            count += 1
    return True

count = 0
for i in  range(10000):
    if isLychrel(i):
        count += 1

print count