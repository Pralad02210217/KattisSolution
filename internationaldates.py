
dates=list(map(int, input().split("/")))

if dates[0] >= 12 and dates[1] < 12 :
    print("US")
elif dates[0] <=12 and dates[1] > 12:
    print("EU")
else :
    print("either")
    