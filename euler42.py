f = open('words.txt', 'r')
name= [one.strip('"') for one in f.readline().split(",")]

def score(x):
    return sum([ord(one)-64 for one in x])

count = 0
import math
for i in range(len(name)):
    x = name[i]
    s = score(x)
    tmp = math.floor(math.sqrt(s*2))
    if s*2==tmp*(tmp+1):
        count += 1

print(count)
