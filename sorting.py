nums=[12, 34, 2, 56, 90, 33, 89, 120, 20, 25, 191]
nums = sorted(nums)
target = 90
left = 0 
right = len(nums) - 1 
found = False
while left <= right:
    mid = (left + right) // 2 
    if nums[mid] == target:
        found = True
        break 
    elif nums[mid] > target:
        right = mid - 1 
    else:
        left = mid + 1 
if found == True:
    print("Found")
else:
    print("Not found")
 
