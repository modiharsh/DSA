# https://leetcode.com/problems/largest-3-same-digit-number-in-string #String


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Method 1 - pattern search
        # for i in range(9,-1,-1):
        #     chk = str(i) * 3
        #     if chk in num:
        #         return chk
        
        # return ""

        # Method 2 - sliding window
        max_num = ""

        for i in range(len(num) - 2):
            substr = num[i:i+3]
            if substr[0] == substr[1] == substr[2]:
                if substr > max_num:
                    max_num = substr

        return max_num


# Example 1:
# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".
# Example 2:
# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.
# Example 3:
# Input: num = "42352338"
# Output: ""
# Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
