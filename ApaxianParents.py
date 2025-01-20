FirstName, parentName = input().split()
vowels = ["a", "e", "i", "o", "u"]
word="ex"

if FirstName[-1] == 'x' and FirstName[-2] =='e':
    FirstName += parentName
    print(FirstName)
elif FirstName[-1] not in vowels:
    FirstName += word + parentName
    print(FirstName)
elif FirstName[-1] in vowels:
    FirstName=FirstName[:-1]+word+parentName
    print(FirstName)

