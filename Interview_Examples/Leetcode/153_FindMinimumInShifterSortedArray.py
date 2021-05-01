"""
153. Find Minimum in Rotated Sorted Array
Medium

3406

303

Add to List

Share
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


"""
def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if (len(nums) == 0 or nums == None):
        return -1


    low = 0
    high = len(nums) - 1

    # we got the shifted array, that has been shifted K times
    # we use the modified binary search to fins the index of the lowest value in this shifted array/list


    # [4,5,6,7,0,1,2]
    #  L     M     H  # the nums[mid] is higher than nums[high], so we need to BS on its right


    while (low < high):

        mid = low + (high - low) // 2

        if (nums[mid] > nums[high]):
            low = mid + 1

        # [7, 0, 1, 2, 3, 4, 5]  // 'normal' scanario, nums[mid] is < than nums[high], we descrese the high pointer
        #  L        M        H
        else:
            high = mid

    # we loop through until low < high, when we got low = high, we reached the minimum value LOW

    return nums[low]