import itertools
x = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))

def check1(x):
    if x[0]*(10**3*x[1]+10**2*x[2]+10*x[3]+x[4])==10**3*x[5]+10**2*x[6]+10*x[7]+x[8]:
        return True

def check2(x):
    if (10*x[0]+x[1])*(10**2*x[2]+10*x[3]+x[4])==10**3*x[5]+10**2*x[6]+10*x[7]+x[8]:
        return True

y1=[one for one in x if check1(one)]
y2=[one for one in x if check2(one)]
print(y1)
print(y2)
