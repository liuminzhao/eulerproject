__author__='liuminzhao'

f = open('matrix.txt', 'r')

mat = [[0 for i in range(80)] for j in range(80)]
i = 0

for a in f:
    b = [int(one) for one in a.split(',')]
    mat[i] = b
    i += 1

f.close()

tmp = [0 for i in range(80)]

import numpy as np
mat = np.array(mat)

for j in range(1, 80):
    tmp[0] = min([mat[one, j-1] + sum(mat[:(one+1), j]) for one in range(80)])
    tmp[79] = min([mat[one, j-1]+ sum(mat[one:, j]) for one in range(80)])
    for i in range(1, 79):
        tmp[i] = min(min([mat[one,j-1]+sum(mat[one:(i+1), j]) for one in range(i)]), mat[i, j-1] + mat[i, j], min([mat[one, j-1] + sum(mat[i:(one+1), j]) for one in range(i+1, 80)]))
    for i in range(80):
        mat[i,j] = tmp[i]

print min(mat[:,79])


# mat = [[131,673,234,103,18],
# [201,	96,	342,965,	150],
# [630,	803,	746,422,	111],
# [537,	699,	497,121,	956],
# [805,	732,	524,37,331]]

# mat = np.array(mat)
# tmp = [0 for i in range(5)]

# for j in range(1, 5):
#     tmp[0] = min([mat[one, j-1] + sum(mat[:(one+1), j]) for one in range(5)])
#     tmp[4] = min([mat[one, j-1]+ sum(mat[one:, j]) for one in range(5)])
#     for i in range(1, 4):
#         tmp[i] = min(min([mat[one,j-1]+sum(mat[one:(i+1), j]) for one in range(i)]), mat[i, j-1] + mat[i, j], min([mat[one, j-1] + sum(mat[i:(one+1), j]) for one in range(i+1, 5)]))
#     print tmp
#     for i in range(5):
#         mat[i,j] = tmp[i]

# print min(mat[:,4])
