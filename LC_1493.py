# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element #Medium #DynamicProgramming #SlidingWindow

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # DP approach : O(n), O(n)
        # n = len(nums)
        # dp0 = [0] * n
        # dp1 = [0] * n
        # dp0[0] = nums[0]

        # max_len = 0

        # for i in range(1, n):
        #     if nums[i] == 1:
        #         dp0[i] = dp0[i-1] + 1
        #         dp1[i] = dp1[i-1] + 1
        #     else:
        #         dp0[i] = 0
        #         dp1[i] = dp0[i-1] # delete this zero
                 
        #     max_len = max(max_len, dp1[i])

        # return max_len

        #Sliding Window approach : O(n), O(1)
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right-left+1)

        return max_len - 1 # Since we must delete one element, return max_len - 1.


Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
