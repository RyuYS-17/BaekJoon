def solution(N, money):
    list_coins = [int(input()) for _ in range(N)]
    count = 0

    for coin in list_coins[::-1]:
        if money == 0: break
        if coin <= money:
            num_coin = money//coin
            money = money%coin
            count += num_coin
    return count

if __name__ == "__main__":
    N, money = map(int, input().split())
    print(solution(N, money))
