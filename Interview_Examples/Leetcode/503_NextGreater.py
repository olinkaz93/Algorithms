"""
503. Next Greater Element II
Medium

2418

92

Add to List

Share
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.



Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]


Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109

https://www.youtube.com/watch?v=ARkl69eBzhY

we loop thorugh x2 so we keep indices and then % to keep proportion for the array
"""


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [-1]

        max_stack = []
        result = [-1] * len(nums)

        # we loop trough the values, and append to stack
        # if there is value which is bigger, we pop the element
        # which is lower than this and update its indeces
        # when we reach the end of list

        # we make it two times, and then keep modulo of index, so we are in the range

        length = len(nums)
        for i in range(0, 2 * length, 1):
            index = i % length
            while (max_stack and nums[index] > nums[max_stack[-1]]):
                popped_element = max_stack.pop()
                # print(popped_element)
                result[popped_element] = nums[index]
            max_stack.append(index)

        return result
        """
        print("currentmax", current_max)
        for i in range(0, len(result), 1):
            if(result[i] == -1 and i != max_index and result[i] < current_max):
                result[i] = current_max

        return result
        """