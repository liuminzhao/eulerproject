import math
def IsPrime(n):
    if not n%2 :
        return False
    if not n%3 or n==1:
        return False
    i = 5
    while n%i and i< int(math.sqrt(n)):
        i += 2
    if i< int(math.sqrt(n)):
        return False
    else :
        return True

def quad(n, a, b):
    return n**2+a*n+b

num = []
tmp = 41
asave = []
bsave = []
tmp2 = 1

for b in range(11, 1001, 2):
    for a in range(-999, 999, 2):
        count = 0
        n = 0
        tmp2 = quad(n,a,b)
        while tmp2>0 and  IsPrime(tmp2) :
            n += 1
            count += 1
            tmp2=quad(n,a,b)
        if count>tmp:
            tmp = count
            num.append(n)
            asave.append(a)
            bsave.append(b)
print(num)
print(tmp)
print(asave)
print(bsave)
            
        
