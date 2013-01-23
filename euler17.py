__author__ = 'liuminzhao'

def num1(x):
    if x == 1 or x == 2 or x == 6:
        return 3
    elif x == 4 or x == 5 or x == 9:
        return 4
    elif x == 0:
        return 0
    elif x == 7 or x == 3 or x == 8:
        return 5
    elif x == 10 :
        return 3
    elif x == 11 or x == 12:
        return 6
    elif x == 16 or x == 15:
        return 7
    elif x == 13 or x == 14 or x == 18 or x == 19:
        return 8
    elif x == 17:
        return 9


def num3(x):
    hun = x/100
    res = x%100
    if x == 1000:
        return 11
    elif res == 0:
        return num1(hun) + 7
    elif hun > 0:
        return num1(hun) + 10 + num2(res)
    else :
        return num2(res)

def num2(x):
    hun = x/10
    res = x%10
    if x < 20 :
        return num1(x)
    elif res == 0:
        return dozen(x)
    else :
        return dozen(hun * 10) + num1(res)


def dozen(x):
    if x == 40 or x == 50 or x == 60:
        return 5
    elif x == 20 or x == 30 or x == 80 or x == 90:
        return 6
    elif x == 70:
        return 7

sum([num3(x) for x in range(1, 1001)])