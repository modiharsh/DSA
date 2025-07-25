# https://leetcode.com/problems/unique-paths #Medium #DynamicProgramming #MatrixDP

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Method 1 : using 2D space O(m.n), time O(m.n)
        # if m == 1 and n == 1:
        #     return 1
        
        # dp = [[1] * n for _ in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # return dp[m-1][n-1]

        # Method 2 : using 1D space O(n), time O(m.n)
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                print(j, dp[j])
                dp[j] += dp[j - 1]
                print(j, dp[j])
        return dp[-1]



# Example 1:

# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
