def checkValidity(numbers):
    for i in range(len(numbers)-1):
        if numbers[i+1].startswith(numbers[i]):
            return("NO")
    return "YES"
        


n = int(input())

for _ in range(n):
    testCase = int(input())
    numbers = [input() for i in range(testCase)]
    numbers.sort()
    result = checkValidity(numbers)
    
    print(result)
   
        
        