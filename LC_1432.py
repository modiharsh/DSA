# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer

class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        # Maximize: replace the first digit ≠ '9' with '9'
        max_int = num
        for ch in num_str:
            if ch != '9':
                max_int = int(num_str.replace(ch, '9'))
                break

        # Minimize
        if num_str[0] != '1':
            min_int = int(num_str.replace(num_str[0], '1'))
        else:
            min_int = num
            for i in range(1, len(num_str)):
                if num_str[i] not in {'0', '1'}:
                    min_int = int(num_str.replace(num_str[i], '0'))
                    break

        return max_int - min_int

      
# Example 1:

# Input: num = 555
# Output: 888
# Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
# The second time pick x = 5 and y = 1 and store the new integer in b.
# We have now a = 999 and b = 111 and max difference = 888
# Example 2:

# Input: num = 9
# Output: 8
# Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
# The second time pick x = 9 and y = 1 and store the new integer in b.
# We have now a = 9 and b = 1 and max difference = 8
