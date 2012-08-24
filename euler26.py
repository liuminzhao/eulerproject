def cycle(n):
    i = 1
    while not n%2: 
        n /= 2
    while not n%5:
        n /= 5
    while (10**i-1)%n :
        i+=1
    return i

print(cycle(14))

print(max([cycle(one) for one in range(1,1000)]))
