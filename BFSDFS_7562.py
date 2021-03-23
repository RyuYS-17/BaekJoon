def solution():
    from collections import deque
    move_x = [-2,-1,-2,-1,1,2,1,2]
    move_y = [-1,-2,1,2,-2,-1,2,1]
    I = int(input())
    stage = [[0 for _ in range(I)] for _ in range(I)]
    location_x, location_y = map(int, input().split())
    arrival_x, arrival_y = map(int, input().split())
    if (arrival_x == location_x) and (arrival_y == location_y):
        return 0
    queue = deque()
    queue.append((location_x, location_y))
    stage[location_x][location_y] = 1

    while queue:
        location = queue.popleft()
        if location[0]==arrival_x and location[1]==arrival_y:
            return stage[location[0]][location[1]]-1
        for i in range(8):
            new_x = location[0] + move_x[i]
            new_y = location[1] + move_y[i]
            if 0<=new_x<I and 0<=new_y<I:
                if stage[new_x][new_y] == 0:
                    stage[new_x][new_y] = stage[location[0]][location[1]]+1
                    queue.append((new_x, new_y))


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        print(solution())