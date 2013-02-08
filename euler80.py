__author__= 'liuminzhao'

# need decimal package

import decimal as dc

sq = [one**2 for one in range(1, 11)]
total = 0
dc.getcontext().prec = 102

for i in range(1, 101):
    if i not in sq:
        a = int(dc.Decimal(i).sqrt()*10**99)
        total += sum(int(one) for one in str(a))

print total


