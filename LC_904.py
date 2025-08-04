# https://leetcode.com/problems/fruit-into-baskets #Medium #SlidingWindow #Array #Hashtable

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
    
        fruit_count = defaultdict(int)
        left = 0
        max_fruits = 0
        
        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1
            
            # Shrink window if more than 2 types of fruits
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            
            # Update max fruits picked
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits


# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].

                



