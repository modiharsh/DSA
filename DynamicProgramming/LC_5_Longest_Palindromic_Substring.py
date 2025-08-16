# https://leetcode.com/problems/longest-palindromic-substring #Medium #DynamicProgramming #TwoPointers

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Method 1 : Expand around center
        # def expand_around_center(left, right):
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     return s[left+1:right]

        # longest = ""
        # for i in range(len(s)):
        #     p1 = expand_around_center(i, i)
        #     p2 = expand_around_center(i, i+1)

        #     if len(p1) > len(longest):
        #         longest = p1
        #     if len(p2) > len(longest):
        #         longest = p2

        # return longest

        # Method 2 : Dynamic Programming
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        start = 0
        max_len = 1
        
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2
        
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start = i
                    max_len = length
        
        return s[start:start+max_len]

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"

