# https://leetcode.com/problems/maximum-difference-between-increasing-elements

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        min_num = nums[0]
        max_diff = -1

        for i in range(1, len(nums)):
            if nums[i] > min_num:
                max_diff = max(max_diff, nums[i] - min_num)
            else:
                min_num = nums[i]
        return max_diff

      
# Example 1:

# Input: nums = [7,1,5,4]
# Output: 4
# Explanation:
# The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
# Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
# Example 2:

# Input: nums = [9,4,3,2]
# Output: -1
# Explanation:
# There is no i and j such that i < j and nums[i] < nums[j].
# Example 3:

# Input: nums = [1,5,2,10]
# Output: 9
# Explanation:
# The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
