# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        power = 0
        value = 0
        zero_count = s.count('0')
        for digit in reversed(s):
            if digit == '1':
                if power < 32 and value + (1 << power) <= k:
                    value += (1 << power)
                    count += 1
                else:
                    continue
            else:
                power += 1
                continue
            power += 1
        return count + zero_count


# Example 1:

# Input: s = "1001010", k = 5
# Output: 5
# Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
# Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
# The length of this subsequence is 5, so 5 is returned.
# Example 2:

# Input: s = "00101001", k = 1
# Output: 6
# Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
# The length of this subsequence is 6, so 6 is returned.
