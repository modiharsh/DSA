# https://leetcode.com/problems/climbing-stairs/description #Easy #DynamicProgramming

class Solution:
    def climbStairs(self, n: int) -> int:
        # Method 1 : with space complexity
        # if n <= 2:
        #     return n

        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]

        # Method 2 : without space complexity
        if n <= 2:
            return n
        
        prev1 = 2
        prev2 = 1

        for _ in range(3, n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return curr
    
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

