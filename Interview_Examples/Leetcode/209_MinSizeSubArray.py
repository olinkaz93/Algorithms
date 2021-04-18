"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray
[numsl, numsl+1, ..., numsr-1, numsr] of which the sum is
greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

"""


def minSubArrayLen(target, nums):
    if len(nums) == 1 and nums[0] == target:
        return 1
    if len(nums) == 1 and nums[0] != target:
        return 0

    target = target
    right_pointer = 0
    left_pointer = 0
    curr_sum = 0

    minimum = float('inf')

    for right_pointer in range(0, len(nums), 1):
        curr_sum += nums[right_pointer]
        while (curr_sum >= target):
            length = right_pointer - left_pointer + 1
            if length < minimum:
                minimum = length

            curr_sum -= nums[left_pointer]
            left_pointer += 1

    if minimum != float('inf'):
        return minimum
    else:
        return 0



if __name__ == "__main__":
    print(minSubArrayLen(7, [2,3,1,2,4,3]))
