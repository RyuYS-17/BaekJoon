def solution():
    N, K = map(int, input().split())

    coins = []
    for _ in range(N):
        coins.append(int(input()))
    
    target = K
    total=0; i=0
    
    while target!=0:
        i += 1
        coin = coins[-i]
        if coin > target:
            continue
        total += target//coin
        target = target%coin

    return total

if __name__ == "__main__":
    print(solution())