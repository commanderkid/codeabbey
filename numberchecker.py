def cardNumb(x : list):
    answer = 0
    for i in range(len(x)):
        if (i + 1) % 2 == 0:
            answer += nonEven(x[i])
        else:
            answer += x[i]
    return answer

def nonEven(x):
    if x > 4:
        return x * 2 - 9
    else:
        return x * 2

def changeArr(y, i):
    x = list(reversed(y[:]))
    per = x[i]
    x[i] = x[i + 1]
    x[i + 1] = per
    x.reverse()
    return xChanger(x, y, i + 1, False)

def intReturner(x):
    x = list(reversed(x))
    x = [str(i) for i in x]
    x = ''.join(x)
    return int(x)

def xChanger(x, y, i, switcher):
    answ = cardNumb(x)
    if  answ % 10 == 0:
        return intReturner(x)
    elif switcher:
        return adder(x, i, switcher)
    else:
        return changeArr(y, i)

def start(x, switcher, ind):
    x = [int(i) for i in x]
    x = list(reversed(x))
    y = x[:]
    if switcher:
        return adder(x, ind, switcher)
    else:
        return xChanger(x, y, 0, False)

def adder(x, i, switcher):
    x.reverse()
    x[i] += 1
    if x[i] == 10:
        x[i] = 0
        x.reverse()
        return xChanger(x, x[:], 0, False)
    else:
        x.reverse()
        return xChanger(x, x[:], i, switcher)

def checkIsIt(x):
    x = list(x)
    i = 0
    switcher = False
    if '?' in x:
        i = x.index('?')
        x[i] = 0
        switcher = True
    return start(x, switcher, i)

ans = []
for i in range(int(input())):
    ans.append(checkIsIt(input()))
print(*ans)
