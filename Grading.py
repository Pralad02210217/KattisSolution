
grades_limit= list(map(int,input().split()))
score= int(input())

def printGrade(score, grades_limit):
    for i in range(len(grades_limit)):
        if score >= grades_limit[i]:
            return chr(65+i)
    return "F"

grade= printGrade(score,grades_limit)
print(grade)