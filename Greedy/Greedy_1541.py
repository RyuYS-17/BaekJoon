def solution():
    equation = input()
    numList = []
    flag_Plus = True
    idx_Plus = 0

    temp = ''
    for word in equation:
        if word.isdigit():
            temp += word
            continue
        
        numList.append(int(temp))
        temp = ''

        if word == '-':
            flag_Plus = False
        if flag_Plus:
            idx_Plus += 1
    numList.append(int(temp))

    total = 0
    total += sum(numList[:(idx_Plus+1)])
    total -= sum(numList[idx_Plus+1:])
    
    return total

if __name__ == "__main__":
    print(solution())
