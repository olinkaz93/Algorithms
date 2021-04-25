"""
Given an integer array nums and an integer k,
return true if there are two distinct indices
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105


Excellent questions! You are right, if you push it into the hashmap,
the old key-value pair with the same key will be overridden.

Code is correct since you only need to do the check with the current
and last index (if this is false then
all the previous indices must also be false since the distance to them is greater).

"""


def containsNearbyDuplicate(nums, k):
    if len(nums) == 0:
        return False

    dictionary_of_nums = {}
    # adding new value will overwrite the current value if we make so
    # hence that we do not need to use slidning window or so
    # the distance before the previous element vs. current shall be already                  bigger or smaller

    for i in range(0, len(nums), 1):
        number = nums[i]
        if number in dictionary_of_nums:
            distance = i - dictionary_of_nums[number]
            if (abs(distance <= k)):
                return True
            dictionary_of_nums[number] = i
        else:
            dictionary_of_nums[number] = i
            #print(dictionary_of_nums)
    print(dictionary_of_nums)
    return False

def containDuplicate(nums, k):


    start_pointer = 0
    # end_pointer = 0
    for start_pointer in range(0, len(nums), 1):
        next_pointer = start_pointer + 1
        while (next_pointer < len(nums) and next_pointer - start_pointer <= k):
            element = nums[start_pointer]
            if element == nums[next_pointer]:
                return True
            next_pointer += 1
            start_pointer += 1

    return False


if __name__ == "__main__":
    print(containsNearbyDuplicate([1,0,1,1,2], 1))
    print(containDuplicate([1, 1, 0, 0, 1], 3))