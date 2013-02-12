from sympy import divisors
def divsum(n):
    a = divisors(n)
    return sum(a[:len(a)-1])

def chaincount(n):
    chain = [n]
    ans = 1
    a = divsum(n)
    while not a in chain:
        if a > 1000000 or a == 1:
            return 1, 1000000
        chain.append(a)
        a = divsum(a)
        ans += 1
    if a == chain[0]:
        return ans, min(chain)
    else:
        return 1, 1000000

nowcount = 1
nowans = 0
for n in range(12496, 999999):
    tmpcount, tmpans = chaincount(n)
    if tmpcount > nowcount:
        nowcount , nowans = tmpcount, tmpans
    if n%100000==0:
        print n

print nowcount, nowans

