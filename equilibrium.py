nums=list(map(int,input().split()))
n=len(nums)
result=-1
for i in range(n):
    leftSum=0
    for j in range(i+1):
        leftSum+=nums[j]
    rightSum=0
    for j in range(i+1,n):
        rightSum+=nums[j]
    if leftSum==rightSum:
        result=i  
        break 
print(result)
