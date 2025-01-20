n=int(input())
first=input()
second=input()
success=True

if n%2==0:
    success= first==second
else:
    for i in range(len(first)):
        if first[i]==second[i]:
            success=False
if success:
    print("Deletion succeeded")
else:
    print("Deletion failed")

