def fill_networks(networks, M):
    for _ in range(M):
        A, B = map(int, input().split())
        networks[(A-1)].add(B)
        networks[(B-1)].add(A)

def virus():
    from collections import deque
    N = int(input())
    M = int(input())

    networks = [set() for _ in range(N)]
    fill_networks(networks, M)
    
    node_start = 1
    queue = deque()
    infested = list()
    queue.append(node_start)
    
    while(queue):
        computer = queue.popleft()
        if computer not in infested:
            infested.append(computer)
            for link in networks[(computer-1)]:
                queue.append(link)
    return len(infested)-1

if __name__ == "__main__":
    print(virus())
