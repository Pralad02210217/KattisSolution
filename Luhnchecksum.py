def result(numbers):
    sum_odd_digits=0
    sum_even_digits=0
    for x in numbers[::2]:
        sum_odd_digits+=x
    for x in numbers[1::2]:
        x=x*2
        
        if x > 9:
            x=1+(x%10)
            sum_even_digits+=x
        else:
            sum_even_digits+=x
    
    total_sum=sum_even_digits+sum_odd_digits
    if total_sum%10==0:
        return "PASS"
    else:
        return "FAIL"
        

n = int(input())

for i in range(n):
    number = input()
    numbers = [int(num) for num in number]
    numbers=numbers[::-1]
    print(result(numbers))