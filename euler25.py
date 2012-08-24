from math import *
a1 = 1
a2 = 1
a3= 2

count = 3
while len(str(int(a3))) <1000 :
    a1 = a2
    a2 = a3 
    a3 = a1+a2
    count += 1

print(count)

