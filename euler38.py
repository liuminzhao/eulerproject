__author__ = 'liuminzhao'

# 10002
# 1002003
# 102030405

import itertools

x = list(itertools.permutations("987654321"))

for num in x:
    tmp = ""
    for i in range(9):
        tmp += num[i]
    tmp = int(tmp)
    if tmp%100002 == 0:
        print tmp
        print tmp/100002

