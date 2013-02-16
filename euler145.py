def isrev(n):
    a = str(n)
    b = a[::-1]
    c = int(a) + int(b)
    if a[0]=='0' or b[0]=='0':
        return False
    cstr = str(c)
    if '0' not in cstr and '2' not in cstr and '4' not in cstr and '6' not in cstr and '8' not in cstr:
        return True
    else:
        return False
count = 0
import time
a = time.time()
for i in range(1, 1000000):
    if isrev(i):
        count += 1
print count + 540000
print time.time() - a
