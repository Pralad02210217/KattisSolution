def findLastDigitFactorial(number):
    factorial=1
    if number==0:
        return number
    for i in range(1,number+1):
        factorial*=i
        
    if factorial < 10:
        return factorial
    
    LastDigit=str(factorial)
    return int(LastDigit[-1])
        

n=int(input())
for i in range(n):
    a=int(input())
    print(findLastDigitFactorial(a))