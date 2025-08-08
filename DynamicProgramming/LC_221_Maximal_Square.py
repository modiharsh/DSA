# https://leetcode.com/problems/maximal-square #Medium #Array #DynamicProgramming #Matrix

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_side = 0

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side



# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:
# Input: matrix = [["0"]]
# Output: 0
