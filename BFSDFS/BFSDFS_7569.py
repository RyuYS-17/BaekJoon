def solution():
    from sys import stdin
    from collections import deque

    M, N, H = map(int, stdin.readline().split())

    dx = [1,-1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]

    flag_ripen = True
    stack = deque()
    visit = [[[0]*M for _ in range(N)] for _ in range(H)]
    farm = [[[0]*M for _ in range(N)] for _ in range(H)]
    for i in range(H):
        for j in range(N):
            temp = stdin.readline().split()
            for k in range(M):
                farm[i][j][k] = temp[k]
                if temp[k] == '0': flag_ripen = False
                elif temp[k] == '1':
                    stack.append((i,j,k))
                    visit[i][j][k] = 1

    if flag_ripen: return 0

    while (stack):
        z,y,x = stack.pop(0)
        for idx in range(6):
            new_z = z + dz[idx]
            new_y = y + dy[idx]
            new_x = x + dx[idx]

            if 0<=new_z<H and 0<=new_y<N and 0<=new_x<M:
                if farm[new_z][new_y][new_x] == '0' and visit[new_z][new_y][new_x] == 0:
                    farm[new_z][new_y][new_x] = '1'
                    visit[new_z][new_y][new_x] = visit[z][y][x] + 1
                    stack.append((new_z, new_y, new_x))
    
    for height in farm:
        for y_axis in height:
            for x_axis in y_axis:
                if x_axis == '0': return -1



    return (visit[z][y][x]-1)

if __name__ == '__main__':
    print(solution())