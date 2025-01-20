def checkICPC(studentsScores):
    currentSum=0
    for i in range(len(studentsScores)):
        if i==0:
            currentSum+=studentsScores[i]
        else:
            currentSum+=(studentsScores[i]* (4/5)**i)
    return currentSum/5

def checkLeavingScore(newStudentsScore):
    newList=newStudentsScore.copy()
    sums=0
    for i in range(len(newStudentsScore)):
        currentValue= newList.pop(i)
        sums+=checkICPC(newList)
        newList.insert(i,currentValue)
    return sums/len(newList)
        


n=int(input())
studentsScore=list(int(input()) for i in range(n))
firstResult=checkICPC(studentsScore)
second=checkLeavingScore(studentsScore)
print(firstResult)
print(second)