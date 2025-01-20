title,cost=list(map(str,input().split()))
cost=float(cost)

if len(title) < cost:
    print(len(title))
else :
    print(cost)