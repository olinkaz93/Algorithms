"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

FLOYD ALGORITHM
fast_runner + slow_runner
and then extra pointer!
https://www.youtube.com/watch?v=UmudS7EXz6o

"""

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return None

        slow_runner = head
        fast_runner = head

        while fast_runner != None and fast_runner.next != None:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
            if slow_runner == fast_runner:
                pointer = head
                while fast_runner != pointer:
                    fast_runner = fast_runner.next
                    pointer = pointer.next
                return pointer
