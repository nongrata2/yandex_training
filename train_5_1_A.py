# https://contest.yandex.ru/contest/59539/problems/A/ - task link

[p, v] = [int(x) for x in input().split()]
[q, m] = [int(x) for x in input().split()]

granmin2 = p - v
granmax2 = p + v
granmin1 = q - m
granmax1 = q + m

num = v * 2 + m * 2 + 1

if p != q:
    num += 1

if (granmin1 >= granmin2 and granmax1 <= granmax2) or (granmin2 >= granmin1 and granmax2 <= granmax1):
    if granmax1 - granmin1 < granmax2 - granmin2:
        num = v * 2 + 1
    else:
        num = m * 2 + 1
elif granmax1 >= granmin2 and granmax1 <= granmax2:
    num -= granmax1 - granmin2 + 1
elif granmax2 >= granmin1 and granmax2 <= granmax1:
    num -= granmax2 - granmin1 + 1

print(num)
