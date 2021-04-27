"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []


https://www.youtube.com/watch?v=gfFn-OXxcgU
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # to remove elements we must see 2 different approaches of removing the elements
        # consider the fact when we start to remove the head element
        while (head != None and head.val == val):
            head = head.next

        node = head
        # and the looping through other elements
        while (node != None and node.next != None):
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return head

