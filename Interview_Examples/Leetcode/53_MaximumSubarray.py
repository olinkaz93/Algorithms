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
https://youtu.be/5WZl3MMT0Eg
"""

"""
The idea is to just focus on the positive number first.
If the final sum is unchanged and the maximum value is a negative number.
That means we just need to return the least negative number which is just one negative from the entire array.
"""


def subarraySum(nums):
    best_sum = 0
    current_sum = 0
    for x in nums:
        current_sum = max(0, current_sum + x)
        print(current_sum)
        best_sum = max(best_sum, current_sum)
        print(best_sum)

    if max(nums) < 0 and best_sum == 0:
        return max(nums)
    return best_sum


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = subarraySum(nums)
    print(result)