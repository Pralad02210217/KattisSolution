from math import gcd
from itertools import permutations

def rearrange_children(n, ages):
    for perm in permutations(ages):
        valid = True
        for i in range(len(perm) - 1):
            if gcd(perm[i], perm[i + 1]) == 1:
                valid = False
                break
        if valid:
            return " ".join(map(str, perm)) 
    return "Neibb"  

n = int(input())
ages = list(map(int, input().split()))

print(rearrange_children(n, ages))
