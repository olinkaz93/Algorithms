"""
Given an array nums of n integers,
return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

"""

def fourSum(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(0, len(nums) - 3, 1):
        for j in range(i + 1, len(nums) - 2, 1):
            left, right = j + 1, n - 1

            # t = target - nums[i] - nums[j]
            while left < right:
                sum_nums = nums[i] + nums[j] + nums[left] + nums[right]
                if sum_nums == target:
                    if [nums[i], nums[j], nums[left], nums[right]] not in result:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif sum_nums > target:
                    right -= 1
                else:
                    left += 1
    return result


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = fourSum(nums, target)
    print(result)