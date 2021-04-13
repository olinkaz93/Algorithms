"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

"""


def findMaxConsecutiveOnes(nums):

    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) == 1 and nums[0] == 1:
        return 1
    if len(nums) == 1 and nums[0] == 0:
        return 0

    max_ones = 0
    # Input: nums = [1,1,0,1,1,1]
    # Output: 3

    for index in range(0, len(nums), 1):
        #print("max_ones", )
        if nums[index] == 1:

            #print(index)
            start_pointer = index
            sum_of_ones = 1

            if (sum_of_ones > max_ones):
                max_ones = sum_of_ones

            next_pointer = start_pointer + 1
            #print("start", start_pointer)
            #print("next", next_pointer)

            while next_pointer != len(nums) - 1 and nums[next_pointer] == 1:
                sum_of_ones += 1
                if (sum_of_ones > max_ones):
                    max_ones = sum_of_ones
                    #print("max ones", max_ones)
                next_pointer += 1

    return max_ones


if __name__ == "__main__":
    result = findMaxConsecutiveOnes([1,1,1,0,1,1,1,1,1,0])
    print(result)