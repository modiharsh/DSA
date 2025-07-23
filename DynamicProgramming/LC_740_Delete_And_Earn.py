# https://leetcode.com/problems/delete-and-earn #Array #DynamicProgramming

from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = Counter(nums)
        max_num = max(nums)

        points = [0] * (max_num + 1)
        for num in count:
            points[num] = num * count[num]

        dp = [0] * (max_num + 1)
        dp[0] = points[0]
        dp[1] = max(points[0], points[1])

        for i in range(2, max_num+1):
            dp[i] = max(dp[i-1], dp[i-2] + points[i])
            
        return dp[max_num]

# Example 1:

# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# Example 2:

# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.

------------------------------------------------------------------------------------------------------------------------------------------------------------
# To solve this, think of it as a dynamic programming twist on the House Robber problem, where choosing one number forces you to avoid its adjacent values (num - 1 and num + 1).

# 💡 Strategy
# Count total points for each number: For example, if nums = [2,2,3,3,3,4], then:

# Total from 2s → 2 × 2 = 4
# Total from 3s → 3 × 3 = 9
# Total from 4s → 4 × 1 = 4

# Sort and apply DP:

# If you take number i, skip i-1
# Transition: dp[i] = max(dp[i-1], dp[i-2] + points[i])
