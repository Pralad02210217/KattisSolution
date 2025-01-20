def properSum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum



n=int(input())
for i in range(n):
    k,n1=map(int,input().split())
    firstSum=properSum(n1)
    secondSum= n1**2
    thirdSum=secondSum+n1
    print(f"{k} {firstSum} {secondSum} {thirdSum}")