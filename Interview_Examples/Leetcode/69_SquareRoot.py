"""
https://www.youtube.com/watch?v=fItuKa_tIpY

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.



Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.



https://www.youtube.com/watch?v=fItuKa_tIpY
https://www.youtube.com/watch?v=l3q2yeHRck8
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # we look for the element to get the SQRT, without using a squrt function

        # we will perform binary search, until we find the element which nums[mid]*nums[mid] <= X

        low = 1
        high = x
        result = 0
        while (low <= high):

            mid = low + (high - low) // 2

            if mid <= x / mid:
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
