import math
wallHeight,angle=map(int,input().split())

angleInRadiant= math.radians(angle)
print(angleInRadiant)

LengthOfLadder= math.ceil(wallHeight/ math.sin(angleInRadiant))
print(LengthOfLadder)

#length of ladder can be found using Sin as sin is Opposite(Wall)/ Hypothenus(the ladder).
#Since computers cannot directly calculate using degree first conver to radian