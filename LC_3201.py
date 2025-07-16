# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i #Medium #Arrays

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # My original solution
        # odd_seq_len = 0
        # even_seq_len = 0
        # odd_even_seq_len = 0
        # even_odd_seq_len = 0

        # even_seq_len = len([n for n in nums if n%2 ==0])
        # odd_seq_len = len([n for n in nums if n%2 !=0])
        # for n in nums:
        #     if odd_even_seq_len % 2 == 0 and n % 2 !=0:
        #         odd_even_seq_len += 1
        #     elif odd_even_seq_len % 2 !=0 and n%2 == 0:
        #         odd_even_seq_len += 1
        #     else:
        #         continue

        # for n in nums:
        #     if even_odd_seq_len % 2 == 0 and n % 2 ==0:
        #         even_odd_seq_len += 1
        #     elif even_odd_seq_len % 2 !=0 and n%2 != 0:
        #         even_odd_seq_len += 1
        #     else:
        #         continue
        
        # return max(odd_seq_len, even_seq_len, odd_even_seq_len, even_odd_seq_len)

        # Cleaner solution from editorial 
        res = 0
        for pattern in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            cnt = 0
            for num in nums:
                if num % 2 == pattern[cnt % 2]:
                    cnt += 1
            res = max(res, cnt)
        return res


# Example 1:
# Input: nums = [1,2,3,4]
# Output: 4
# Explanation:
# The longest valid subsequence is [1, 2, 3, 4].

# Example 2:
# Input: nums = [1,2,1,1,2,1,2]
# Output: 6
# Explanation:
# The longest valid subsequence is [1, 2, 1, 2, 1, 2].

# Example 3:
# Input: nums = [1,3]
# Output: 2
# Explanation:
# The longest valid subsequence is [1, 3].
