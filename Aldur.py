n = int(input())
min = -1
for i in range(n):
    age = int(input())
    if min == -1:
        min = age
    if age < min:
        min = age
print(min)
    