__author__ = 'liuminzhao'

a = 3
b = 2
count = 0

for i in range(999):
    a = a + b * 2
    b = a - b
    if len(str(a)) > len(str(b)):
        count += 1

print count