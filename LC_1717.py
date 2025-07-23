# https://leetcode.com/problems/maximum-score-from-removing-substrings #String #Stack #Greedy

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, first, second, points):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(ch)
            return ''.join(stack), score

        # Prioritize the substring with the higher point
        if x > y:
            s, score1 = remove_substring(s, 'a', 'b', x)  # Remove "ab" first
            _, score2 = remove_substring(s, 'b', 'a', y)  # Then "ba"
        else:
            s, score1 = remove_substring(s, 'b', 'a', y)  # Remove "ba" first
            _, score2 = remove_substring(s, 'a', 'b', x)  # Then "ab"

        return score1 + score2
        

# Example 1:

# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# Example 2:

# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
