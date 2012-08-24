n = 10 

def factor(n):
    return [ x for x in range(1, n) if not n%x]

print(factor(n))

total = 0

for i in range(2,10000):
    j = sum(factor(i))
    if j> i :
        if sum(factor(j))==i:
            total += i+j

print(total)
