"""
15. 3Sum
Medium

10333

1066

Add to List

Share
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""

def threeSum(nums):
    res = []
    n = len(nums)
    nums = sorted(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1
        new_target = -nums[i]
        while j < k:
            summ = nums[j] + nums[k]
            if summ < new_target:
                j += 1
            elif summ > new_target:
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j + 1] == nums[j]:
                    j += 1
                j += 1
                while k > j and nums[k - 1] == nums[k]:
                    k -= 1
                k -= 1
    return res


if __name__ == "__main__":
    print(threeSum([-1,0,1,2,-1,-4]))