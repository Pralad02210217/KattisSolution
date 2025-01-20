n=int(input())
junks=list(map(int,input().split()))
minimumJunk=min(junks)
print(junks.index(minimumJunk))