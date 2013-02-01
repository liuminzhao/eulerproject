__author__='liuminzhao'

a1 = 2
a2 = 3
a3 = 8

for i in range(3, 101):
    if i%3 == 0:
        a3 = a2*(i/3)*2 + a1
    else:
        a3 = a1 + a2
    a1 = a2
    a2 = a3

print sum([int(one) for one in str(a3)])
