"""
Given an array A of non-negative integers,
return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""


def sortArrayByParity(A):
    nums = A
    #we use the queue
    result = []

    if len(nums) == 1:
        return nums

    for i in range (0, len(nums), 1):
        #even number for the beginning
        if nums[i] % 2 == 0:
            result.insert(0, nums[i])
        #odd to the end
        else:
            result.append(nums[i])

    return result

def sortVersion2(nums):

    nums = nums
    left_even_pointer = 0
    right_odd_pointer = len(nums)-1

    while(left_even_pointer < right_odd_pointer):

        if (nums[left_even_pointer] % 2 != 0 and nums[right_odd_pointer] % 2 == 0):
            nums[left_even_pointer], nums[right_odd_pointer] = nums[right_odd_pointer], nums[left_even_pointer]

        if (nums[left_even_pointer] % 2 == 0):
            left_even_pointer += 1

        if (nums[right_odd_pointer] % 2 == 1):
            right_odd_pointer -= 1

    return nums

if __name__ == "__main__":

    list = [3,1,2,4]
    result = sortArrayByParity(list)
    print(result)

    list = [3, 1, 2, 4]
    result = sortVersion2(list)
    print(result)



