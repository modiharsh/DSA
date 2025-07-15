# https://leetcode.com/problems/valid-word   #Easy #Strings

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = set("aeiouAEIOU")
        has_vowel = False
        has_consonant = False

        for c in word:
            if c.isdigit() or c.isalpha():
                if c in vowels:
                    has_vowel = True
                elif c.isalpha():
                    has_consonant = True
            else:
                return False

        return has_vowel and has_consonant

# Example 1:
# Input: word = "234Adas"
# Output: true
# Explanation:
# This word satisfies the conditions.

# Example 2:
# Input: word = "b3"
# Output: false
# Explanation:
# The length of this word is fewer than 3, and does not have a vowel.

# Example 3:
# Input: word = "a3$e"
# Output: false
# Explanation:
# This word contains a '$' character and does not have a consonant.
