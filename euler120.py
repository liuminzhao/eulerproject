# r = 2na mod a**2 for n is odd
import time
b = time.time()
def rmax(a):
    return max([2*n*a % a**2 for n in range(1, a*a+1) if n%2])
total = 0
for a in range(3, 1001):
    total += rmax(a)
print total
print time.time()-b
# a little bit slow
