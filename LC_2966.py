# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Initial version
        # nums.sort()
        # res = []
        # i = 0
        # curr = []
        # for num in nums:
        #     curr.append(num)
        #     i += 1
        #     if i == 3:
        #         if curr[-1] - curr[0] > k:
        #             return [] 
        #         else:
        #             res.append(curr)
        #             curr = []
        #         i = 0
        # return res

        # Cleaner code version
        nums.sort()
        res = []
        n = len(nums)
        for i in range(0, n, 3):
            group = nums[i:i+3]
            if group[-1] - group[0] > k:
                return []
            res.append(group)
        return res


# Example 1:

# Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
# Output: [[1,1,3],[3,4,5],[7,8,9]]
# Explanation:
# The difference between any two elements in each array is less than or equal to 2.

# Example 2:
      
# Input: nums = [2,4,2,2,5,2], k = 2
# Output: []
# Explanation:
# Different ways to divide nums into 2 arrays of size 3 are:

# [[2,2,2],[2,4,5]] (and its permutations)
# [[2,2,4],[2,2,5]] (and its permutations)
# Because there are four 2s there will be an array with the elements 2 and 5 no matter how we divide it. since 5 - 2 = 3 > k, the condition is not satisfied and so there is no valid division.

# Example 3:

# Input: nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14
# Output: [[2,2,12],[4,8,5],[5,9,7],[7,8,5],[5,9,10],[11,12,2]]
# Explanation:
# The difference between any two elements in each array is less than or equal to 14.
