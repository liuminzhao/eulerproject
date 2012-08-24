m = 0 
for a in range(2, 100):
    for b in range(2, 100):
        tmp= sum([int(one) for one in str(a**b)])
        if tmp > m :
            m = tmp

print(m)


