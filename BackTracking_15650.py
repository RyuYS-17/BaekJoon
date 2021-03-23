from itertools import combinations
N, M = map(int, input().split())

numList = [(i+1) for i in range(N)]
combi = (list(combinations(numList, M)))

for c in combi:
    for b in c:
        print(b, end= " ")
    print("")