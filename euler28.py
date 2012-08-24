total = 1
tmp = 1
incre = 2
while tmp<1001*1001:
    for i in range(4):
        tmp += incre
        total += tmp
    incre += 2
print(total)
