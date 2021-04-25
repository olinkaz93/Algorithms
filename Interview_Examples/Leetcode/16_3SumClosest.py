"""
Given an array nums of n integers
and an integer target,
find three integers in nums
such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""

def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # we need to loop for each element and find the other two elements in sliding window, until we find a sum.
    # when we get sum of 3 elements we check if is the closest to the target sum

    if len(nums) < 3:
        return None

    # we must sort the list ! so we can use pointers!
    nums.sort()

    # the initial sum is made from 3 elements
    result = nums[0] + nums[1] + nums[-1]

    # then we loop for every element and try to find the 3 elements, which sum
    # is closest to the target

    for i in range(0, len(nums) - 2, 1):
        low_pointer = i + 1
        high_pointer = len(nums) - 1

        while (low_pointer < high_pointer):
            current_sum = nums[i] + nums[low_pointer] + nums[high_pointer]
            if current_sum > target:
                high_pointer -= 1
            else:
                low_pointer += 1

            if abs(current_sum - target) < abs(result - target):
                result = current_sum

    return result

if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1

    print(threeSumClosest(nums, target))