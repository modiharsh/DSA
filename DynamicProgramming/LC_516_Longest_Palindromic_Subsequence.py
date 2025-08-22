# https://leetcode.com/problems/longest-palindromic-subsequence #Medium #DynamicProgramming

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        rev_s = s[::-1]
        dp = [[0] * (n+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == rev_s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][n]

# Example 1:
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".

# Example 2:
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
