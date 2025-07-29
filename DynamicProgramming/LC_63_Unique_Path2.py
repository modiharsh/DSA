# https://leetcode.com/problems/unique-paths-ii #Medium #Array #DynamicProgrmaming #Matrix

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # Method 1 : Use 2D space O(m.n)
        dp = [[float(inf)] * n for _ in range(m)]

        
        for i in range(m):
            for j in range(n):
                # if obstacleGrid[i][j] == 1:
                #     dp[i][j] == 0

                if i==0 and j==0:
                    dp[i][j] = 1 if obstacleGrid[i][j] == 0 else 0
                elif i == 0:
                    dp[i][j] = dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
                elif j == 0:

                    dp[i][j] = dp[i-1][j] if obstacleGrid[i][j] == 0 else 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
        
        return dp[m-1][n-1]


# Example 1:
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
