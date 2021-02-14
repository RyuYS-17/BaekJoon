### reference from https://roseline124.github.io/algorithm/2019/04/06/Altorithm-baekjoon-7568.html

N = int(input())

people = []

for _ in range(N):
    w, h = map(int, input().split()) # map 활용법 기억
    people.append((w,h))

for person in people:
    rank = 1
    for comparison in people:
        if person[0] < comparison[0]:
            if person[1] < comparison[1]:
                rank += 1
    print(rank)
