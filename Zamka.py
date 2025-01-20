def checkSum(number,c):
    currentSum=0
    checkNumber=str(number)
    for i in checkNumber:
        currentSum+=int(i)
    if currentSum == c:
        return number
    
a=int(input())
b=int(input())
c=int(input())
alist=[]

for i in range(a-1,b+1):
    result=checkSum(i,c)
    if result is not None:
        alist.append(result)
minimum=min(alist)
maximum=max(alist)
print(minimum)
print(maximum)
    
