from itertools import combinations

a1 = [str(one) for one in range(10)]
a2 = a1

b1 =  [one for one in combinations(a1, 6)]
b2 =  [one  for one in combinations(a2, 6)]

#for one in b :
#    print one
count = 0

for i in b1:
    if '6' in i:
        i+= ('9',)
    elif '9' in i:
        i+= ('6',)
    for j in b2:
        tmp = []
        if '6' in j:
            j+= ('9',)
        elif '9' in j:
            j += ('6',)
        for x in i:
            for y in j:
                tmp.append(int(x+y))
                tmp.append(int(y+x))
        if 1 in tmp and 4 in tmp and 9 in tmp and 16 in tmp and 25 in tmp and 36 in tmp and 49 in tmp and 64 in tmp and 81 in tmp:
            count += 1

print count/2
