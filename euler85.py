from math import factorial

def ncr(n,r):
    return (factorial(n)/(factorial(r)*factorial(n-r)))

# m*(m-1)/2*n*(n-1)/2
# m*(m-1)*n*(n-1) close to 8000000
# 4th square root of 8m is 53


dist = 10000
nowm = 1
nown = 1
for m in range(2, 100):
    for n in range(2, m):
        rec = ncr(m,2)*ncr(n,2)
        tmp = abs(rec - 2000000)
        if tmp < dist:
            dist, nowm, nown = tmp, m, n
print dist, nowm, nown, (nowm-1)*(nown-1), ncr(nowm,2)*ncr(nown,2)

