# https://contest.yandex.ru/contest/53027/problems/B/ - task link

def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def nok(a, b):
    return (a * b) // nod(a, b)


a, b, c, d = [int(i) for i in input().split(' ')]

nodab = nod(a, b)
if nodab != 1:
    a = a//nodab
    b = b//nodab

nodcd = nod(c, d)
if nodcd != 1:
    c = c//nodcd
    d = d//nodcd

currn = nok(b, d)
a *= currn//b
c *= currn//d
summ = a + c

nodsc = nod(summ,currn)

if nodsc != 1:
    summ = summ // nodsc
    currn = currn // nodsc

print(summ, currn)
