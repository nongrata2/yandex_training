# https://contest.yandex.ru/contest/53027/problems/E/- task link

n = int(input())

arr = [int(i) for i in input().split()[:n]]
summ = sum(arr)

currn2 = 0
currn = 0
prevsum = 0
for i in range(n):
    if i == 0:
        currn = summ - n * arr[i]
        summ -= arr[i]
        prevsum += arr[i]
    else:
        currn = summ - (n-i)*arr[i] + (arr[i]*i - prevsum)
        summ -= arr[i]
        prevsum += arr[i]
    print(currn, end=' ')
