def solution():
    equation = input()
    temp = ''
    numList = []
    flag_Plus = True
    i = 1
    for spell in equation:
        if spell.isdigit():
            temp += spell
            continue
        if spell == '-':
            flag_Plus = False
        if flag_Plus:
            i += 1
        numList.append(int(temp))
        temp = ''
    numList.append(int(temp))
    total = 0
    for _ in range(i):
        total += numList.pop(0)
    total -= sum(numList)
    
    return total

if __name__ == "__main__":
    print(solution())