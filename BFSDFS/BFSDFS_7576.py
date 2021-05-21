def tomato():
    from sys import stdin
    from collections import deque

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    stack = deque()
    farm = []
    flag_0 = True
    M, N = map(int, stdin.readline().split())

    for i in range(N):
        temp = stdin.readline().split()
        farm.append(temp)
        for j in range(M):
            if temp[j] == '0':
                flag_0 = False
            if temp[j] == '1':
                stack.append((i,j))

    if flag_0: return 0

    visit = [[0]*M for _ in range(N)]
    for y, x in stack:
        visit[y][x] = 1

    while(stack):
        y, x = stack.popleft()
        farm[y][x] = "1"
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if 0<=new_y<N and 0<=new_x<M:
                if farm[new_y][new_x] == "0" and visit[new_y][new_x] == 0:
                    stack.append((new_y, new_x))
                    visit[new_y][new_x] = visit[y][x] + 1

    for line in farm:
        for tom in line:
            if tom == "0":
                return -1

    return visit[y][x]-1

if __name__ == "__main__":
    print(tomato())