# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description

class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        # My Version
        str_num = str(num)
        digit_to_replace = str_num[0]
        for digit in str_num:
            if digit != '9':
                digit_to_replace = digit
                break
        
        max_str_digit = str_num.replace(digit_to_replace, '9')
        min_str_digit = str_num.replace(str_num[0], '0')

        max_digit = int(max_str_digit)
        min_digit = int(min_str_digit)

        return max_digit - min_digit

        # Optimized code version
        # str_num = str(num)

        # # Find first non-'9' digit for max transformation
        # digit_to_replace = next((digit for digit in str_num if digit != '9'), str_num[0])

        # # Generate max and min versions
        # max_num = int(str_num.replace(digit_to_replace, '9'))
        # min_num = int(str_num.replace(str_num[0], '0'))

        # return max_num - min_num


# Example 1:

# Input: num = 11891
# Output: 99009
# Explanation: 
# To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
# To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
# The difference between these two numbers is 99009.
# Example 2:

# Input: num = 90
# Output: 99
# Explanation:
# The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
# Thus, we return 99.
