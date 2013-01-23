__author__ = 'liuminzhao'

import math

prime= [x for x in range(2,1000000) if not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]]

def circular(n):
    numstr = str(n)
    l = len(numstr)
    if l > 1:
        for i in range(l-1):
            new = int(numstr[(i+1):] + numstr[0:(i+1)])
            if not new in prime:
                return False
    return True

count = 0

for num in prime:
    if circular(num):
        count += 1

print count
