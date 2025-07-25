# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion #Easy #Array #Greedy

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if all(x < 0 for x in nums):
            return max(nums)
        else:
            return sum(set(filter(lambda x:x>0, nums)))
        
      
Example 1:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation:
Select the entire array without deleting any element to obtain the maximum sum.

Example 2:
Input: nums = [1,1,0,1,1]
Output: 1
Explanation:
Delete the element nums[0] == 1, nums[1] == 1, nums[2] == 0, and nums[3] == 1. Select the entire array [1] to obtain the maximum sum.

Example 3:
Input: nums = [1,2,-1,-2,1,0,-1]
Output: 3
Explanation:
Delete the elements nums[2] == -1 and nums[3] == -2, and select the subarray [2, 1] from [1, 2, 1, 0, -1] to obtain the maximum sum.
