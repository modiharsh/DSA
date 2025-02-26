class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindrome
        if x < 0:
            return False

        # Single digits are palindrome
        if x < 10:
            return True

        if x % 10 == 0 and x != 0:
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10
        
if __name__ == '__main__':
    solution = Solution()
    test_cases = [121, -121, 10, 12321, 123321, 0, 1]
    for num in test_cases:
        print(solution.isPalindrome(num))