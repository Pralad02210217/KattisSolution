rooms,taken=map(int,input().split())
taken_rooms=set([int(input()) for i in range(taken)])

if rooms==taken:
    print("too late")
else:
    for i in range(1,rooms+1):
        if i not in taken_rooms:
            print(i)
            break