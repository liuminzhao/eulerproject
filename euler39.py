__author__ = 'liuminzhao'

def triangle(n):
    count = 0
    for a in range(1, n/3 + 1):
        for b in range(a, (n - a)/2 + 1):
            c = n - a - b
            if a**2 + b**2 == c**2 :
                count += 1
    return count

maxsol = 0

for i in range(12, 1001):
    if triangle(i) > maxsol:
        maxsol = triangle(i)
        print maxsol, i

