"""
540. Single Element in a Sorted Array
Medium

2416

88

Add to List

Share
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.



Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10


Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5

"""


def singleNonDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # So we look for the element that exists ONLY ONCE
    # the nums are SORTED
    # we can use binary SEARCH
    # must find the element that exist only once
    # nums = [1,1,2,3,3,4,4,8,8]
    # we can see that the element that is only ONCE, split the input array
    # for either two sides with EVEN number of numbers
    # or just [X: rest numbers] or [restnumbers:x]

    """
    if you are returning from inside the loop, use left <= right
    if you are reducing the search space, use left < right and finally return a[left]

    nums = [1,1,2,3,3,4,4,8,8]
                X
    Elements on the left are soubles, length is odd
    Elements on the right as well

            0 1 2 3 4 5 6 7 8
    nums = [1,1,2,3,3,4,4,8,8]
                    X

    when we perform binary check we need  to see if MID % 2 == 0
    If is at odd position we must  swift to its left - 1, so then pairs are equal


    https://www.youtube.com/watch?v=sxletPlNuK4
    """

    low = 0
    high = len(nums) - 1

    while (low < high):
        mid = low + (high - low) // 2

        if mid % 2 == 1:  # if the index is even we need to make it odd, so we swift -1
            mid = mid - 1
        if nums[mid] == nums[mid + 1]:
            # if the paired elements are the same, that means, all element on its                                           left are also paired, so we make a low mid + 2
            low = mid + 2
        else:
            high = mid

    return nums[low]