import time
import numpy as np
a = time.time()
count = 0
peter = [0]*37
colin = [0]*37
for a1 in range(1, 5):
    for a2 in range(1, 5):
        for a3 in range(1, 5):
            for a4 in range(1, 5):
                for a5 in range(1, 5):
                    for a6 in range(1, 5):
                        for a7 in range(1, 5):
                            for a8 in range(1, 5):
                                for a9 in range(1, 5):
                                    peter[a1+a2+a3+a4+a5+a6+a7+a8+a9] += 1.0/4**9

for a1 in range(1, 7):
    for a2 in range(1,7):
        for a3 in range(1,7):
            for a4 in range(1,7):
                for a5 in range(1,7):
                    for a6 in range(1,7):
                        colin[a1+a2+a3+a4+a5+a6] += 1.0/6**6
print peter, colin,  sum(peter), sum(colin)
colincumsum = np.cumsum(colin)
total = 0
for i in range(1, 37):
    total += peter[i]*colincumsum[i-1]
print total
print time.time() - a

