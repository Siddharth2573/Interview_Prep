nums = [2, 7, 11, 15]
target = 9
visited = {}
found = False  # Flag to track if the target was met

for i in range(len(nums)):
    second = target - nums[i]
    if second in visited:
        print([visited[second], i])
        found = True
        break  # Exit loop immediately after finding the pair
    visited[nums[i]] = i

if not found:
    print(-1)

# Output: [0,1]
# Time Complexity: O(n)
# Space Complexity: O(n)

# https://leetcode.com/problems/two-sum/description/
# https://neetcode.io/solutions/two-sum
