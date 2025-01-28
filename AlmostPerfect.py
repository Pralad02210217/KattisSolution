def find_divisor_sum(n):
    if n <= 1:
        return 0
    total = 1  
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n + 1): 
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def check_perfect(n):
    divisors = find_divisor_sum(n)
    totalSum = divisors
    if totalSum == n:
        return print(f'{n} perfect')
    if n == totalSum-2 or n == totalSum -1 or n == totalSum+1 or n == totalSum+2:
        return print(f'{n} almost perfect')
    
    return print(f'{n} not perfect')
while True:
    try:
        n = int(input())
        check_perfect(n)
    except EOFError:
        break