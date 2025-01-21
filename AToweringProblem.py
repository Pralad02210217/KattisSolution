from itertools import combinations
towerHeights = list(map(int, input().split()))
towerHeight1 = towerHeights[-2]
newList = towerHeights[:-2]
result = [list(combo) for combo in combinations(newList, 3) if sum(combo) == towerHeight1]
newResult = [number for number in newList if number not in result[0]]
finalList = sorted(result[0],reverse=True) + sorted(newResult, reverse=True)

print(*finalList)