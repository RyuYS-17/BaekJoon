N = int(input())

wordList = set()

for _ in range(N):
    wordList.add(input())
for word in sorted(wordList, key = lambda x: (len(x), x)):
    print(word)