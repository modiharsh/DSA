# https://leetcode.com/problems/delete-characters-to-make-fancy-string #Easy #Strings

class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[:2]
        for c in s[2:]:
            if c == res[-1] and c == res[-2]:
                continue
            else:
                res += c
        
        return res

# Example 1:

# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".
# Example 2:

# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".
# Example 3:

# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".
