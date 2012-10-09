prime= [x for x in range(2,20000) if not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]]

n = 33

import math

while 1:
    i = 0
    flag = False
    if not n in prime:
        while prime[i] < n:
            tmp = (n - prime[i])/2
            if int(math.sqrt(tmp)) == math.sqrt(tmp) :
                flag = True
                break
            i += 1
        if flag==False:
            print(n)
            break
    n += 2
