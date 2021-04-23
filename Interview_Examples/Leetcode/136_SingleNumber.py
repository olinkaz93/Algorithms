"""
Given a non-empty array of integers nums,
every element appears twice except for one.
Find that single one.

Follow up: Could you implement a solution
with a linear runtime complexity and without using extra memory?

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

"""


def singleNumber(self, nums):
    if len(nums) == 0:
        return False

    nums.sort()
    previous_element = 0
    index = 1
    while index < len(nums):
        if nums[previous_element] == nums[index]:
            index += 2
            previous_element += 2
        elif nums[previous_element] != nums[index]:
            return nums[previous_element]
    return nums[-1]



if __name__ == "__main__":
    list_a = [1,2,2]
    list_b = [1,1]

    print(singleNumber(list_a))


