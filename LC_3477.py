# https://leetcode.com/problems/fruits-into-baskets-ii #Easy #Array #BinarySearch #Simulation #OrderedSet

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        count = 0

        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    count += 1
                    baskets[j] = -1
                    break
        
        return n - count


# Example 1:
# Input: fruits = [4,2,5], baskets = [3,5,4]
# Output: 1
# Explanation:
# fruits[0] = 4 is placed in baskets[1] = 5.
# fruits[1] = 2 is placed in baskets[0] = 3.
# fruits[2] = 5 cannot be placed in baskets[2] = 4.
# Since one fruit type remains unplaced, we return 1.

# Example 2:
# Input: fruits = [3,6,1], baskets = [6,4,7]
# Output: 0
# Explanation:
# fruits[0] = 3 is placed in baskets[0] = 6.
# fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
# fruits[2] = 1 is placed in baskets[1] = 4.
# Since all fruits are successfully placed, we return 0.
