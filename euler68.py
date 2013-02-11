import itertools
x = list(itertools.permutations(range(1, 11)))

        

def num(a):
    index = a.index(min(a[5:10]))
    if index == 5:
        return int(str(a[5])+str(a[0])+ str(a[1]) + str(a[6]) + str(a[1]) + str(a[2]) + str(a[7]) + str(a[2])+ str(a[3])+ str(a[8]) + str(a[3]) + str(a[4]) + str(a[9]) + str(a[4]) + str(a[0]))
    elif index == 6:
        return int( str(a[6]) + str(a[1]) + str(a[2]) + str(a[7]) + str(a[2])+ str(a[3])+ str(a[8]) + str(a[3]) + str(a[4]) + str(a[9]) + str(a[4]) + str(a[0])+ str(a[5])+str(a[0])+ str(a[1]))
    elif index == 7:
        return int(str(a[7]) + str(a[2])+ str(a[3])+ str(a[8]) + str(a[3]) + str(a[4]) + str(a[9]) + str(a[4]) + str(a[0])+ str(a[5])+str(a[0])+ str(a[1]) +  str(a[6]) + str(a[1]) + str(a[2]) )
    elif index == 8:
        return int( str(a[8]) + str(a[3]) + str(a[4]) + str(a[9]) + str(a[4]) + str(a[0])+ str(a[5])+str(a[0])+ str(a[1]) +  str(a[6]) + str(a[1]) + str(a[2]) +str(a[7]) + str(a[2])+ str(a[3]))
    else :
        return int( str(a[9]) + str(a[4]) + str(a[0])+ str(a[5])+str(a[0])+ str(a[1]) +  str(a[6]) + str(a[1]) + str(a[2]) +str(a[7]) + str(a[2])+ str(a[3]) + str(a[8]) + str(a[3]) + str(a[4]) )

ans  = 0

for y in x:
    if y[5]+y[0]+y[1] == y[6]+y[1]+y[2] == y[7]+y[2]+y[3] == y[3]+y[4]+y[8] == y[9] + y[4]+y[0]:
        print y
        tmp = num(y)
        if len(str(tmp)) == 16:
            if tmp > ans:
                ans = tmp
            
print ans
