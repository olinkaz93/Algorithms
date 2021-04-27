"""

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

https://www.youtube.com/watch?v=XtYEEvrhemI
https://www.youtube.com/watch?v=Kka8VgyFZfc

"""


# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    """
    def removeNthFromEnd(self, head, n):

        fast_pointer = head
        pointer_previous = head
        counter = 0

        while (fast_pointer != None):
            counter += 1
            fast_pointer = fast_pointer.next

        steps = counter - n

        # 5 elements, 2 from the end -> 3rd node needed
        # must make 2 hops / end up at 3rd node
        if steps == 0:
            head = head.next
            return head

        for step in range(1, steps): #
            pointer_previous = pointer_previous.next

        pointer_previous.next = pointer_previous.next.next

        return head




    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head

        fast_pointer = dummy
        slow_pointer = dummy
        steps = 0

        while (fast_pointer.next != None):
            fast_pointer = fast_pointer.next
            steps += 1
            if (n - steps < 0):
                slow_pointer = slow_pointer.next

        slow_pointer.next = slow_pointer.next.next

        return dummy.next
        """


    """ We create a dummy node,
    and start our pointers from there,
    the distance between them must be N steps away, in that case I will find the reference
    to the element tha must be deleted """

    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head

        fast_pointer = dummy
        slow_pointer = dummy
        steps = 0

        # fast pointer needs to go N steps ahead, until slow pointer will be able to move
        for i in range(0, n):
            fast_pointer = fast_pointer.next

            """
            Input: head = [1,2,3,4,5], n = 2
            
            Output: [1,2,3,5]
            """

        while (fast_pointer.next != None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        slow_pointer.next = slow_pointer.next.next

        return dummy.next






