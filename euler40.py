x= ''
i = 1
while len(x)<1000000 :
    x += str(i)
    i += 1
    
print(int(x[0])*int(x[9])*int(x[99])*int(x[999])*int(x[9999])*int(x[99999])*int(x[999999]))
