# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array

class Solution:
    def findKDistantIndices(
        self, nums: List[int], key: int, k: int
    ) -> List[int]:
        res = []
        r = 0  # unjudged minimum index
        n = len(nums)
        for j in range(n):
            if nums[j] == key:
                l = max(r, j - k)
                r = min(n - 1, j + k) + 1
                for i in range(l, r):
                    res.append(i)
        return res

# Wrong logic
# class Solution:
#     def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
#         matching_key_indexes = [i for i,j in enumerate(nums) if j==key]
#         length = len(nums)
#         result_set = set(matching_key_indexes)
#         for idx in matching_key_indexes:
#             for i in range(1, k+1):
#                 if idx - k >=0:
#                     result_set.add(idx-i)
#                 if idx + k < length:
#                     result_set.add(idx+i)
        
#         return sorted(result_set)


# Example 1:

# Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
# Output: [1,2,3,4,5,6]
# Explanation: Here, nums[2] == key and nums[5] == key.
# - For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j where |0 - j| <= k and nums[j] == key. Thus, 0 is not a k-distant index.
# - For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
# - For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
# - For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
# - For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
# - For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
# - For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
# Thus, we return [1,2,3,4,5,6] which is sorted in increasing order. 
# Example 2:

# Input: nums = [2,2,2,2,2], key = 2, k = 2
# Output: [0,1,2,3,4]
# Explanation: For all indices i in nums, there exists some index j such that |i - j| <= k and nums[j] == key, so every index is a k-distant index. 
# Hence, we return [0,1,2,3,4].
