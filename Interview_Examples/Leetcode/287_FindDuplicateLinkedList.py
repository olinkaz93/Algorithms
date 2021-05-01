"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.


Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1


https://www.youtube.com/watch?v=Oq-FnANg-R4
"""

def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    """
    Let's try to approach the list as a linked list,
    since we cannot loop n^2 - the contraint, also we cannot sort the elements - than we could 
    just compare neibour elements
  i: 0  1  2  3  4  5  6 
    [1, 2, 3, 4, 5, 4, 7]



    ListNode:
    self.value = value
    self.next = None

    =================== We can make analogy of list to the linked list:
        treating THE VALUE, e.g. nums[0] as the pointer

    0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 4 ... | this makes CYCLE in the linked list!


    """
    # initialize the data starting nodes/values
    slow = nums[0]  # slow_pointer = 1, so at each nums[i], we store .next value
    fast = nums[0]  # fast_pointer = 1

    # we will go slow_pointer by 1 step, and fast_pointer by 2 steps
    # slow is the POINTER to the VALUE, so we can go STEP by STEP, by going to THE NEXT VALUE,

    while (True):
        slow = nums[slow]
        fast = nums[nums[fast]]  # fast pointer will go twice steps
        if slow == fast:
            break

    # we found a crossing value, now we go to find the duplicate element, tha caused the loop

    # we reseat the SLOW pointer, and go one step at the time for each pointer
    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow