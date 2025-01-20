
currentCurrency=list(map(int,input().split()))
propertyPrices={"Province" : 8, "Duchy" : 5, "Estate" : 2}
mineralsPrices={"Gold" : 6, "Silver": 3, "Copper": 0}

currentCurrency[0]=currentCurrency[0]*3
currentCurrency[1]=currentCurrency[1]*2

currentSum=sum(currentCurrency)
buyProperty=""
buyMineral=""
for key,value in propertyPrices.items():
    if currentSum >= value:
        buyProperty= key
        break
for key, value in mineralsPrices.items():
    if currentSum >= value:
        buyMineral=key
        break
if buyProperty !="":
    print(f"{buyProperty} or {buyMineral}")
else :
    print(f"{buyMineral}")
