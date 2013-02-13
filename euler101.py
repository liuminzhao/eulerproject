a = [[j**i for i in range(12)] for j in range(1,12)]
print a
import numpy as np
b = np.matrix(a)
print b[:3,:3]

z = [[one**3] for one in range(1, 4)]

for d in range(2, 4):
    sol = b[:d, :d]**-1 * np.mat(z[:d])
    print int(b[d, :d]*sol)

def pgf(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

ans = [[pgf(one)] for one in range(1, 11)]
total = 1
for d in range(2, 11):
    sol = b[:d, :d]**-1 * np.mat(ans[:d])
    total += int(b[d, :d]*sol)
print total

# 2 less than true answer
