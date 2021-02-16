def solution():
    N = int(input())

    waitingTime = sorted(list(map(int,input().split())))
    totalTime = 0; i = 0
    for time in waitingTime:
        totalTime += (N-i)*time
        i += 1
    return totalTime

if __name__ == "__main__":
    print(solution())