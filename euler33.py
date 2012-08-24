for a in range(1, 10):
    for b in range(1,10):
        if 2*a*(5-b)==(a-b):
            print(a,b,5)

for b in range(1,10):
    for d in range(1,10):
        if 2*(b+5)*(d-b)==d:
            print(b,d)

for b in range(1,10):
    for d in range(1,10):
        if 2*(b-5)*(d-b)==-d:
            print(b-5,b,d)

