# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer #LinkedList #Math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # My initial solution
        # num_list = []
        # while head:
        #     num_list.append(head.val)
        #     head = head.next
        
        # num = 0
        # n = len(num_list)
        # for i in range(n):
        #     curr = num_list.pop()
        #     num = num + (2 ** i) * curr
        # return num

        # Optimized solution with O(1) space complexity
        num = 0
        while head:
            num = num * 2 + head.val
            head = head.next
        return num

        # Alternative solution with bitwise operations
        # num = 0
        # while head:
        #     num = (num << 1) | head.val
        #     head = head.next
        # return num


# Example 1:

# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:

# Input: head = [0]
# Output: 0
