prices = [7,1,5,3,6,4]
l,r=0,1
max_profit=0
while r<len(prices):
    if prices[l]<prices[r]:
        curr_profit = prices[r] - prices[l]
        max_profit = max(curr_profit,max_profit)
    else:
        l=r
    r=r+1
print(max_profit)

# Output: 5
# Time Compleexity = O(n)
# Space Complexity = O(1)

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# https://neetcode.io/solutions/best-time-to-buy-and-sell-stock
