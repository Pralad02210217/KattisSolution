
import math


angle, speed = map(int, input().split())

angle_in_radians = math.radians(angle) 
distance = speed / math.cos(angle_in_radians)

# Check if the distance is less than or equal to 180
if distance <= 180:
    print("Safe")
else:
    min_safe_distance = speed / math.cos(angle_in_radians + math.pi)
    print(int(min_safe_distance))
