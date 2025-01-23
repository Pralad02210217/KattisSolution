n = int(input())
words = input().split()
number = input()

alienNumbers = {word: num for num, word in enumerate(words)}

decodedValue = 0
power = 0
i = len(number)

sorted_words = sorted(alienNumbers.keys(), key=len, reverse=True)

while i > 0:
    for word in sorted_words:
        if i >= len(word) and number[i - len(word):i] == word:
            value = alienNumbers[word]
            decodedValue += value * (n ** power)
            power += 1
            i -= len(word)
            break

print(decodedValue)
