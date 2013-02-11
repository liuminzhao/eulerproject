from fractions import gcd

import numpy as np
prime= [x for x in range(2000,5000) if not [t for t in range(2,int(np.sqrt(x))+1) if not x%t]]


nowratio = 100
n = 1
for j in range(len(prime)-1, 2, -1):
    for i in range(j-1, 0, -1):
        p2 = prime[j]
        p1 = prime[i]
        tmpn = p1*p2
        phin = (p1-1)*(p2-1)
        if tmpn < 10000000:
            if sorted(str(phin)) == sorted(str(tmpn)):        
                if tmpn*1.0/phin < nowratio:
                    nowratio, n = tmpn*1.0/phin, tmpn
print n
        


