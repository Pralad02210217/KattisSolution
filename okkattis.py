
while True:
    Numerator,Denominator=map(int,input().split())
    
    if (Numerator and Denominator) == 0:
        break
    whole_fraction= Numerator // Denominator
    remainder= Numerator%Denominator
    print(f"{whole_fraction} {remainder} / {Denominator}")
    
    
