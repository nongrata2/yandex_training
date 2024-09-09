# https://contest.yandex.ru/contest/59539/problems/B/ - task link

[ft_goals1, st_goals1] = [int(x) for x in input().split(':')]
[ft_goals2, st_goals2] = [int(x) for x in input().split(':')]

hon = int(input())
nts = 0

total_scored = ft_goals1 + ft_goals2
total_missed = st_goals1 + st_goals2

if hon == 1: #мы сейчас в гостях
    home_missed = st_goals1
    guest_scored = ft_goals2
else: #мы сейчас дома
    home_missed = st_goals2
    guest_scored = ft_goals1

if total_scored == total_missed:
    if guest_scored > home_missed:
        nts = 0
    else:
        nts = 1

elif total_scored > total_missed:
    nts = 0

else: #пропустили больше чем забили
    if hon == 1: # мы сейчас в гостях
        if home_missed < guest_scored:
            nts = total_missed - total_scored
        elif home_missed >= guest_scored and home_missed - guest_scored >= total_missed - total_scored:
            nts = total_missed - total_scored + 1
        elif home_missed >= guest_scored and home_missed - guest_scored < total_missed - total_scored:
            nts = total_missed - total_scored
    else: # мы сейчас дома
        if home_missed < guest_scored:
            nts = total_missed - total_scored
        elif home_missed >= guest_scored and home_missed-guest_scored > total_missed-total_scored:
            nts = total_missed - total_scored + 1
        elif home_missed >= guest_scored and home_missed-guest_scored <= total_missed-total_scored:
            nts = total_missed - total_scored + 1

print(nts)
