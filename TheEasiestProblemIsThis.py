
def sum_of_digit(n):
    sum=0
    for digit in str(n):
        sum+=int(digit)
    return sum


def sameSum(n):
    currentNumber=11
    while True:
        product= n* currentNumber
        if sum_of_digit(product)== sum_of_digit(n):
            return currentNumber
        currentNumber+=1





while True:
    n=int(input())
    if n==0:
        break
    result=sameSum(n)
    print(result)