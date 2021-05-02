"""
2. Add Two Numbers
Medium

11609

2762

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        """
        Input: l1 = [2,4,3],
               l2 = [5,6,4]
        Output:     [7,0,8]
        Explanation: 342 + 465 = 807.

            [2, 4, 3]    [ 2, 4, 4, 3]   [ 9, 9, 9, 9, 9]
            [5, 6, 4]    [ 2, 6, 6, 3]   [ 1, 1, 1, 1, 1]
                           5  1  0  6  | 1   1   1  1  1  0 | We add the

        We can traverse from the head of the two linked lists,

        l1 = [9,9,9,9,9,9,9], 
        l2 = [9,9,9,9]           =>   [8,9,9,9,0,0,0,1]

        R = [8] ( 9 + 9 = 18, so we keep 8 and carry the '+1' for next pointer)       

        1)
            9 + 9, carry 0 (as we are in the head)
          = 18 (carry = (9+9)//10)  , we append

Output: [8,9,9,9,0,0,0,1]

        """
        """
        if l1.val == 0 and l1.next == None and l2.val == 0 and l2.next == 0:
            return [0]

        pointer1 = l1
        pointer2 = l2

        result = []

        dummy_node = ListNode(-1)

        #we perform sum of two numbers if X//10 == 1 -> we carry this +1 for next pair of numbers
        #first sum will have no carry
        carry = 0

        while (pointer1 != None and pointer2 != None):

            value = (pointer1.val + pointer2.val + carry)
            print(value)
            print("carry", (value)//10)
            result.append(value%10)
            if value//10 == 1:

                carry = 1
            else:
                carry = 0

            pointer1 = pointer1.next
            pointer2 = pointer2.next

        if pointer2 == None:
            while (pointer1 != None):
                value = (pointer1.val + carry)
                result.append(value%10)
                if value//10 == 1:
                    carry = 1
                else:
                    carry = 0

                pointer1 = pointer1.next

        elif pointer1 == None:
             while (pointer2 != None):
                value = (pointer2.val + carry)
                result.append(value%10)
                if value//10 == 1:
                    carry = 1
                else:
                    carry = 0

                pointer2 = pointer2.next

        if carry == 1:
            result.append(carry)
        print(result)
        """
        # return result

        #########################################################################
        # LINKED LIST

        if l1.val == 0 and l1.next == None and l2.val == 0 and l2.next == 0:
            return [0]

        pointer1 = l1
        pointer2 = l2

        # dummy keeps the reference late to the head

        dummy_head = ListNode(-1)

        pointer3 = dummy_head

        # head = None

        carry = 0

        while (pointer1 != None and pointer2 != None):
            value = pointer1.val + pointer2.val + carry

            new_node = ListNode(value % 10)
            # if head == None:
            #    head = new_node

            pointer3.next = new_node

            if (value // 10 == 1):
                carry = 1
            else:
                carry = 0

            pointer1 = pointer1.next
            pointer2 = pointer2.next

            pointer3 = pointer3.next
        print(dummy_head)

        if pointer2 == None:
            while (pointer1 != None):
                value = pointer1.val + carry

                new_node = ListNode(value % 10)
                pointer3.next = new_node

                if (value // 10 == 1):
                    carry = 1
                else:
                    carry = 0

                pointer1 = pointer1.next
                pointer3 = pointer3.next

        elif pointer1 == None:
            while (pointer2 != None):
                value = pointer2.val + carry

                new_node = ListNode(value % 10)
                pointer3.next = new_node

                if (value // 10 == 1):
                    carry = 1
                else:
                    carry = 0

                pointer2 = pointer2.next
                pointer3 = pointer3.next

        if carry > 0:
            new_node = ListNode(1)
            pointer3.next = new_node

        return dummy_head.next






