nums = [5,4,-1,7,8]
max_sum=nums[0]
curr_sum=0
for num in nums:
    if curr_sum<0:
        curr_sum=0
    curr_sum+=num
    max_sum = max(curr_sum,max_sum)
print(max_sum)

# Kadane's algorithm
# Output: 23
# Time Complexity: O(n)
# Space Complexity: O(1)

# https://leetcode.com/problems/maximum-subarray/
# https://neetcode.io/solutions/maximum-subarray
