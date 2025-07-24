# https://leetcode.com/problems/valid-anagram/description/ #Array #Easy #Hashtable #Strings

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Method 1
        # return Counter(s) == Counter(t)

        # Method 2
        if len(s) != len(t):
            return False

        my_hashmap = defaultdict(int)
        for c in s:
            my_hashmap[c] += 1
        for c in t:
            my_hashmap[c] -= 1

        return all(v==0 for v in my_hashmap.values())


# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
