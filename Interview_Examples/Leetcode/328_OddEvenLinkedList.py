"""
Given the head of a singly linked list,
group all the nodes with odd indices together
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        odd_node = head
        even_node_head = head.next
        even_node = head.next

        while (odd_node != None and even_node != None and even_node.next != None):
            #node_after_odd = odd_node.next
            node_after_even = even_node.next

            odd_node.next = node_after_even

            even_node.next = node_after_even.next

            odd_node = odd_node.next
            even_node = even_node.next

        odd_node.next = even_node_head

        return head
