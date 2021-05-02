"""
1. Two Sum
Easy

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""
def twoSum(self, nums, target):

        # return indices of TWO numbers, that nums[i] + nums[j] = target

        # we can loop through the nums, ans see if the missed element is in the dictionary

        dictionary = {}

        for i in range(0, len(nums), 1):

            x = target - nums[i]  # [3, 3]

            if x in dictionary:
                second_index = dictionary[x]
                first_index = i
                if second_index != first_index:
                    return [first_index, second_index]
            else:
                dictionary[nums[i]] = i










