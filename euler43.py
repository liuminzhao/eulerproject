__author__ = 'liuminzhao'

def meet(n):
    num = str(n)
    a = int(num[1:4])
    b = int(num[2:5])
    c = int(num[3:6])
    d = int(num[4:7])
    e = int(num[5:8])
    f = int(num[6:9])
    g = int(num[7:10])
    if not a%2 and not b%3 and not c%5 and not d%7 and not e%11 and not f%13 and not g%17 :
        return True
    else:
        return False

import itertools

x = list(itertools.permutations("9876543210"))

total = 0

for num in x:
    tmp = ""
    for i in range(10):
        tmp += num[i]
    tmp = int(tmp)
    if meet(tmp):
        print tmp
        total += tmp

print total