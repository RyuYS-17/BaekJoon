def solution():
    from sys import stdin
    
    N = int(stdin.readline())
    timetable = [tuple(map(int, stdin.readline().split())) for _ in range(N)]
    timetable.sort(key= lambda x: (x[1], x[0]))

    count = 1
    pivot = timetable[0][1]
    ㅁ
    
    for x in timetable[1:]:
        if x[0] >= pivot:
            pivot = x[1]
            count += 1
            
    return count

if __name__ == "__main__":
    print(solution())
