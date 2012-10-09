p = 1
lastten = 0

n = 28433

while p <= 7830457:
    n *= 2
    p += 1
    if n > 10**10:
        n = n%10**10
print(n+1)
