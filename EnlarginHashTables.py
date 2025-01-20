def checkPrime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i+=6
    return True

def main():
    while True:
        n=int(input())
        if n== 0:
            break
        resultWord=""
        if not checkPrime(n):
            resultWord=f"({n} is not prime)"
        
        i=0
        while True:
            number = 2 * n + i
            if checkPrime(number):
                print(f"{number} {resultWord}")
                i=0
                break
            i+=1

if __name__=="__main__":
    main()