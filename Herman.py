import math

radius=int(input())

radius_square=radius* radius
normal_area=math.pi*radius_square
taxicom_area=2*radius_square
print(round(normal_area,6))
print(taxicom_area)