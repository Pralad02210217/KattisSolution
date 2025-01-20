first_line = list(map(int, input().split()))
k = first_line[1]

newIntegers = list(map(int, input().split()))

j=k
while j<= len(newIntegers):
    print(newIntegers[j - 1])
    j+=k
