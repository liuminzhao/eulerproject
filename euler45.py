count = 0

n = 1
import math
while count <= 2:
    tmp = n*(2*n - 1)
    p = math.floor(math.sqrt(tmp*2/3))+1
    t = math.floor(math.sqrt(tmp*2))
    if tmp == p*(3*p-1)/2 and tmp == t*(t+1)/2:
        print(n)
        count += 1
    n += 1


print(tmp)
