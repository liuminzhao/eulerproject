f = open('triangles.txt', 'r')


def oneside(p3, p1, p2): # p3, 0 relative to p1,p2
    if p1[0] == p2[0]:
        return (p3[0]-p1[0])*(-p1[0]) > 0
    else:
        return (-p1[1]-(p2[1]-p1[1])*1.0/(p2[0]-p1[0])*(-p1[0]))*(p3[1]-p1[1]-(p2[1]-p1[1])*1.0/(p2[0]-p1[0])*(p3[0]-p1[0])) > 0

count = 0
for line in f:
    cord = [int(one) for one in line.split(',')]
    point1 = cord[0:2]
    point2 = cord[2:4]
    point3 = cord[4:6]
    if oneside(point1, point2, point3) and oneside(point3, point2, point1) and oneside(point2, point3, point1):
        count += 1
f.close()
print count 

