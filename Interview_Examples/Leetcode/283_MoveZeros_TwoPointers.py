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

    reader_pointer = 0
    writer_pointer = 0
    total_zeros = 0

    nums = nums

    for reader_pointer in range(0, len(nums), 1):
        if nums[reader_pointer] == 0:
            total_zeros += 1
        else:
            nums[writer_pointer] = nums[reader_pointer]
            writer_pointer += 1

    while (total_zeros > 0):
        nums[writer_pointer] = 0
        writer_pointer += 1
        total_zeros -= 1

    return nums



if __name__ == "__main__":
    list1 = [0,1,0,3,12]
    result = moveZeroes(list1)
    print(result)