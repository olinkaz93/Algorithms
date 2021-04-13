"""
In a given integer array nums,
there is always exactly one largest element.
Find whether the largest element in the array
is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

"""
def dominantIndex(nums):

    if len(nums) == 1:
        return 0
    max_value = max(nums)

    second_array = []
    for number in nums:
        if number == max_value:
            continue
        else:
            second_array.append(number)
    second_max = max(second_array)

    #print(second_array)
    #print(second_max)
    if max_value >= (2*second_max):
        return nums.index(max_value)

    else:
        return -1

if __name__ == "__main__":
    list = [9, 8, 4, 2, 3]
    print(dominantIndex(list))