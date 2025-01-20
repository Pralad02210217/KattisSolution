n=int(input())
busNumbers=sorted(list(map(int,input().split())))
short_representation=[]

i=0
while i<len(busNumbers):
    start=busNumbers[i]
    end=busNumbers[i]
    
    while i < n-1 and busNumbers[i]+1 == busNumbers[i+1]:
        i+=1
        end=busNumbers[i]
    if start == end:
        short_representation.append(str(start))
    elif end-start==1:
        short_representation.append(str(start))
        short_representation.append(str(end))
    else:
        short_representation.append(f"{start}-{end}")
    i+=1
print(*short_representation)
    