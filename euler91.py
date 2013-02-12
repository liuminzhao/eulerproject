p  = 50
count = 0
for x2 in range(1, p+1):
    for y2 in range(1, p+1):
        for x1 in range(1, x2):
            for y1 in range(1, p+1):
                a2 = x1**2 + y1**2
                b2 = x2**2 + y2**2
                c2 = (x1-x2)**2 + (y1-y2)**2
                if a2 + b2 == c2 or a2 + c2 == b2 or a2 == b2 + c2:
                    count += 1
count2 = 0
for x2 in range(2, p+1):
    y2 = 0
    for x1 in range(1, x2):
        for y1 in range(1, p+1):
            a2 = x1**2 + y1**2
            b2 = x2**2 + y2**2
            c2 = (x1-x2)**2 + (y1-y2)**2
            if a2 + b2 == c2 or a2 + c2 == b2 or a2 == b2 + c2:
                count2 += 1
print count + p*p*2 + p*p + count2*2
