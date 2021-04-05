import heapq
N = int(input())
numList = []
for _ in range(N):
    numList.append(int(input()))
heapq.heapify(numList)
for _ in range(N):
    print(heapq.heappop(numList))
