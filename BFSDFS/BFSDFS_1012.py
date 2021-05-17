def countWorm():
    count = 0
    M, N, K = map(int, input().split())
    farm = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x,y = map(int, input().split())
        farm[y][x] = 1
    
    def dfs(i, j):
        stack = [(i, j)]
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        while(stack):
            y, x = stack.pop()
            farm[y][x] = -1
            for l in range(4):
                new_y = y + dy[l]
                new_x = x + dx[l]
                if 0<=new_y<N and 0<=new_x<M and farm[new_y][new_x] == 1:
                    stack.append((new_y, new_x))
    
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                dfs(i, j)
                count += 1
            elif farm[i][j] == 0:
                farm[i][j] = -1
    print(count)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        countWorm()