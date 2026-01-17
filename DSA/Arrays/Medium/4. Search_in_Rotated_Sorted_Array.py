nums = [4,5,6,7,0,1,2]
target = 3
l, r = 0, len(nums) - 1
found_index = -1  # Initialize with -1 (default for not found)

while l <= r:
    m = (l + r) // 2
    if nums[m] == target:
        found_index = m
        break  # Stop searching once the target is found
    
    # Left sorted portion
    if nums[l] <= nums[m]:
        if target > nums[m] or target < nums[l]:
            l = m + 1
        else:
            r = m - 1
    
    # Right sorted portion
    else:
        if target < nums[m] or target > nums[r]:
            r = m - 1
        else:
            l = m + 1

print(found_index)

# Output: -1 (Since target not found)
# Time Complexity: O(logn)
# Space Complexity: O(1)

# https://leetcode.com/problems/search-in-rotated-sorted-array/
# https://neetcode.io/solutions/search-in-rotated-sorted-array
