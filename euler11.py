f=open('e11.txt','r')

x=[[0 for i in range(20)] for j in range(20)]

for i in range(20):
    for j in range(20):
        x[i][j]=int(f.read(3))

print(x)

result=0

for i in range(20):
    for j in range(17):
        tmp=x[i][j]*x[i][j+1]*x[i][j+2]*x[i][j+3]
        if tmp>result:
            result=tmp

print(result)

for i in range(20):
    for j in range(17):
        tmp=x[j][i]*x[j+1][i]*x[j+2][i]*x[j+3][i]
        if tmp>result:
            result=tmp


print(result)

for i in range(17):
    for j in range(17):
        tmp=x[i][j]*x[i+1][j+1]*x[i+2][j+2]*x[i+3][j+3]
        if tmp>result:
            result=tmp

print(result)

for i in range(17):
    for j in range(17):
        tmp=x[i][19-j]*x[i+1][18-j]*x[i+2][17-j]*x[i+3][16-j]
        if tmp>result:
            result=tmp

print(result)

