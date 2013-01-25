__author__ = 'liuminzhao'

pentagon = [n*(3*n - 1)/2 for n in range(1, 10001)]

diff = 100000

# http://blog.dreamshire.com/2009/04/17/project-euler-problem-44-solution/

def pe44():
    ps = set()
    i = 0
    while True:
        i += 1
        p = (3*i*i - i) / 2
        ps.add(p)
        for n in ps:
            if p-n in ps and p-2*n in ps:
                return p-2*n

print "Answer to PE44 = ", pe44()