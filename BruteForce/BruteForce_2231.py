N = int(input())

minimum = 1
maximum = 1000000
flag=True

for i in range(minimum, maximum+1):
    N_copy = N
    temp = []
    number = i
    while(number):
        temp.append(number%10)
        number = number//10
    for num in temp:
        N_copy -= num
    if N_copy == i:
        print(N_copy)
        flag=False
        break

if flag:
    print(0)