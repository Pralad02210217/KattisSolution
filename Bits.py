def count_number(number):
    currentMax=0
    number=int(number)
    
    while number > 0:
        binary=bin(number)
        binary=binary[2:]
        counts=binary.count("1")
        
        if counts > currentMax:
            currentMax=counts
        number=number//10
    return currentMax
        
    




n=int(input())
for i in range(n):
    number=input()
    print(count_number(number))
    