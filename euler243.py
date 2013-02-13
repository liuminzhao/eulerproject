import numpy as np
prime= [x for x in range(2,40) if not [t for t in range(2,int(np.sqrt(x))+1) if not x%t]]

n = 1
s = 1
for p in prime:
    s *= (1 -1.0/p)
    n *= p
    if s < 15499.0/94744:
        for i in range(2, p+1):
            tmpn = n * i
            if s*(1+1.0/(tmpn-1)) < 15499.0/94744:
                print p, tmpn
                break


    
