f=open('e13.txt', 'r')
x=[0 for i in range(100)]
for i in range(100):
    f.seek(i*51)
    x[i]= int(f.read(13))

print(sum(x))
    
# print str(sum(int(line) for line in open('13.txt')))[:10]
