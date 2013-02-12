ans = 0
from fractions import gcd
for m in range(2, 18300):
    for n in range(m-1, 0, -2):
        if gcd(m, n) == 1:
            if abs(m**2 - 3*n**2) == 1:
                L = 2*(m**2 + n**2) + 2*m**2 - 2*n**2
                if L <= 1000000000:
                    ans += L
            elif abs(m**2 + n**2 - 4*m*n) == 1:
                L = 2*(m**2 + n**2) + 4*m*n
                if L <= 1000000000:
                    ans += L
print ans
                
                
