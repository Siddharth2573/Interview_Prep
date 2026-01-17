nums = [3, 5, 4, 1, 9]
print([min(nums),max(nums)])  

# Output: [1,9]
# Time Complexity: O(n) + O(n) = O(n)
# Space Complexity: O(1)
# --------------------------

# Optimal with single pass

nums = [3, 5, 4, 1, 9]
mi = ma = nums[0]
for num in nums:
    if num > ma:
        ma = num
    if num < mi:
        mi = num
print([mi, ma])

# Output: [1,9]
# Time Complexity: O(n)
# Space Complexity: O(1)

# https://www.geeksforgeeks.org/dsa/maximum-and-minimum-in-an-array/
