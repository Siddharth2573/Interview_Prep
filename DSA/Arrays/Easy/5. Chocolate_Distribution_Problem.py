nums = {7, 3, 2, 4, 9, 12, 56}
m = 5
nums_sorted = sorted(nums)
lowest_m = nums_sorted[:m]
print(max(lowest_m) - min(lowest_m))

# Intution: Sort and pick 1st m element and subtract max with min among that sorted element
# Output: 7 --> (9-2)
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# https://www.geeksforgeeks.org/dsa/chocolate-distribution-problem/
