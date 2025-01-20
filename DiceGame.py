GunnarList=list(map(int,input().split()))
EmmaList=list(map(int,input().split()))
gunnarSum=sum(GunnarList)
emmaSum=sum(EmmaList)

if gunnarSum > emmaSum:
    print("Gunnar")
elif gunnarSum == emmaSum:
    print("tie")
else:
    print("Emma")