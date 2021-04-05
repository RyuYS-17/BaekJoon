N = int(input())
numList = []
while(N!=0):
    numList.append((N%10))
    N = N//10
numList.sort(key= lambda x: x)
num = 0
for i in range(1,len(numList)):
    num += numList[i]*(10**(i))
print(num+numList[0])
