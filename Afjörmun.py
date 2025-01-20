n = int(input())

for i in range(n):
    word = input()
    firstWord = word[0]
    remainingWord = word[1:]
    print("".join([firstWord.upper(), remainingWord.lower()]))