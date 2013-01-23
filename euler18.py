__author__ = 'liuminzhao'

f = open('e18.txt', 'r')

dat = [[0 for i in range(15)] for j in range(15)]

for i in range(15):
    for j in range(i+1):
        dat[i][j] = int(f.read(3))

print dat

total = 0

for i in range(2):
    dat[1][i] +=  dat[0][0]

for i in range(2, 15):
    dat[i][0] += dat[i-1][0]
    dat[i][i] += dat[i-1][i-1]
    for j in range(1, i):
        dat[i][j] += max(dat[i-1][j-1], dat[i-1][j])

print max(dat[14])

f.close()