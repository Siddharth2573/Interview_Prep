nums = [2,3,-2,4]
n=len(nums)
max_prod=nums[0]
prefix=suffix=0

for i in range(n):
    prefix = (prefix or 1) * nums[i]
    suffix = (suffix or 1) * nums[n-1-i]
    max_prod = max(max_prod,prefix,suffix)
print(max_prod)

# Output: 6
# Time Complexity: O(n)
# Space Complexity: O(1)

# https://leetcode.com/problems/maximum-product-subarray/
# https://neetcode.io/solutions/maximum-product-subarray
