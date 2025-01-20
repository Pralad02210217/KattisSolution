n= int(input())

for i in range(n):
    types = {}
    total= 1
    m = int(input())
    for j in range(m):
       _, word= input().split(' ')
       if word not in types:
           types[word] = 2
       else:
           types[word]+=1
    for key, value in types.items():
        total*= value
            
    print(total-1)

        
        