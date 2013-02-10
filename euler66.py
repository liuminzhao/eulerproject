__author__='liuminzhao'

# limit = 1000000

# square = [one**2 for one in range(limit)]
# square[0] = 1

# import numpy as np
# import math

# def findx(d):
#     t = 1
#     while True:
#         x1 = d*t - 1
#         x2 = d*t + 1
#         y1 = np.sqrt((x1**2 - 1)/d)
#         y2 = np.sqrt((x2**2 - 1)/d)
#         if int(y1) == y1:
#                 return x1
#         if int(y2) == y2:
#                 return x2
#         t += 1
                
# nowx = 3
# nowd = 2
                
# for D in range(1, 1001):
#     sqD = np.sqrt(D)
#     if not sqD == int(sqD):
#         tmpx = findx(D)
#         if tmpx > nowx:
#             nowd = D
#             nowx = tmpx
#     print D

# print nowd

# still too slow , like findx(61)

# check wiki : http://en.wikipedia.org/wiki/Chakravala_method#n_.3D_61

def findx(N):
    a = 1
    b = 0
    k = 1
    m = 1
    sd = np.sqrt(N)
    while k != 1 or b == 0 :
        m = k*(m/k + 1) - m
        m = m - int((m - sd)/k)*k
        a, b, k = (a*m + N*b)/abs(k), (a + b*m)/abs(k), (m**2 - N)/k
    if k == 1:
        return a

def pell(d):
    p, k, x1, y, sd = 1, 1, 1, 0, np.sqrt(d)
 
    while k != 1 or y == 0:
        p = k * (p/k+1) - p
        p = p - int((p - sd)/k) * k
 
        x = (p*x1 + d*y) / abs(k)
        y = (p*y + x1) / abs(k)
        k = (p*p - d) / k
        
        x1 = x
        
    return x
        
nowd = 1
nowx = 3
for d in range(3, 1001):
    if not int(np.sqrt(d))==np.sqrt(d):
        tmpx = findx(d)
        if tmpx > nowx:
            nowx, nowd = tmpx, d
        print d

print nowx, nowd
