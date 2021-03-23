def solution(N, M):
    graph = []
    edges = []
    for _ in range(M):
        edges.append(list(map(int, input().split())))
    for i in range(N):
        temp = []
        for edge in edges:
            if (i+1)==edge[0]:
                temp.append(edge[1])
            if (i+1)==edge[1]:
                temp.append(edge[0])
        graph.append(temp)
    
    virus = []
    stack = []
    stack.append(1)
    while stack:
        node = stack.pop(0)
        if node not in virus:
            virus.append(node)
            for link in graph[(node-1)]:
                stack.append(link)
    return len(virus)-1

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    print(solution(N, M))