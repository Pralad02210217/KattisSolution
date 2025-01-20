Dominant={"A":11, "K": 4, "Q": 3, "J": 20,"T" :10,"9":14,"8":0,"7":0}
notDominant={"A":11, "K": 4, "Q": 3, "J": 2,"T" :10,"9":0,"8":0,"7":0}

NumberofHands,suit= input().split()
number=4*(int(NumberofHands))
currentSum=0
for i in range(number):
    a=input()
    if a[-1] == suit:
        currentSum+=Dominant[a[0]]
    else:
        currentSum+=notDominant[a[0]]
print(currentSum)        