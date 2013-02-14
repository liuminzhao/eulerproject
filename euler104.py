a = 1
b = 1
n = 2

pandi = [str(one) for one in range(1, 10)]
for i in range(3000000):
    if i%10000 == 0: print i
    a, b = b, a + b
    n += 1
    tail  = b%10**9
    if  pandi  == sorted(set(str(tail))):
        head = str(b)[:9]
        if sorted(set(head)) == pandi:
            print n
            break

