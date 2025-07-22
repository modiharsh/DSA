# https://leetcode.com/problems/maximum-erasure-value #Array #SlidingWindow

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        curr_sum = max_sum = 0
        seen = set()

        for right in range(n):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            seen.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)

        return max_sum


# Example 1:

# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
# Example 2:

# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
