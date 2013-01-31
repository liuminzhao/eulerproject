__author__ = 'liuminzhao'

total = [one**3 for one in range(1, 10000)]
length = [len(str(one)) for one in total]

for j in range(1, 13):
    tmp = [one for one in total if len(str(one))==j]
    tmp2 = sorted([sorted(str(one)) for one in tmp])
    count = 0
    for i in tmp2:
        if tmp2.count(i)==5:
            print "done", i
            break

print [one for one in tmp if sorted(str(one))==i]

