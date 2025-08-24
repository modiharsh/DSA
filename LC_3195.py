# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i #Medium #Matrix #Array

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row_set = set()
        column_set = set()

        m = len(grid)
        n = len(grid[0])

        min_row, max_row = m, -1
        min_col, max_col = n, -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)
        if max_row == -1:
            return 0

        return (max_row - min_row + 1) * (max_col - min_col + 1)

  You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.

 

# Example 1:
# Input: grid = [[0,1,0],[1,0,1]]
# Output: 6
# Explanation:
# The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

# Example 2:
# Input: grid = [[1,0],[0,0]]
# Output: 1
# Explanation:
# The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.
