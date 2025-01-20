NumberofGuest, chickens=map(int,input().split())
word="pieces"

Need= chickens- NumberofGuest
if abs(Need) == 1:
    word="piece"

if NumberofGuest > chickens:
    Need=abs(Need)
    print(f"Dr. Chaz needs {Need} more {word} of chicken!")
    
else:
    Need= chickens - NumberofGuest
    print(f"Dr. Chaz will have {Need} {word} of chicken left over!")