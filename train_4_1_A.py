#https://contest.yandex.ru/contest/53027/problems/A/ - task link

n, m = [int(i) for i in input().split(' ')]
arr = [int(i) for i in input().split()[:n]]


for i in range(m):
    a, b = [int(x) for x in input().split(' ')]
    currmin = arr[a]
    flag = 0
    for j in range(a + 1, b + 1):
        if arr[j] > currmin and flag == 0:
            print(arr[j])
            flag = 1
        if arr[j] < currmin and flag == 0:
            print(currmin)
            flag = 1
        if j == b and flag == 0:
            print('NOT FOUND')
