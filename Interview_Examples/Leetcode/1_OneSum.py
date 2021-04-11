"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
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
def twoSum(nums, target):


    dictionary_of_numbers = {}

    # create a dictionary with the value of the number as a key, and index as a value
    # while creating a hash map, check if the number2 has occured already
    # if so return the indices

    for index, number in enumerate(nums):
        dictionary_of_numbers[number] = index
        print(dictionary_of_numbers)
        number2 = target - number

        #if number2 in dictionary_of_numbers:
        #    return [index, dictionary_of_numbers[number2]]


if __name__ == "__main__":
    numbers = [3,3]
    result = twoSum(numbers, 6)
    #print(result)

