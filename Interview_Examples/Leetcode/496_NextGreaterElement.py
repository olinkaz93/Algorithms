"""
You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.

Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.



Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array is 3.
For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation:
For number 2 in the first array, the next greater number for it in the second array is 3.
For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

#######################

Next Greater Element I https://leetcode.com/problems/next-greater-element-i/

Algorithm

https://discuss.leetcode.com/topic/77916/java-10-lines-linear-time-complexity-o-n-with-explanation
Suppose we have a decreasing sequence followed by a greater number.
For example [5, 4, 3, 2, 1, 6] then the greater number 6 is the next greater element for all previous numbers in the sequence.
We use a stack to keep a decreasing sub-sequence,
whenever we see a number x greater than stack.peek() we pop all elements less than x and for all the popped ones, their next greater element is x.
For example [9, 8, 7, 3, 2, 1, 6].
The stack will first contain [9, 8, 7, 3, 2, 1]
and then we see 6 which is greater than 1 so we pop 1 2 3 whose next greater element should be 6.



"""


def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    # let's treat nums 1 as a keys
    # then we can make nums dictionary with max to the right,
    # we will loop from the end (stack)

    if len(nums2) == 1:
        return [-1]

    dic = {}
    stack = []
    for i in range(len(nums2)):
        while stack and stack[-1] < nums2[i]:
            dic[stack.pop()] = nums2[i]
        stack.append(nums2[i])
    res = []

    for x in nums1:
        if x in dic:
            res.append(dic[x])
        else:
            res.append(-1)
    return res




