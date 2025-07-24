# https://leetcode.com/problems/group-anagrams/ #Arrays #Hashtable #Sorting #Medium

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Method 1 - O(n.k.log n)
        # string_hash = {}
        # for s in strs:
        #     sorted_s = ''.join(sorted(s))
        #     if sorted_s in string_hash:
        #         string_hash[sorted_s].append(s)
        #     else:
        #         string_hash[sorted_s] = [s]
        # return [s for s in string_hash.values() ]

        # Method 2 - - O(n.k)
        string_hash = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            string_hash[tuple(count)].append(s)
        return list(string_hash.values())


# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]


