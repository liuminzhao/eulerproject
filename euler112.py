import numpy as np
import scipy as sp
import sympy
import time
start = time.time()

def isbouncy(n):
    num = str(n)
    l = len(num)
    flag1, flag2 = 0, 0
    for i in range(1, l):
        if int(num[i]) > int(num[i-1]):
            flag1 = 1
        elif int(num[i]) < int(num[i-1]):
            flag2 = 1
        if flag1*flag2 > 0:
            return True
    return False
count = 0
n = 100
ratio = count*1.0/n
while ratio < 0.99:
    n += 1
    if isbouncy(n):
        count += 1
        ratio = count*1.0/n
    if n%10000 == 0:
        print n
print n    
print time.time() - start
