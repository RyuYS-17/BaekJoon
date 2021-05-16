N, M, start = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

for x,y in edges: matrix[x][y] = matrix[y][x] = 1
visit = [0 for _ in range(N+1)]

def dfs(start):
    stack = [start]
    print(start, end=' ')
    visit[start] = 1
    for idx in range(1,N+1):
        if visit[idx] == 0 and matrix[start][idx] == 1:
            dfs(idx)

def bfs(start):
    queue = [start]
    while (queue):
       node = queue.pop(0)
       if visit[node] == 0:
        print(node, end=' ')
        visit[node] = 1
        for idx in range(1,N+1):
            if visit[idx] == 0 and matrix[node][idx] == 1:
                queue.append(idx)


dfs(start)
print()
visit = [0 for _ in range(N+1)]
bfs(start)