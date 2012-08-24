x = str(2**1000)
tmp=0
for i in range(len(x)):
    tmp += int(x[i])
print(tmp)

# sum([int(one) for one in str(2**1000)])
