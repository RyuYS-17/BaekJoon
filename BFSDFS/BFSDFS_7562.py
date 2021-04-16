dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

def solution():
    M = int(input())
    chess_field = [[0 for _ in range(M)] for _ in range(M)]
    location_now = list(map(int, input().split()))
    destination = list(map(int, input().split()))

    if location_now == destination: return 0

    stack = []
    stack.append(location_now)
    chess_field[location_now[0]][location_now[1]] = 1
    
    while(stack):
        node = stack.pop(0)
        if node == destination: return chess_field[node[0]][node[1]]-1
        for i in range(8):
            new_x = node[0] + dx[i]
            new_y = node[1] + dy[i]
            if 0<=new_x<M and 0<=new_y<M and chess_field[new_x][new_y] == 0:
                stack.append([new_x, new_y])
                chess_field[new_x][new_y] = (chess_field[node[0]][node[1]])+1

    return chess_field[node[0]][node[1]]-1

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        print(solution())
