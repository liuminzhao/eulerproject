__author__ = 'liuminzhao'

def prime(n):
    i = 2
    ans = []
    while n > 1 :
        if n%i :
            i += 1
        else:
            n /= i
            if not i in ans:
                ans.append(i)
    return ans

print prime(16)

def keyi(a, b):
    if len(a) != len(b):
        return False
    else:
        return not any([one in b for one in a])

keyi(prime(10), prime(4))



def ep47():
    chain = []
    count = 0
    for i in range(10, 1000000):
        if count == 4 :
            print i-4
            break
        else:
            if len(prime(i))==4:
                chain.append(i)
                count += 1
            else:
                count = 0
        if i%10000 == 0:
            print i

def ep47():
    chain = []
    count = 0
    for i in range(10, 1000000):
        if count == 3 :
            print i-3
            break
        else:
            if len(prime(i))==3:
                chain.append(i)
                count += 1
            else:
                count = 0

print "Answer to Euler Project Problem 47 is :" , ep47()
