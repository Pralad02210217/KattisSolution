
word=list(set(input()))
guess=input()
mistake=0

for letter in guess:
    if letter in word:
        word.remove(letter)
        
        if len(word)==0:
            print("WIN")
            break
    else:
        mistake+=1
        
        if mistake==10:
            print("Lose")
            break