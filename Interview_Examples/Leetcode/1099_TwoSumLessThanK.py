"""
Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.



Example 1:

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.

"""
def twoSumLessThanK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if (len(nums) < 2):
        return -1

    """
    sum such that there exists i < j
    with nums[i] + nums[j] = sum
    and sum < k.
    If no i, j exist satisfying
    this equation, return -1.
    """

    # i, j - sliding window, two pointers
    # nums[i] + nums[j] = sum
    # and sum < k
    # so we look for the sum of two numbers that are the closest maximum to its K value
    # if no return -1

    nums.sort()

    # so we will look through when the SUM is LESS than K
    # if the sum is > K , we must decremet,

    # having sorted array we will have the lowest element on its LEFT
    # and the highest element on its very far right
    # [10,20,30,40,50,60,70,80,90,100], k = 70

    print(nums)

    left_pointer = 0
    right_pointer = len(nums) - 1
    current_max = float('-inf')

    while (left_pointer < right_pointer):

        summ = nums[left_pointer] + nums[right_pointer]
        if summ >= k:
            right_pointer -= 1
        else:
            print(summ)
            if summ > current_max:
                current_max = summ
            left_pointer += 1

    if current_max != float('-inf'):
        return current_max
    else:
        return -1