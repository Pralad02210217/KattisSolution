
n=int(input())
for i in range(n):
    total_guest=int(input())
    arr=list(map(int, input().split()))
    unique_guests=None
    
    for x in arr:
        count= arr.count(x)
        if count==1:
            unique_guests=x
            break
    print(f"Case #{i+1}: {unique_guests}")
    