"""Given an integer array nums,
move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""


def moveZeroes(nums):


    # [0,1,0,3,12]
    # we can use two pointers, which will start at the same position
    # the pointer can count the number of 0's in the list
    # having this we can find the pointer where we can will put our zeros.

    # [0,1,0,3,12]
    # we can use two pointers, which will start at the same position
    # the pointer can count the number of 0's in the list
    # having this we can find the pointer where we can will put our zeros.
    zero_counter = 0
    left_index = 0

    for number in nums:
        if number == 0:
            zero_counter += 1
        else:
            nums[left_index] = number
            left_index += 1

    # print("zeros", zero_counter)

    if (zero_counter) == len(nums):
        return nums

    for i in range(-(zero_counter), 0, 1):
        nums[i] = 0

    pointer = 0
    while pointer < len(nums):
        print(pointer)
        pointer += 1


if __name__ == "__main__":
    list1 = [0,1,0,3,12]
    result = moveZeroes(list1)
    print(result)