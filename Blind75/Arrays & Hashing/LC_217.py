# https://leetcode.com/problems/contains-duplicate/ #Arrays #Easy #Hash Table

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Method 1
        # return len(nums) != len(set(nums)) 

        # Method 2
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
