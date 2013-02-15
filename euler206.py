import numpy as np
high = int(np.sqrt(19293949596979899))
low = int(np.sqrt(10203040506070809))
def meet(n):
    num = str(n)
    for i in range(9):
        if num[2*i] == str(i+1):
            continue
        else:
            return False
    return True
    
for i in range(low, high):
    if i%10 == 3 or i%10 ==7:
        if meet(i**2):
            print i**2
            break
