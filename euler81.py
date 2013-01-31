__author__ = 'liuminzhao'

f = open('matrix.txt', 'r')

mat = [[0 for i in range(80)] for j in range(80)]
i = 0

for a in f:
    b = [int(one) for one in a.split(',')]
    mat[i] = b
    i += 1

f.close()

mat[0][1] += mat[0][0]
mat[1][0] += mat[0][0]

for i in range(2, 80):
    mat[i][0] += mat[i-1][0]
    mat[0][i] += mat[0][i-1]
    for j in range(1, i):
        k = i - j
        mat[k][j] += min(mat[k][j-1], mat[k-1][j])

for i in range(1, 80):
    for j in range(i, 80):
        k = 79 + i - j
        mat[j][k] += min(mat[j-1][k], mat[j][k-1])

print mat[79][79]
    
