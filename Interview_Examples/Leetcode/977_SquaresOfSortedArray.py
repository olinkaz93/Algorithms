"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

def sortedSquares(nums):

        square_list = [0] * len(nums)

        left_index = 0
        right_index = len(nums) - 1

        for number in range((len(nums)-1), -1, -1):
            if (abs(nums[left_index])) > (abs(nums[right_index])):
                print(nums[left_index])
                squared_value = (nums[left_index] * nums[left_index])
                square_list[number] = squared_value
                left_index += 1
            else:
                squared_value = (nums[right_index] * nums[right_index])
                print(squared_value)
                square_list[number] = squared_value
                #print(nums[right_index])
                right_index -= 1

        return square_list

def sortedArray(nums):
    square_list = [0] * len(nums)

    left_index = 0
    right_index = len(nums) - 1
    """
    for number in range((len(nums)-1), -1, -1):

        if (abs(nums[left_index])) > (abs(nums[right_index])):
            print(nums[left_index])
            squared_value = (nums[left_index] * nums[left_index])
            square_list[number] = squared_value
            left_index += 1

        else:
            squared_value = (nums[right_index] * nums[right_index])
            print(squared_value)
            square_list[number] = squared_value
            #print(nums[right_index])
            right_index -= 1

    return square_list
    """

    # [-4,-1,0,3,10]
    # result = []
    # for el in nums: # O(n)
    #    result.append(el*el) #O(n)

    # result.sort() #O(n log n )

    # return result #O(n)

    # [-4,-1,0,3,10]

    # we initiate the result list
    result = len(nums) * [0]

    # setup the pointers
    left_pointer = 0
    right_pointer = len(nums) - 1

    # setup the index at return list
    number_of_el = len(nums) - 1
    # print(number_of_el)
    # loop through the nums and get the higher abs value

    while (left_pointer <= right_pointer):
        if abs(nums[left_pointer]) < abs(nums[right_pointer]):
            result[number_of_el] = nums[right_pointer] * nums[right_pointer]
            number_of_el -= 1
            print(number_of_el)
            right_pointer -= 1

        else:
            result[number_of_el] = nums[left_pointer] * nums[left_pointer]
            number_of_el -= 1
            left_pointer += 1

    # return the result
    return result

if __name__ == "__main__":
    nums = [3]
    result = sortedSquares(nums)
    print(result)

    print(sortedArray([-7,-3,2,3,11]))