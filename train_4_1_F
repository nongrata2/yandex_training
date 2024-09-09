# https://contest.yandex.ru/contest/53027/problems/F - task link

import math
capacity = int(input())
stages = int(input())
arr = []
time = 0
free_space = capacity
max_curr_floor = -1

for i in range(stages):
    arr.append(int(input()))

for j in range(len(arr)-1, -1, -1):

    if arr[j] >= capacity:
        time += math.floor(arr[j] / capacity) * 2 * (j+1)
        arr[j] -= math.floor(arr[j] / capacity) * capacity
        
    while arr[j] != 0: #while stage is not empty

        if arr[j] <= free_space: #if we can bring all people in one trip
            if max_curr_floor == -1:
                max_curr_floor = j+1
            free_space -= arr[j]
            arr[j] = 0

        elif arr[j] > free_space:
            arr[j] -= free_space
            free_space = 0

        if free_space == 0:
            time += max_curr_floor * 2
            free_space = capacity
            max_curr_floor = -1

if free_space != capacity: # if we are at the end, but have people in elevator
    time += max_curr_floor * 2

print(time)
