# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i

class Solution:
    def kthCharacter(self, k: int) -> str:
        # iterative solution O(n)
        # word = ['a']
        # while len(word) < k:
        #     next_part = [(chr(((ord(ch) - ord('a') + 1) % 26) + ord('a')))  for ch in word]
        #     word.extend(next_part)
        # return word[k-1]

        # Recursive solution O(log n)
        def get_char(k, layer):
            if layer == 0:
                return 'a'
            half = 1 << (layer -1)
            if k <= half:
                return get_char(k, layer-1)
            prev = get_char(k - half, layer-1)
            return chr(((ord(prev) - ord('a') + 1) % 26) + ord('a'))

        layer = 0
        while (1<<layer) < k:
            layer += 1
        return get_char(k, layer)


# Example 1:

# Input: k = 5

# Output: "b"

# Explanation:

# Initially, word = "a". We need to do the operation three times:

# Generated string is "b", word becomes "ab".
# Generated string is "bc", word becomes "abbc".
# Generated string is "bccd", word becomes "abbcbccd".
# Example 2:

# Input: k = 10

# Output: "c"
