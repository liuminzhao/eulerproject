# print sum ( [ (pos+1) * nv for pos, nv in enumerate([ sum ( [ ord(char) - 64 for char in name ] ) for name in sorted([name.strip('"') for name in open('names.txt','r').readline().split(",")]) ]) ] )
# 871185934
namelist = sorted([name.strip('"') for name in open('names.txt','r').readline().split(",")])

total = 0
for i in range(len(namelist)):
    total += (i + 1) * sum([ord(char) - 64 for char in namelist[i]])

print total
# 871185934

# correct : 871198282

n = open('names.txt').read()
ns = sorted(n.replace('"','').split(','))

scores = 0
for i in range(len(ns)):
    sumc = 0
    for c in ns[i]:
        sumc += ord(c)-64
    scores += sumc*(i+1)
print(scores) #871190344
LETTER_VALUES = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,\
    'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,\
    'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,\
    'Z': 26}

total_sum = 0

for n in range(len(namelist)):
    for letter in namelist[n]:
        sum_name = LETTER_VALUES[letter]
        total_sum += sum_name * (n + 1)

