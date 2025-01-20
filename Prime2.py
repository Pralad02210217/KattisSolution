from fractions import Fraction
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


n=int(input())

for i in range(n):
    number=input()
    bases=[2,8,10,16]
    numerator=0
    denominator=0
    
    for base in bases:
        try:
            checkNumber=int(number,base)
            denominator+=1
            if is_prime(checkNumber):
                numerator+=1
        except ValueError:
            pass
    f = Fraction(numerator, denominator)
    if (f == Fraction(0)):
      print("0/1")
    elif (f == Fraction(1)):
      print("1/1")
    else:
      print(f)