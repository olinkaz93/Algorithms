"""
Given an integer array nums,
find the contiguous subarray
(containing at least one number)
which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""

#find max sum of subarray size k

import math
def maxSumSubarray(nums, k):
    #find max sum of subarray size k
    max_value = -math.inf
    current_sum = 0
    for i in range (0, len(nums), 1):
        #current_value = nums[i]
        current_sum += nums[i]
        if (i >= k-1): #if we have at least 3 elements, the window is 3 el long