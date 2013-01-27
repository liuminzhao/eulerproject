__author__ = 'liuminzhao'

flushsuit = ['HHHHH', 'SSSSS', 'CCCCC', 'DDDDD']
straightnumber =['23456', '34567', '45678', '56789', '6789T', '789TJ' , '89TJQ', '9TJQK', 'TJQKA']
card = ['2' ,'3', '4', '5','6','7','8','9','T','J','Q','K','A']
carddict = {'2':2 ,'3':3, '4':4, '5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

def Score(suit, number):
    if suit in flushsuit and number == 'TJQKA':
        return (10, 'A')
    elif suit in flushsuit and number in straightnumber:
        return (9, number[4])
    elif any([number.count(one) == 4 for one in card]) :
        for one in card:
            if number.count(one) == 4:
                return (8, one)
    elif any([number.count(one)==3 for one in card]) and any([number.count(one)==2 for one in card]) :
        for one in card:
            if number.count(one) ==3:
                return (7, one)
    elif suit in flushsuit:
        return (6, number[4])
    elif number in straightnumber:
        return (5, number[4])
    elif any([number.count(one)==3 for one in card]):
        for one in card:
            if number.count(one) == 3:
                return(4, one)
    elif sum([number.count(one)==2 for one in card])==2:
        ans = []
        for one in card:
            if number.count(one) == 2:
                ans.append(one)
        for one in ans:
            number = number.replace(one, '')
        return (3, ans.append(number))
    elif sum([number.count(one)==2 for one in card])==1:
        for one in card:
            if number.count(one) == 2:
                return (2, [number.replace(one, ''), one])
    else:
        return(1, number)

def beat(a, b):
    n = len(a)
    for i in range(n-1, -1, -1):
        if carddict[a[i]] > carddict[b[i]] :
            return True
        elif carddict[a[i]] < carddict[b[i]]:
            return False

count = 0
f = open("poker.txt", "r")

for twohand in f:

    suit1 = twohand[1:14:3]
    number1 = ''.join(sorted(twohand[0:14:3], key = carddict.get))
    # need to define sorted
    suit2 = twohand[16:29:3]
    number2 = ''.join(sorted(twohand[15:29:3], key = carddict.get))
    # need to define sorted

    (score1, max1) = Score(suit1, number1)
    (score2, max2) = Score(suit2, number2)


    if score1 > score2:
        count += 1
    elif score1 == score2 and score1 > 3:
        if carddict[max1[0]] > carddict[max2[0]]:
            count += 1
    elif score1 == score2 and score1 == 3:
        if carddict[max1[1]] > carddict[max2[1]]:
            count += 1
        elif carddict[max1[1]] == carddict[max2[1]]:
            if carddict[max1[0]] > carddict[max2[0]]:
                count += 1
            elif carddict[max1[0]] == carddict[max2[0]]:
                if carddict[max1[2]] > carddict[max2[2]]:
                    count += 1
    elif score1 == score2 and score1 == 2:
        if carddict[max1[1]] > carddict[max2[1]]:
            count += 1
        elif carddict[max1[1]] == carddict[max2[1]]:
            if beat(max1[0], max2[0]):
                count += 1
    elif score1 == score2 and score1 == 1:
        if beat(max1, max2):
            count += 1

f.close()

print count