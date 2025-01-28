height, width, bircksLength = map(int, input().split())
bricks = list(map(int, input().split()))
totalBricks  = height * width
if totalBricks <= sum(bricks):
    print("YES")
else:
    print('No')


