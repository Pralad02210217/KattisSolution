def binarySearch(sub, num):
    left, right = 0, len(sub)-1
    while left <= right:
        mid = (left + right) //2
        if sub[mid] < num:
            left = mid + 1
        else:
            right = mid -1
    return left

def LIS(nums):
    sub = []
    indices = [-1 for i in range(len(nums))]
    prev_index = [-1 for i in range(len(nums))]
    for i,num in  enumerate(nums):
        pos = binarySearch(sub, num)
        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos]= num
        if pos > 0:
            prev_index[i]= indices[pos -1]
        indices[pos] = i
    lis = []
    idx = indices[len(sub)-1]
    while idx !=-1:
        lis.append(nums[idx])
        idx = prev_index[idx]
    lis.reverse()
    
    print(len(lis), *lis)
        

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    newNums = nums[1:]
    LIS(newNums)