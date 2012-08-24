def getterm(n):
    count = 1
    while n!=1 :
        if not n%2:
            n /= 2
        else:
            n = 3*n +1
        count +=1
    return count

print(getterm(13))

tmp=0
num=1
for i in range(1, 1000000):
    if getterm(i)>tmp:
        tmp = getterm(i)
        num=i
print(num)
print(tmp)
