dx = [-1,1,0,0]
dy = [0,0,1,-1]

def solution(N):
    from collections import deque
    neighbor = [list(map(int, list(input()))) for _ in range(N)]
    visit_map = [[0 for _ in range(N)] for _ in range(N)]

    queue = deque()
    list_village = []
    count = 0

    for k in range(N):
        for l in range(N):
            if neighbor[k][l]:
                queue.append((k, l))
            else:
                visit_map[k][l] = -1

            while (queue):
                y, x = queue.popleft()
                if visit_map[y][x] == 0:

                    for i in range(4):
                        new_y = y + dy[i]
                        new_x = x + dx[i]
                        if 0<=new_y<N and 0<=new_x<N:
                            if neighbor[new_y][new_x] == 1:
                                queue.append((new_y, new_x))

                    if neighbor[y][x] == 1:
                        visit_map[y][x] = 1
                        count += 1

            if count != 0:
                list_village.append(count)
            count = 0

    list_village.sort()
    print(len(list_village))
    for village in list_village:
        print(village)

if __name__ == "__main__":
    N = int(input())
    solution(N)