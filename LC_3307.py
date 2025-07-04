# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:

        # Iterative solution - TLE
        # word = ['a']
        # i = 0 
        # while len(word) < k:
        #     if operations[i] == 0:
        #         next_part = word
        #     else:
        #         next_part = [chr(((ord(ch) - ord('a') + 1) %26) + ord('a')) for ch in word]
        #     word.extend(next_part)
        #     i += 1
        # return word[k-1]

        # Recursive solution
        def get_char(k, layer):
            if layer == 0:
                return 'a'
            half = 1 << (layer-1)
            if k <= half:
                return get_char(k, layer-1)
            prev = get_char(k - half, layer-1)
            if operations[layer-1] == 0:
                return prev
            else:
                return chr(((ord(prev) - ord('a') + 1) % 26) + ord('a'))

        layer = 0
        while (1<<layer) < k:
            layer += 1
        return get_char(k, layer)


# Example 1:

# Input: k = 5, operations = [0,0,0]

# Output: "a"

# Explanation:

# Initially, word == "a". Alice performs the three operations as follows:

# Appends "a" to "a", word becomes "aa".
# Appends "aa" to "aa", word becomes "aaaa".
# Appends "aaaa" to "aaaa", word becomes "aaaaaaaa".
# Example 2:

# Input: k = 10, operations = [0,1,0,1]

# Output: "b"

# Explanation:

# Initially, word == "a". Alice performs the four operations as follows:

# Appends "a" to "a", word becomes "aa".
# Appends "bb" to "aa", word becomes "aabb".
# Appends "aabb" to "aabb", word becomes "aabbaabb".
# Appends "bbccbbcc" to "aabbaabb", word becomes "aabbaabbbbccbbcc".
