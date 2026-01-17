nums = [1, 2, 3, 1]
visited = set()
has_duplicate = False  # Flag to track the result

for num in nums:
    if num in visited:
        has_duplicate = True
        break  # Exit loop immediately when first duplicate is found
    else:
        visited.add(num)

print(has_duplicate)

# Output: True
# Time Complexity: O(n)
# Space Complexity: O(n)
# https://leetcode.com/problems/contains-duplicate/
# https://neetcode.io/solutions/contains-duplicate

# ----------------------------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return True
            else:
                visited.add(nums[i])
        return False
