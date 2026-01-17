class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        curr_sum=0
        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            max_sum = max(max_sum,curr_sum)
        return max_sum

# Kadane's algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

# https://leetcode.com/problems/maximum-subarray/
# https://neetcode.io/solutions/maximum-subarray
