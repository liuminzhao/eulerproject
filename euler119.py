import numpy as np
import scipy as sp
import time
start = time.time()
# def digitsum(n):
#     ans = 0
#     while 1:
#         ans += n%10
#         n /= 10
#         if n == 0:
#             return ans
# count = 0
# def ispower(n, ds):
#     ds = digitsum(n)
#     if ds == 1 or ds == 0:
#         return False
#     while n != 1:
#         if n%ds :
#             return False
#         else:
#             n /= ds
#     return True

# n = 10
# while count < 10:
#     if ispower(n):
#         count += 1
#         print n
#     n += 1

count = 0
group = []
ds = range(2, 100)
for n in ds:
    tmp = [n**one for one in ds]
    for one in tmp:
        if digitsum(one) == n:
            count += 1
            group.append(one)
            print one
print sorted(group)[29]
            
print time.time() - start

# slow after 10th 
