# https://leetcode.com/problems/n-th-tribonacci-number #Easy #DynamicProgramming

class Solution:
    def __init__(self):
        self.memo = {0:0, 1:1, 2:1}

    def tribonacci(self, n: int) -> int:
        # Method 1 : Tabulation
        # if n <= 1:
        #     return n
        # if n == 2:
        #     return 1

        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 1
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        # return dp[n]

        # Method 2 : memoization
        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.memo[n]

# Example 1:

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:

# Input: n = 25
# Output: 1389537
