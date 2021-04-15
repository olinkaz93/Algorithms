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

    #
    squared_values = []
    if len(nums) == 1:
        squared_values.append(nums[0]*nums[0])
    elif nums[0] <= 0 and nums[-1] <= 0:
        for index in range(len(nums)-1, -1, -1):
            squared_values.append(nums[index]*nums[index])
    elif nums[0] >= 0 and nums[-1] >= 0:
        for index in range(0, len(nums), 1):
            squared_values.append(nums[index] * nums[index])
    else:


    return squared_values

if __name__ == "__main__":
    nums = [3]
    result = sortedSquares(nums)
    print(result)