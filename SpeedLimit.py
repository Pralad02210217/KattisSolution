while True:
    n=int(input())
    
    if n== -1:
        break
    
    distanceTravelled=0
    prevTime=0
    
    for i in range(n):
        a,b=map(int,input().split())
        elapsedtime= b-prevTime
        distanceTravelled+= a* elapsedtime
        prevTime=b
    print(distanceTravelled, "miles")