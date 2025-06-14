# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        
        nums.sort()
        low, high = 0, nums[-1] - nums[0]

        def can_form_valid_pairs(threshold):
            c = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= threshold:
                    c += 1
                    i += 1
                i += 1
                if c >= p:
                    return True
            return False

        while low < high:
            mid = (high + low) // 2
            if can_form_valid_pairs(mid):
                high = mid
            else:
                low = mid + 1

        return low


# Example 1:

# Input: nums = [10,1,2,7,1,3], p = 2
# Output: 1
# Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
# The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
# Example 2:

# Input: nums = [4,2,1,2], p = 1
# Output: 0
# Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

# This problem involves forming p pairs of elements such that the maximum absolute difference among all chosen pairs is minimized. To approach it efficiently, a binary search strategy combined with greedy pairing works well.

# Solution Explanation:
# Sort the array: Sorting helps in efficiently finding the closest pairs.

# Binary search on the maximum difference: We search for the smallest possible max difference (low to high).

# Check feasibility: For a candidate difference mid, determine if we can form p pairs without reusing indices.

# Pair elements greedily: Iterate through sorted nums, and greedily pair adjacent elements if their difference is within mid.

# This approach ensures an optimal O(n log m) complexity, where n is the length of nums and m is the range of differences.
