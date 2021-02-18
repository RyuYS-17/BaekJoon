def solution():
    total = 0
    _ = int(input())
    distances = [int(x) for x in input().split()]
    prices = [int(x) for x in input().split()]
    prices = prices[:-1]

    minPrice = min(prices)
    location_minimum = prices.index(minPrice)
    
    if location_minimum == 0:
        return sum(distances)*minPrice
    
    current_oilPrice = prices[0]
    idx = 0
    for _ in range(location_minimum):
        if current_oilPrice > prices[idx]:
            current_oilPrice = prices[idx]
        total += current_oilPrice*distances[idx]
        idx += 1

    total += sum(distances[idx:])*minPrice    
    return total

if __name__ == "__main__":
    print(solution())