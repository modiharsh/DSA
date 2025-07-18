# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements #Hard #Array #DynamicProgramming #Heap

import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        n = len(nums) // 3
        min_prefix_sums = [0] * (2 * n)
        curr_sum = 0
        max_heap = []

        # First step to calculate prefix sums for first part
        for i in range(2 * n):
            heapq.heappush(max_heap, -nums[i]) # For max_heap, we add negated numbers
            curr_sum += nums[i]

            if len(max_heap) > n:
                curr_sum += heapq.heappop(max_heap) # Numbers are negated so + to actually -
            
            if len(max_heap) == n:
                min_prefix_sums[i] = curr_sum

        # Second step to calculate suffix sums for second part
        min_heap = []
        curr_sum = 0
        max_suffix_sums = [0] * (3 * n)
        for j in range(3 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[j])
            curr_sum += nums[j]

            if len(min_heap) > n:
                curr_sum -= heapq.heappop(min_heap)

            if len(min_heap) == n:
                max_suffix_sums[j] = curr_sum
        
        # Last step to calculate min difference between both parts
        print(min_prefix_sums)
        print(max_suffix_sums)
        min_diff = float('inf')
        for k in range(n-1, 2*n):
            print(min_prefix_sums[k], max_suffix_sums[k+1])
            curr_diff  = min_prefix_sums[k] - max_suffix_sums[k+1]
            min_diff = min(min_diff, curr_diff)
        
        return min_diff


# Example 1:

# Input: nums = [3,1,2]
# Output: -1
# Explanation: Here, nums has 3 elements, so n = 1. 
# Thus we have to remove 1 element from nums and divide the array into two equal parts.
# - If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
# - If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
# - If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
# The minimum difference between sums of the two parts is min(-1,1,2) = -1. 
# Example 2:

# Input: nums = [7,9,5,8,1,3]
# Output: 1
# Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
# If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
# To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
# It can be shown that it is not possible to obtain a difference smaller than 1.
        
