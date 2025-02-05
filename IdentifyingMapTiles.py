n = input()
x = 0
y = 0
for i in range(len(n)):
    currentIndex = int(n[i])
    if currentIndex == 1 or currentIndex == 3:
        x+= pow(2, len(n) - i - 1)
    if currentIndex == 2 or currentIndex == 3:
        y+= pow(2, len(n)- i - 1)
print(f"{len(n)} {x} {y}")