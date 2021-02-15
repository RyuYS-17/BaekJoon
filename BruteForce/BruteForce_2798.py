from itertools import combinations

N, M = map(int, input().split())

cardList = list(map(int, input().split()))

maximum = 0
for combi in combinations(cardList, 3):
    total = sum(combi)
    if total <= M:
        if maximum < total:
            maximum = total

print(maximum)