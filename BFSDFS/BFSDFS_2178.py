from sys import stdin

N, M = map(int, stdin.readline().split())
maze = [list(stdin.readline()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
visit[0][0] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

stack = [(0,0)]

while (stack):
    y, x = stack.pop(0)
    if y == (N-1) and x == (M-1): break
    
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0<=new_y<N and 0<=new_x<M:
            if visit[new_y][new_x] == 0 and maze[new_y][new_x] == '1':
                stack.append((new_y, new_x))
                visit[new_y][new_x] = visit[y][x] + 1

print(visit[y][x])