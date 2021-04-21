

def wiggleSort(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    previous_pointer = 0
    # next_pointer = 1

    for next_pointer in range(1, len(nums), 1):
        if previous_pointer % 2 == 0 and nums[previous_pointer] <= nums[next_pointer]:
            previous_pointer += 1
            next_pointer += 1
        elif previous_pointer % 2 == 0 and nums[previous_pointer] > nums[next_pointer]:
            print("prev", nums[previous_pointer])
            nums[previous_pointer], nums[next_pointer] = nums[next_pointer], nums[previous_pointer]
            previous_pointer += 1
            next_pointer += 1
            print("previous", previous_pointer)
            print("next", next_pointer)
        elif previous_pointer % 2 == 1 and nums[previous_pointer] >= nums[next_pointer]:
            previous_pointer += 1
            next_pointer += 1
        elif previous_pointer % 2 == 1 and nums[previous_pointer] < nums[next_pointer]:
            print("prev", nums[previous_pointer])
            nums[previous_pointer], nums[next_pointer] = nums[next_pointer], nums[previous_pointer]
            previous_pointer += 1
            next_pointer += 1
            print("previous", previous_pointer)
            print("next", next_pointer)
    return nums

if __name__ == "__main__":
    print(wiggleSort([3,5,2,1,6,4]))