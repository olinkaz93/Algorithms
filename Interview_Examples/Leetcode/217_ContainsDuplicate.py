"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

#we get the list of the numbers, and we can loop through the list, making a hash map/dictionary, that will store the
number and whether the number will be duplicate we will increase it, and return True

we can use the set, as it keeps the unique values, and if is not gonna be unique we return True otherwsie is false
"""


def containsDuplicate(nums):

    set_of_numbers = set()

    for number in nums:
        if number not in set_of_numbers:
            set_of_numbers.add(number)
        else:
            return True

    return False
###
def containsDuplicate2(nums):

    print("hello", nums)
    nums.sort()

    for index in range(0, len(nums)-1, 1):
        if nums[index] == nums[index+1]:
            return True
        else:
            False


if __name__ == "__main__":
    list1 = [1,2,3,1] #true
    list2 = [1,1,1,3,3,4,3,2,4,2] #true
    list3 = [1,2,3,4] #false
    #print(containsDuplicate(list1))

    result = containsDuplicate2(list2)
    print(result)