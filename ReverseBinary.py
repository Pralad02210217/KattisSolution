n=int(input())
binary=bin(n)
binary=binary[2:]
binary=binary[::-1]
print(int(binary,2))
