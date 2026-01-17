nums = [3,4,5,1,2]
l=0
r=len(nums)-1
res=nums[0]
while l<r:
    if nums[l]<nums[r]:
        res=min(res,nums[l])
        break
    
    mid = (l+r)//2 
    res = min(res,nums[mid])
    
    if nums[mid]>nums[l]:
        l = mid + 1 
    else:
        r = mid - 1
        
print(res)

# Output = 1
# Time Complexity: O(logn)
# Space Complexity: O(n)

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# https://neetcode.io/solutions/find-minimum-in-rotated-sorted-array

