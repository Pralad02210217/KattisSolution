a,b=map(int,input().split())

if a+b==0:
    print("Not a moose")
elif a ==b :
    print("Even",a+b)
else :
    age=max(a,b)*2
    print("Odd", age)