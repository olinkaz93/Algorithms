"""
162. Find Peak Element
Medium

2786

2650

Add to List

Share
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.



Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

"""

"""
https://stackoverflow.com/questions/57194118/confuse-in-binary-search-when-to-use-left-right-left-right-and-few-more
We use while (lo <= hi) if we are returning the match from inside the loop.
We use while (lo < hi) when we want to exit the loop first and then use the result of lo or hi to return the match.

https://www.youtube.com/watch?v=CFgUQUL7j_c
"""

"""
We start off by finding the middle element,
midmid from the given numsnums array.
If this element happens to be lying in a descending sequence of numbers.
or a local falling slope(found by comparing nums[i]nums[i] to its right neighbour),
it means that the peak will always lie towards the left of this element.
Thus, we reduce the search space to the left of midmid(including itself) and perform the same process on left subarray.

If the middle element
midmid lies in an ascending sequence of numbers,
or a rising slope(found by comparing nums[i]nums[i] to its right neighbour),
it obviously implies that the peak lies towards the right of this element.
Thus, we reduce the search space to the right of midmid and perform the same process on the right subarray.

In this way, we keep on reducing the search space till we eventually reach a state where only one element is remaining in the search space. This single element is the peak element.
"""





class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # looping linear is not the most time efficient
        # we can think about the binary search
        # to get BigO(logN)
        # for binary search - prerequisite is sorted array

        low = 0
        high = len(nums) - 1

        while (low < high):
            mid = low + (high - low) // 2
            # to get element at middle index
            # we know if is a peak if the element is lower than the element to the right
            if (nums[mid] < nums[mid + 1]):
                low = mid + 1
            else:
                high = mid

        return low
