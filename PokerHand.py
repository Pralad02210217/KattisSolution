cards=input().split()
rank_count={}

for card in cards:
    rank=card[0]
    if rank in rank_count:
        rank_count[rank]+=1
        print(rank_count)
    else:
        rank_count[rank]=1
print(max(rank_count.values()))