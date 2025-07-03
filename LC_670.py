# https://leetcode.com/problems/maximum-swap/

class Solution:
    def maximumSwap(self, num: int) -> int:
        # My solution : O(n2)
        # if num < 10:
        #     return num
        # str_num = str(num)
        # i = 0
        # n = len(str_num)
        
        # while i < n -1:
        #     max_than_curr = -1
        #     left_side_to_be_swapped = int(str_num[i])
        #     right_side_swap_index = -1
        #     for j in range(i+1, n):
        #         if int(str_num[j]) > left_side_to_be_swapped and int(str_num[j]) >= max_than_curr:
        #             right_side_swap_index = j
        #             max_than_curr = int(str_num[j])
        #     if right_side_swap_index != -1:
        #         print(i, right_side_swap_index)
        #         return int(str_num[:i] + str_num[right_side_swap_index] + str_num[i+1:right_side_swap_index] + str_num[i] + str_num[right_side_swap_index+1:])
        #     i += 1
        
        # return num
        
        # Optimized O(n) solution
            
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}
        
        for i, d in enumerate(digits):
            for bigger in range(9, int(d), -1):
                if last.get(bigger, -1) > i:
                    j = last[bigger]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))
        
        return num


# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.
