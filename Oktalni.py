n = input()
zerosNeeded = len(n) % 3
newN = ""
if zerosNeeded == 2:
    newN = "00" + n
elif zerosNeeded == 1:
    newN = "0"+ n
else:
    newN = n
number = int(newN, 2)
octoNumber = oct(number)[2:]
print(octoNumber)