import re

def checkPangram(currentAlphabets):
    alphabets=[chr(ord('a')+i) for i in range(26)]
    remainingWords=""
    newAlphabets=alphabets.copy()
    
    for i in newAlphabets:
        if i in currentAlphabets:
            alphabets.remove(i)
        else:
            remainingWords+=i
    
            
    return "Pangram" if not remainingWords else f"missing {remainingWords}"


n = int(input())

for i in range(n):
    word = re.sub(r'[^a-z]', '', input().lower())
    currentAlphabets = list(set(word))
    
    result=checkPangram(currentAlphabets)
    print(result)


