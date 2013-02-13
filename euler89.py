f = open('roman.txt', 'r')

bad1 = ['VIIII', 'LXXXX','DCCCC']
bad2 = ['IIII', 'XXXX', 'CCCC']
def legit(a):
    ans = 0
    if 'VIIII' in a:
        ans += 3
    elif 'IIII' in a:
        ans += 2
    if 'LXXXX' in a:
        ans += 3
    elif 'XXXX' in a:
        ans += 2
    if 'DCCCC' in a:
        ans += 3
    elif 'CCCC' in a:
        ans += 2
    return ans
            
count = 0
for a in f:
    ans = legit(a)
    count += ans
    
        
f.close()

print count 
