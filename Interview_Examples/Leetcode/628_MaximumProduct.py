"""
628. Maximum Product of Three Numbers
Easy

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.


Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6


Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000

"""
def maximumProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # nums = [-1,-2,-3] , the x*y*z is high when we have either 3 positive
    #                   numbers, or two negatives and 1 positive

    """
    if len(nums) < 3:
        return None

    nums.sort()

    positive_product = nums[-3]*nums[-2]*nums[-1]
    mixed_product = nums[0]*nums[1]*nums[-1]

    maximum = max(positive_product, mixed_product)

    return maximum
    """
    # Alternative option is to loop linear the list and find 2minimums, and 1 max. and , 2 other maximums than we can calculate and get higher value

    minimum1 = float('inf')
    minimum2 = float('inf')
    maximum1 = float('-inf')
    maximum2 = float('-inf')
    maximum3 = float('-inf')

    for el in nums:
        if el <= minimum1:
            minimum2 = minimum1
            minimum1 = el
        elif el <= minimum2:
            minimum2 = el

        if el >= maximum1:
            maximum3 = maximum2
            maximum2 = maximum1
            maximum1 = el
        elif el >= maximum2:
            maximum3 = maximum2
            maximum2 = el
        elif el >= maximum3:
            maximum3 = el

    mixed_product = minimum1 * minimum2 * maximum1
    positive_product = maximum1 * maximum2 * maximum3
    maximum = max(mixed_product, positive_product)

    return maximum