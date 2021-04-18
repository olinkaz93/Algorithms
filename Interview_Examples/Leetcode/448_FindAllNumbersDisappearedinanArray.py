"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where
nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

The problem specifies that the numbers in the array will be in the range [1, n] where n is
the number of elements in the array.
Can we use this information and modify the array in-place somehow to find what we need?
"""


def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    numbers_dictionary = {}
    for i in range(1, len(nums)+1, 1):
        numbers_dictionary[i] = False

    print(numbers_dictionary)

    for el in nums:
        if el in numbers_dictionary.keys():
            numbers_dictionary[el] = True

    print(numbers_dictionary)


    #for key, value in list(numbers_dictionary.items()):
    #    if value == True:
    #        del numbers_dictionary[key]

    #print(numbers_dictionary)
    result = []
    for key in numbers_dictionary.keys():
        if numbers_dictionary[key] == False:
            result.append(key)

    print(result)

    return result

def findDifference(nums):
    L = [False] * len(nums)
    for e in nums:
        L[e - 1] = True
    Res = []
    for i in range(len(nums)):
        if not L[i]:
            Res.append(i + 1)
    return Res

def findDifferentSet(nums):

    #return list(set(range(1, len(nums) + 1)) - set(nums))
    # create the input set
    input_set = set(range(1, len(nums) + 1))
    # create the expected set
    expected_set = set(nums)
    print(input_set - expected_set)
    result = list(input_set - expected_set)
    print(result)
    #return result
    return result

if __name__ == "__main__":
    findDisappearedNumbers([1,1])
    print(findDifference([1,1,1,1]))
    print(findDifferentSet([1,1]))
