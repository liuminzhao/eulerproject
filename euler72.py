import sympy as sp

def phi(n):
    a = sp.factorint(n)
    ans = n
    for base in a:
        ans *= 1-1.0/base
    return ans

total = 0
for d in range(2, 1000001):
    total += phi(d)

print total

# take less than 1 min
