__author__='liuminzhao'

# def triangle(n):
#     count = 0
#     for a in range(1, n/3 + 1):
#         for b in range(a, (n - a)/2 + 1):
#             c = n - a - b
#             if a**2 + b**2 == c**2 :
#                 count += 1
#             if count > 1:
#                 return 2
#     return count

# count = 0

# for i in range(12, 1500000, 2):
#     if triangle(i) == 1:
#         count += 1
#     if i%1000 == 0:
#         print i

# print count

# slow
from fractions import gcd
import math
limit = 1500000
mlimit = int(math.sqrt(limit/2))
ans = [0]*(limit+1)

for m in range(2, mlimit + 1):
    for n in range(1, m):
        if (m-n)%2 and gcd(m, n) == 1:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            L = a + b + c
            while L <= limit :
                ans[L] += 1
                L += a + c + b

print ans.count(1)

                
