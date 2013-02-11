import numpy as np
prime= [x for x in range(2,7400) if not [t for t in range(2,int(np.sqrt(x))+1) if not x%t]]

prime2 = [one**2 for one in prime if one**2 < 50000000]
prime3 = [one**3 for one in prime if one**3 < 50000000]
prime4 = [one**4 for one in prime if one**4 < 50000000]

total = []
for a in prime2:
    for b in prime3:
        for c in prime4:
            tmp = a + b + c
            if tmp < 50000000:
                total.append(tmp)

print len(set(total))
