import math

def lowestValue(p,a,b,c,d,n):
    prices = [p * (math.sin(a *(t+1)+b )+ math.cos(c* (t+1)+d) + 2) for t in range(n)]
        
    max_price = prices[0]
    max_decline = 0.0
        
    for price in prices:
        max_price = max(max_price, price)
        max_decline = max(max_decline, max_price - price)
    print(round(max_decline, 9))

n = list(map(int, input().split()))
lowestValue(*n)