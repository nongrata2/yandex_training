# https://contest.yandex.ru/contest/53027/problems/D/ - task link

word1 = input()
word2 = input()

set1 = set(word1)
set2 = set(word2)

flag = 0
for letter in set1:
    count1 = word1.count(letter)
    count2 = word2.count(letter)
    if count1 != count2 and flag == 0:
        flag = 1

if flag == 1:
    print('NO')
else:
    print('YES')
