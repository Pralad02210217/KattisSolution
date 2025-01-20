currentLine=input()
modifiedLine=[]

for letter in currentLine:
    if letter == "<":
        if modifiedLine:
            modifiedLine.pop()
    else:
        modifiedLine.append(letter)
result=''.join(modifiedLine)
print(result)