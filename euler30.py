# at most 6 digits number 
res = 0
for x in range(1000000):
    y = str(x)
    total = 0
    for i in range(len(y)):
        total += int(y[i])**5 
    if total == x and x !=1:
        res += x 
print(res)



