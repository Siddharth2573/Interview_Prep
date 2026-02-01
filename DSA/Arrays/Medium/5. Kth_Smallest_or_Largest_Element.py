# We can use sort the array then pick the required index.
# Another approach is using heap (This is a tree structure which have smallest value at top

import heapq

# Function to find the K'th largest element
def kth_largest(arr, K):
  
    # Min heap to store K largest elements
    pq = []

    # Iterate through the array elements
    for val in arr:
      
        # Add current element to the min heap
        heapq.heappush(pq, val)
        
        # If heap exceeds size K, remove smallest element
        if len(pq) > K:
            heapq.heappop(pq)

    # Top of the heap is the K'th largest element
    return pq[0]

arr = [12, 3, 5, 7, 19]
K = 2
print(kth_largest(arr, K))

# --------------------------------------------------------------

import heapq

# Function to find the K'th largest element
def kth_smallest(arr, K):
  
    # Min heap to store K largest elements
    pq = []

    # Iterate through the array elements
    for val in arr:
      
        # Add current element to the min heap
        heapq.heappush(pq, -val)
        
        # If heap exceeds size K, remove smallest element
        if len(pq) > K:
            heapq.heappop(pq)

    # Top of the heap is the K'th largest element
    return pq[0]

arr = [12, 3, 5, 7, 19]
K = 2
print(kth_smallest(arr, K))

# ----------------------------------------------------------

# Only different is the negative sign (-val) which ensures that the largest numbers have the "smallest" value in the heap, so they stay at the top to be popped.
# And Since you stored the values as negatives, you must use -pq[0] to get the original positive number back.

# Time Complexity: O(n * log(k))
# Space Complexity: O(k)

# https://neetcode.io/solutions/kth-largest-element-in-an-array
# https://www.geeksforgeeks.org/dsa/kth-smallest-largest-element-in-unsorted-array/
