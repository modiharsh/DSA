# https://leetcode.com/problems/house-robber #Medium #Array #DynamicProgramming

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Method 1: with time complexity
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        # return dp[n-1]

        # Method 2: without time complexity
        # n = len(nums)
        # if n == 1:
        #     return nums[0]

        # prev1 = max(nums[0], nums[1])
        # prev2 = nums[0]

        # for i in range(2, n):
        #     curr = max(prev1, prev2 + nums[i])
        #     prev1, prev2 = curr, prev1
        
        # return prev1



# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
