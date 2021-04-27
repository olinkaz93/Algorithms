"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        if k == 0:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        old_head = head

        current = head
        count = 1

        while current.next != None:
            current = current.next
            count += 1

        # we calculate the nodes, and create a cycle
        current.next = old_head

        # get % of rotation
        k = k % count
        steps = count - k

        # steps = 5 - 2 = 3
        # head = [1,2,3,4,5], k = 2
        # we need to get to (3) Node, set new head
        # as its .next and than break the cycle node.next == None

        slower = dummy  # if we iterate from dummy we are away -1 step
        # slower = head / if we iterate from head is +1 steps away
        for i in range(0, steps, 1):
            slower = slower.next

        new_head = slower.next
        slower.next = None

        return new_head





