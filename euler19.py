import datetime
startday = datetime.date(1901, 1,1)
print(startday.weekday())
count = 0
endday = datetime.date(2000, 12, 31)

cur = startday

while cur <= endday :
    if cur.weekday()==6 and cur.day==1:
        count +=1
    cur += datetime.timedelta(days=1)

print(count)
