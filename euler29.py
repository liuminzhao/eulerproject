# from math import *
# count = 0 
# x=[]
# for a in range(2, 101):
#     for b in range(2, 101):
#         c = b*log(a)/log(b)
#         if c>=2 and not a==b and c<=100:
#             if abs(c-floor(c)) < 0.00000001:
#                 count += 1
#                 print(a,b)
#                 x.append(a**b)

# print(count)
# print(99*99-count+99)
# y = [int(one) for one in x]
# z = list(set(y))
# print(99*99-len(list(set(y))))

# above are wrong, no idea why

xx =[]
for a in range(2, 101):
    for b in range(2, 101):
        xx.append(a**b)
print(len(list(set(xx))))
