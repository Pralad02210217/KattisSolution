e,f,cost=list(map(int,input().split()))
empty_soda=e+f
soda_drank=0

while True:
    soda_bought=empty_soda // cost
    empty_soda%=cost
    
    soda_drank+=soda_bought
    empty_soda+=soda_bought
    
    if empty_soda < cost:
        break
print(soda_drank)
