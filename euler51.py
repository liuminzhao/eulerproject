__author__ = 'liuminzhao'

import math
prime = [x for x in range(100000,1000000) if not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]]

# n has 0
def meet(n, k):
    num = str(n)
    count  = 0
    for i in num:
        if int(i)==k:
            count += 1
    return count


for n in prime:
    if meet(n, 1) == 3:
        count = 0
        for i in range(0, 10):
            newdigit = str(i)
            new = int(str(n).replace("1", newdigit))
            if new in prime:
                count += 1
        if count == 8:
            print n
