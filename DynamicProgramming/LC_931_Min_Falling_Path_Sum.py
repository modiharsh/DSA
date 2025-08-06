# https://leetcode.com/problems/minimum-falling-path-sum #Medium #DynamicProgramming #Matrix #Array


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Method 1: with O(n2) space

        # n = len(matrix)
        # dp = [row[:] for row in matrix]
        
        # # Build DP table from second row onward
        # for i in range(1, n):
        #     for j in range(n):
        #         down = dp[i - 1][j]
        #         left = dp[i - 1][j - 1] if j > 0 else float('inf')
        #         right = dp[i - 1][j + 1] if j < n - 1 else float('inf')      
        #         dp[i][j] += min(down, left, right)

        # return min(dp[-1])
                
        # Method 2 : with O(n) space

        n = len(matrix)
        prev = matrix[0][:]

        for i in range(1, n):
            curr = [0] * n
            for j in range(n):
                down = prev[j]
                left = prev[j-1] if j > 0 else float('inf')
                right = prev[j+1] if j < n-1 else float('inf')
                curr[j] = min(down, left, right) + matrix[i][j]
            prev = curr
    
        return min(prev)




# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

# Example 1:
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# Example 2:
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
