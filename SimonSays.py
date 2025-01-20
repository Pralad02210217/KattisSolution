n=int(input())
for i in range(n):
    word=input()
    word2="Simon says"
    
    if word2 in word :
        word=word.replace(word2,"").strip()
        print(word)
    