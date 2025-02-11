import sys


words = []
for line in sys.stdin:
    words.append(len(line.strip()))
max_length = max(words)
penalty = 0
for length in words[:-1]:
    penalty += (max_length - length) ** 2
print(penalty)
