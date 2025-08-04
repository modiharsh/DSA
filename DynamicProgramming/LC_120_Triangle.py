# https://leetcode.com/problems/triangle #Medium #DynamicProgramming #Arrays

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Method 1 : using O(n2) space
        # n = len(triangle)
        # if n == 1:
        #     return triangle[0][0]

        # dp = [[100000] * (x+1)  for x in range(n)]
        # dp[0][0] = triangle[0][0]

        # for i in range(1, n):
        #     for j in range(i+1):
        #         if j == 0:
        #             dp[i][j] = dp[i-1][0] + triangle[i][j]
        #         elif j == i:
        #             dp[i][j] = dp[i-1][-1] + triangle[i][j]
        #         else:
        #             dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            
        # return min(dp[-1])

        # Method 2 : using O(n) space but in-place 
        # n = len(triangle)
        # if n == 1:
        #     return triangle[0][0]

        # for i in range(1, n):
        #     for j in range(i+1):
        #         if j == 0 :
        #             triangle[i][j] += triangle[i-1][0]
        #         elif j == i:
        #             triangle[i][j] += triangle[i-1][-1]
        #         else:
        #             triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])

        # return min(triangle[-1])

        # Method 3 : Bottom up approach with O(n) space only
        n = len(triangle)
        dp = triangle[-1][:]

        for i in range(n-2, -1,-1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

        return dp[0]


# 🧠 How It Works
# Initialization: Start with a copy of the last row since it represents the base cases.
# Update Rule: At each step, we choose the best among the two adjacent values below.
# Compact Space: Reuse a single array to hold intermediate results—very memory efficient!

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10
 

