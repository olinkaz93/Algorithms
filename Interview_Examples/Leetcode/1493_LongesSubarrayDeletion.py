"""
1493. Longest Subarray of 1's After Deleting One Element
Medium

398

7

Add to List

Share
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.

Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
Example 4:

Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4
Example 5:

Input: nums = [0,0,0]
Output: 0


Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""


def longestSubarray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    result = 0

    # longest nonempty subrray which has only 1's
    # that means either we have only 1's or maximum just one zero
    # nums = [1,1,0,1], if we remove 0, we will have length  = 3
    # nums = [0,1,1,1,0,1,1,0,1], if we remove 0, we will have 5, length - 1, utmost ONE zero
    # nums = [1,1,1], no 0's, length - 1, no zeros, but still - 1 element

    left = 0
    zeros = 0

    for right in range(0, len(nums), 1):

        if (nums[right] == 0):
            zeros += 1

        while (zeros > 1):
            if (nums[left] == 0):
                zeros -= 1

            left += 1

        subarray = right - left
        result = max(result, subarray)

    return result