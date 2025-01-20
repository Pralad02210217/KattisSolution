import math

while True:
    radius,markSquare,markCircle=map(float,input().split())
    if radius == 0:
        break
    areaOfCircle=math.pi*(radius**2)
    estimatedArea=(2*radius)*(2*radius) * (markCircle/markSquare)
    print(f"{areaOfCircle} {estimatedArea}")
