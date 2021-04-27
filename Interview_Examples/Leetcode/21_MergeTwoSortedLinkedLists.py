"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.



Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        current_l1 = l1
        current_l2 = l2
        # result = []
        dummy = ListNode(-1)

        if current_l1.val <= current_l2.val:
            result_linked = ListNode(current_l1.val)
            current_l1 = current_l1.next
        else:
            result_linked = ListNode(current_l2.val)
            current_l2 = current_l2.next

        dummy.next = result_linked

        while (current_l1 != None and current_l2 != None):
            if current_l1.val <= current_l2.val:
                # result.append(current_l1.val)
                result_linked.next = current_l1
                result_linked = current_l1
                current_l1 = current_l1.next
            else:
                # result.append(current_l2.val)
                result_linked.next = current_l2
                result_linked = current_l2
                current_l2 = current_l2.next

        if (current_l1 != None):
            while (current_l1 != None):
                # result.append(current_l1.val)
                result_linked.next = current_l1
                result_linked = current_l1
                current_l1 = current_l1.next

        elif (current_l2 != None):
            while (current_l2 != None):
                # result.append(current_l2.val)
                result_linked.next = current_l2
                result_linked = current_l2
                current_l2 = current_l2.next

        # print(result)
        # print(dummy.next)
        return dummy.next

