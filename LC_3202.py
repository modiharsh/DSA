# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii #Medium #Array #DynamicProgramming

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        from collections import defaultdict

        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        max_len = 1

        for i in range(n):
            for j in range(i):
                r = (nums[j] + nums[i]) % k
                dp[i][r] = max(dp[i][r], dp[j][r] + 1, 2)
                max_len = max(max_len, dp[i][r])

        return max_len


# Example 1:
# Input: nums = [1,2,3,4,5], k = 2
# Output: 5
# Explanation:
# The longest valid subsequence is [1, 2, 3, 4, 5].

# Example 2:
# Input: nums = [1,4,2,3,1,4], k = 3
# Output: 4
# Explanation:
# The longest valid subsequence is [1, 4, 1, 4].
