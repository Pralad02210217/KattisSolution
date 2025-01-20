

def checkDifference(sequence):
    currentDif=sequence[1]-sequence[0]
    for i in range(len(sequence)-1):
        if (sequence[i+1] - sequence[i])!= currentDif:
            return False   
    return True
    
        
n=int(input())
for i in range(n):
    sequence= list(map(int,input().split()))
    newSequence=sequence[1:]
    if checkDifference(newSequence):
        print("arithmetic")
    else :
        if checkDifference(sorted(newSequence)):
            print("permuted arithmetic")
        else:
            print("non-arithmetic")


    
    


        