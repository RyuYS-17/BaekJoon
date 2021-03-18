def make_list(N):
    numList = []
    for _ in range(N):
        numList.append(int(input()))
    return numList

def sorting(numList):
    if len(numList)<2:
        return numList
    middle = len(numList)//2
    pivot = numList[middle]
    lower = []; higher = []
    for num in numList:
        if num < pivot:
            lower.append(num)
        if num > pivot:
            higher.append(num)
    return sorting(lower)+[pivot]+sorting(higher)

if __name__ == "__main__":
    N = int(input())
    numList = make_list(N)
    sort_List = sorting(numList)
    for num in sort_List:
        print(num)