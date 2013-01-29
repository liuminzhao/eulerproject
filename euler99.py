__author__ = 'liuminzhao'

import math

f = open('base_exp.txt', 'r')

maxnum = 0
maxline = 1
l = 1

for n in f:
    num = n.split(',')
    res = int(num[1]) * math.log(int(num[0]))
    if res > maxnum:
        maxline = l
        maxnum = res
    l += 1

print maxline
f.close()