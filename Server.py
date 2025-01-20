task,time=map(int,input().split())
taskTime=list(map(int,input().split()))
count=0
CurrentTime=0

for t in taskTime:
    if CurrentTime+t <=time:
        CurrentTime+=t
        count+=1
    else:
        break
print(count)
    