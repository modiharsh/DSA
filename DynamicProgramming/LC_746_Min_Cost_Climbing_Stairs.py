# https://leetcode.com/problems/min-cost-climbing-stairs  #Easy #DynamicProgramming

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Method 1 : with space complexity
        # n = len(cost)
    
        # dp = [0] * n
        # dp[0] = cost[0]
        # dp[1] = cost[1]

        # for i in range(2, n):
        #     dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        # return min(dp[n-1], dp[n-2])

        # Method 2 : without space complexity
        n = len(cost)
        first = cost[0]
        second = cost[1]
        for i in range(2, n):
            curr = cost[i] + min(first, second)
            first, second = second, curr

        return min(first, second)


# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
