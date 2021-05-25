def solution(X):
    from sys import stdin
    from collections import deque

    N, K = map(int, stdin.readline().split())
    visit = [0]*X
    queue = deque([N])
    visit[N] = 1

    while (queue):
        location = queue.popleft()
        if location == K: break
        if (location+1)<X and visit[location+1] == 0:
            queue.append((location+1))
            visit[location+1] = visit[location]+1
        if (location-1)<X and visit[location-1] == 0:
            queue.append((location-1))
            visit[location-1] = visit[location]+1
        if (location*2)<X and visit[location*2] == 0:
            queue.append((location*2))
            visit[location*2] = visit[location]+1
    return visit[location]-1

if __name__ == '__main__':
    X = 100001
    print(solution(X))