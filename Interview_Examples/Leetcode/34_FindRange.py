"""
34. Find First and Last Position of Element in Sorted Array
Medium

5552

208

Add to List

Share
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109


https://www.youtube.com/watch?v=bU-q1OJ0KWw
https://www.youtube.com/watch?v=YaZVo8hnA9g

"""

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    if len(nums) == 0 or nums == None:
        return [-1, -1]

    low = 0
    high = len(nums) - 1

    # slighly different variation of the
    # classic binary search,
    # we look for the TARGET same way
    # but even having the target founded we sill narrow down the boundries so we have the VERY FIRST, and VERY last index of THE TARGET

    # we find starting index
    # nums = [5,7,7,8,8,10]

    start_index = -1

    while (low <= high):
        mid = low + (high - low) // 2

        if nums[mid] == target:
            start_index = mid
        # if the mid_element in greater than TARGET, we must low down the HIGH boundry
        if nums[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1

    print("start", start_index)
    # we find ending index
    end_index = -1

    low = 0
    high = len(nums) - 1

    while (low <= high):
        mid = low + (high - low) // 2

        # if we find the target we can update the end_pointer, but we still loop through
        if nums[mid] == target:
            end_index = mid
        # if MID element = Target, or MID is lower than target, we scale down the high boudry
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1

    return [start_index, end_index]

if __name__ == "__main__":
    searchRange([5,7,7,8,8,10], 6)
