n = int(input())
Days = sorted(map(int, input().split()), reverse=True)

max_day = 0
for i, day in enumerate(Days, start=1):  
    max_day = max(max_day, i + day)  

print(max_day + 1)  
