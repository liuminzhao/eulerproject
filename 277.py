# 277

import math

prime = [x for x in range(2, 200) if not [t for t in range(2, int(math.sqrt(x)) + 1) if not x % t]]
n = 10**15
i = 0
text = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'
maxlen = len(text)
n0 = n

def isgood(n, subtext):
    for i in range(len(subtext)):
        if  ( n % 3 == 0):
            if not (subtext[i] == 'D'):
                return False
            n = n/3
        elif (n%3 == 1):
            if not (subtext[i] == 'U'):
                return False
            n = (4*n + 2)/3
        elif (n%3 == 2):
            if not (subtext[i] == 'd'):
                return False
            n = (2*n - 1)/3
    return True

step = 1

for j in range(maxlen):
    sub = text[0:(j+1)]
    while not isgood(n, sub):
        n = n + step
        print n
    step *=3
    print n, j

print n

