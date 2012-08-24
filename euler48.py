x = sum([one**one for one in range(1, 1001)])
y= str(x)
l = len(y)
for i in range(10):
    print(y[l-i-1])
