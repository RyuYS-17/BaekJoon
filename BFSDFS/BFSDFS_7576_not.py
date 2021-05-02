def solution(M, N):
    from collections import deque

    tomato_farm = [input().split() for _ in range(N)]
    
    flag_ripen = True
    count = 0

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    queue = deque()
    
    for i in range(N):
        for j in range(M):
            tomato = tomato_farm[i][j]
            if tomato == "0": flag_ripen = False
            if tomato == "1": queue.append((i,j,0))

    # 0이 존재하지 않아 모두 익어 있는 경우
    if flag_ripen: return 0
    
    while(queue):
        y,x,day = queue.popleft()
        count = day
        if tomato_farm[y][x] == "0":
            tomato_farm[y][x] = "1"
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if 0<=new_y<N and 0<=new_x<M and tomato_farm[new_y][new_x] == "0":
                queue.append((new_y,new_x,(day+1)))

    for line in tomato_farm:
        if "0" in line: return -1

    return count


if __name__ == "__main__":
    M, N = map(int, input().split())
    print(solution(M, N))
