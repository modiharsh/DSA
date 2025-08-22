# https://leetcode.com/problems/maximum-69-number #Easy #Math #Greedy

class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = list(str(num))
        for i in range(len(num_str)):
            if num_str[i] == '6':
                num_str[i] = '9'
                break
        return int(''.join(num_str))




# Example 1:

# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
# Example 2:

# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# Example 3:

# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
