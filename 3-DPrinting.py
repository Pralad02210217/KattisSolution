import math

x=int(input())
print(math.ceil(math.log(x,2))+1)

print(math.log(x,2))
# count number times the the productivity has to be double to reach the x numbeer of statues
# Here we are trying to find the log x with base 2 to see to what power of 2 it is
# if numStatues is 8, then numDays will be 3 because 2^3 = 8.