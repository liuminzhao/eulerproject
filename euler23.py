def factor(n):
    return [ x for x in range(1, n/2+1) if not n%x]

print(factor(12))

abundant = [ one for one in range(1, 28123) if sum(factor(one))>one]

res = []


for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        tmp = abundant[i]+abundant[j]
        if tmp <= 28123 :
            res.append(tmp)

final= list(set(res))
final2=final[len(final)-1]

print((1+final2)*final2/2 - sum(final))
