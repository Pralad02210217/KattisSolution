n=int(input())
for i in range(n):
    a=int(input())
    steps=list(map(int,input().split()))
    min_distance=(max(steps)-min(steps))*2
    print(min_distance)