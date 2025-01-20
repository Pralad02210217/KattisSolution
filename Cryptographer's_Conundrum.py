
chiper_text=input().lower()
target_text="per"* (len(chiper_text)//3)
days=0

for i in range(len(chiper_text)):
    if chiper_text[i]!=target_text[i]:
        days+=1

print(days)