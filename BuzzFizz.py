import math

# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Read input values
A, B, X, Y = map(int, input().split())

# Calculate the number of integers divisible by X
N1 = B // X
N2 = (A - 1) // X
count_X = N1 - N2

# Calculate the number of integers divisible by Y
N3 = B // Y
N4 = (A - 1) // Y
count_Y = N3 - N4

# Calculate the least common multiple (LCM) of X and Y
lcm_XY = (X * Y) // gcd(X, Y)

# Calculate the number of integers divisible by both X and Y
N5 = B // lcm_XY
N6 = (A - 1) // lcm_XY
count_XY = N5 - N6

# Output the result
print(count_XY)
