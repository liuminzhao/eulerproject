import math

prime= [x for x in range(2,200) if not [t for t in range(2,int(math.sqrt(x))+1) if not x%t]]
num = 1
count = 5

def getnum(n, a):
    count = 0
    while (not n%a):
        count += 1
        n /= a
    return count


while (num<500):
    count += 1
    tmp = count*(count+1)/2
        
    num = 1

    for x in prime:
        if (not tmp%x):
            num *= (getnum(tmp, x) + 1)
                
print(count)
print(tmp)
