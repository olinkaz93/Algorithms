# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        # we keep fast runner and slow runner
        # fast runner goes to the end of the list
        # when it reaches , the point of slow runner will reverse the list
        #then compare the values
        
class Solution(object):
    
    def reverse(self, node):
        if node == None:
            return None
        
        current = node
        previous = None
        while (current != None):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        head = previous
        return head
    
    def isPalindrome(self, head):
        
        if head == None:
            return False
        if head.next == None:
            return True
        
        slow_runner = head
        fast_runner = head
        
        while (fast_runner != None and fast_runner.next != None):
            fast_runner = fast_runner.next.next
            slow_runner = slow_runner.next
        
        sorted_half_linked_list = self.reverse(slow_runner)
                
        fast_runner = head
        slow_runner = sorted_half_linked_list
        #print(slow_runner.val)
        #print(slow_runner.next.val)
        
        
        #print("MAIN",head)
        #print("SORTED",sorted_half_linked_list)
        
        while(slow_runner != None):
            
            if fast_runner.val != slow_runner.val:
                return False
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next
        
        return True