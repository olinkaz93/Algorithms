#Given an array of integers nums and an integer target,
#return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution,
#and you may not use the same element twice.
#You can return the answer in any order.

"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

"""
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

#so having the target sum, we can loop thorugh the given list,
# and see which elements, values from the list are sum of the target sum

#list_numbers = [1, 2, 3, 4, 6]

# we could have two nested loops, but this won't be efficient, and having high complexity,
# the good approach would be try to access the numbers from the beginning and from the end at the same time
# and check if we find the elements of sum

# we can deduct one element from the sum, and check with the function if we see element that is the rest of the sum

# e.g. having 9, first element of the list is 1, we check weather there is "8" in the list and find the index

def find_numbers(list_of_numbers, tar_sum):


    #index_of_number1 = 0
    #index_of_number2 = None
    target = tar_sum
    length_of_list = len(list_of_numbers)

    #first_number + second_number = tar_sum

    for index_of_number1 in range (0, length_of_list, 1):
        first_number = list_of_numbers[index_of_number1]
        print("index of number 1:", index_of_number1, " value of number 1:", first_number)
        second_number = tar_sum - first_number

        if second_number in list_of_numbers and list_of_numbers.index(second_number) != index_of_number1:
            index_of_number2 = list_of_numbers.index(second_number)
            print("value of second", second_number,"index of number 2", index_of_number2)
            break

    indexes_of_numbers = []
    indexes_of_numbers.append(index_of_number1)
    indexes_of_numbers.append(index_of_number2)
    return indexes_of_numbers

nums = [3, 20, 4, 6, 10]
target = 30
output = find_numbers(nums, target)
print(output)

"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

"""
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

