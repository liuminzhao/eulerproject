
def coin1(n):
    return 1

def coin2(n):
    return n/2

def coin5(n):
    div = n/5
    res = n%5
    if n < 5 :
        return 0
    elif div == 1:
        return coin2(res) + coin1(res)
    else :
        ans = 0
        for i in range(1, div + 1):
            restmp = n - i * 5
            ans += coin2(restmp) + 1
        return ans

def coin10(n):
    div = n/10
    res = n%10
    if n < 10:
        return 0
    elif div == 1:
        return coin5(res) + coin2(res) + 1
    else:
        ans = 0
        for i in range(1, div + 1):
            restmp = n - i * 10
            ans += coin5(restmp) + coin2(restmp) + 1
        return ans

def coin20(n):
    div = n/20
    res = n%20
    if n < 20:
        return 0
    elif div == 1:
        return coin10(res) + coin5(res) + coin2(res) + 1
    else:
        ans = 0
        for i in range(1, div + 1):
            restmp = n - i * 20
            ans += coin10(restmp) + coin5(restmp) + coin2(restmp) + 1
        return ans

def coin50(n):
    div = n/50
    res = n%50
    if n < 50:
        return 0
    elif div == 1:
        return coin20(res) + coin10(res) + coin5(res) + coin2(res) + 1
    else:
        ans = 0
        for i in range(1, div + 1):
            restmp = n - i * 50
            ans += coin20(restmp) + coin10(restmp) + coin5(restmp) + coin2(restmp) + 1
        return ans

def coin100(n):
    div = n/100
    res = n%100
    if n < 100:
        return 0
    elif div == 1:
        return coin50(res) + coin20(res) + coin10(res) + coin5(res) + coin2(res) + 1
    else:
        ans = 0
        for i in range(1, div + 1):
            restmp = n - i * 100
            ans += coin50(restmp) + coin20(restmp) + coin10(restmp) + coin5(restmp) + coin2(restmp) + 1
        return ans

def coin200(n):
    return 1

n = 200
print coin200(n) + coin100(n) + coin50(n) + coin20(n) + coin10(n) + coin5(n) + coin2(n) + coin1(n)