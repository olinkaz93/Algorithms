"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is rotated
at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104


https://www.youtube.com/watch?v=QdVrY3stDD4

1) Find the index of the smallest VALUE - PIVOT
2) Decide if you loop on its right side, or its left side
3) Proceed with regular binary search
"""


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if nums == None or len(nums) == 0:
        return -1
    if len(nums) == 1 and nums[0] == target:
        return 0

    # we need to find the pivot where will we adjust out lower/higher bounds
    # 4,5,6,7,0,1,2
    # 0,1,2,3,4,5,6 - if we have gottten the sorted input
    #                   but in that case we must look for the pivot
    # 4, 5, 6, 7, 0, 1, 2
    # then either TARGET will be AFTER pivot , or BEFORE PIVOT
    # 1) Find element where the array has been pivoted
    # 2) Take decision where we search before, or after
    # 3) Make Binary search

    # 4, 5, 6, 7
    # 0, 1, 2

    low = 0
    high = len(nums) - 1

    # 1) Find the pivot
    # boundries must meet at the moment of the smallest value
    while (low < high):
        # modified binary search

        mid = low + (high - low) // 2
        # if the mid value is greater than high value, means
        # that midpoint IS BEFORE the PIVOT, so we need to look for it on its right
        # we increase the low bound
        # 4, 5, 6, 7, 0, 1, 2
        # L        M        H

        # is this middle element greater of the highest element on the right?
        # in sorted array THE ELEMENT should be < than the high boundry
        # so we need to increase the LOW index
        # as we are sure that THIS MID element is not the smallest
        if nums[mid] > nums[high]:
            low = mid + 1
        # otherwise the pivot is on its left side, we lower down the high bound
        else:  # if the MID element is smaller than THE MAX value from the end
            # this is normal behaviour, we will narrow down the HIGH boundry
            # to the left side
            high = mid
    # that pivot search will end up at the low/left pointer
    pivot = low

    # than we reset the low pointer
    low = 0
    high = len(nums) - 1

    # 2) Having pivot we must to determin where we will make binary search
    # which side?

    # if the X target is greater than the PIVOT or the HIGHEST boundy value
    # we got perfect scenario, we can loop on the pivot's right side
    if (target) >= nums[pivot] and target <= nums[high]:
        low = pivot
    else:
        high = pivot - 1

    # 3) Regular binary search

    while (low <= high):

        mid = low + (high - low) // 2

        if (nums[mid] == target):
            return mid
        elif (nums[mid] < target):
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
