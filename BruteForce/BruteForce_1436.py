N = int(input())
n = 0; number = 0

while(True):
    number += 1
    if '666' in str(number):
        n += 1
    if n == N:
        print(number)
        break