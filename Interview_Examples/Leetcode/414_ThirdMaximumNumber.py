"""
Given integer array nums,
return the third maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""
def printMax(nums):
    maximum = float('-inf')
    second_max = float('-inf')
    third_max = float('-inf')
    for el in nums:
        if el > maximum:
            third_max = second_max
            second_max = maximum
            maximum = el
        elif el > second_max and el < maximum:
            third_max = second_max
            second_max = el
        elif el < maximum and el < second_max and el > third_max:
            third_max = el
        #elif el > maximum:
        #    third_max = second_max
        #    second_max = maximum
        #    maximum = el

    if third_max == float('-inf'):
        return maximum
    else:
        return third_max



if __name__ == "__main__":
    print(printMax([3,2,1]))

