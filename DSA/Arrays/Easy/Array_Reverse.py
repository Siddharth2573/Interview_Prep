nums = [3, 5, 4, 1, 9]
print(nums[::-1])

# Time Complexity: O(n)
# Space Complexity: O(n)
# Best for: Quick, readable one-liners where a new list is needed.

# ---------------------

nums = [3, 5, 4, 1, 9]
nums.reverse()
print(nums)

# Time Complexity: O(n)
# Space Complexity: O(1)
# Best for: Memory-critical tasks where the original list can be modified.

# --------------------

nums = [3, 5, 4, 1, 9]
for num in reversed(nums):
  print(num)

# Time Complexity: O(n)
# Space Complexity: O(1)
# Best for: Large datasets where you only need to iterate, not store.

# https://www.geeksforgeeks.org/dsa/program-to-reverse-an-array/

