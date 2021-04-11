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


def singleNumber(nums):

    dictionary_numbers = {}
    for number in nums:
        if number not in dictionary_numbers:
            dictionary_numbers[number] = 1
        else:
            dictionary_numbers[number] += 1

    for number in dictionary_numbers:
        if dictionary_numbers[number] == 1:
            return number

if __name__ == "__main__":
    list_a = [1,2,2]
    list_b = [1,1]

    print(singleNumber(list_a))


