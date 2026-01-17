nums = [1,2,3,4]
n=len(nums)
res = [1] * n

prefix = 1

for i in range(n):
    res[i] = prefix
    prefix *= nums[i]

suffix = 1

for i in range(n-1,-1,-1):
    res[i] *= suffix
    suffix *= nums[i]
    
print(res)

# Output: [24, 12, 8, 6]
# Time Complexity: O(n)
# Space Complexity: O(n)

# https://leetcode.com/problems/product-of-array-except-self/
# https://neetcode.io/solutions/product-of-array-except-self
