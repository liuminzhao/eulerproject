import math

n = 1000000
i = 9

# i = 2
# n= 4

x = range(0, i+1)

tmp = True

while tmp :
    div = n/math.factorial(i)
    if not n%math.factorial(i) :
        print(x[div-1])
        x.remove(x[div-1])
        break
    else:
        print(x[div])
        x.remove(x[div])
        n = n%math.factorial(i)
        i -= 1

print(sorted(x, reverse=True))

