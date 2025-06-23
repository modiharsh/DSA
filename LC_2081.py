# https://leetcode.com/problems/sum-of-k-mirror-numbers

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        # My initial version - TLE
        # def base_10_to_n(num):
        #     digits = "0123456789"
        #     res = ""
        #     while num > 0:
        #         rem = num % k
        #         res = digits[rem] + res
        #         num = num // k
        #     return res
        
        # def is_palindrome(num):
        #     return str(num) == str(num)[::-1]

        # i = 1
        # res_count = 0
        # res_sum = 0
        # while res_count < n:
        #     if is_palindrome(i) and is_palindrome(base_10_to_n(i)):
        #         print(i)
        #         res_count += 1
        #         res_sum += i
        #     i += 1
        # return res_sum

        def is_palindrome(s):
            return s == s[::-1]

        def to_base_k(n, k):
            digits = []
            while n > 0:
                digits.append(str(n % k))
                n //= k
            return ''.join(reversed(digits))

        def generate_palindromes():
            length = 1
            while True:
                # Generate odd-length palindromes
                for half in range(10**((length - 1) // 2), 10**((length + 1) // 2)):
                    half_str = str(half)
                    if length % 2 == 0:
                        # Even-length
                        yield int(half_str + half_str[::-1])
                    else:
                        # Odd-length
                        yield int(half_str + half_str[-2::-1])
                length += 1

        count = 0
        total = 0
        for num in generate_palindromes():
            if is_palindrome(to_base_k(num, k)):
                total += num
                count += 1
                if count == n:
                    break
        return total

# Example 1:

# Input: k = 2, n = 5
# Output: 25
# Explanation:
# The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
#   base-10    base-2
#     1          1
#     3          11
#     5          101
#     7          111
#     9          1001
# Their sum = 1 + 3 + 5 + 7 + 9 = 25. 
# Example 2:

# Input: k = 3, n = 7
# Output: 499
# Explanation:
# The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
#   base-10    base-3
#     1          1
#     2          2
#     4          11
#     8          22
#     121        11111
#     151        12121
#     212        21212
# Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.
# Example 3:

# Input: k = 7, n = 17
# Output: 20379000
# Explanation: The 17 smallest 7-mirror numbers are:
# 1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596
