"""
Given an integer array nums,
find the contiguous subarray
(containing at least one number)
which has the largest sum and return its sum.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
https://youtu.be/5WZl3MMT0Eg
"""


def subarraySum(nums, k):
    subarrayFound = 0

    if (len(nums) == 1):
        if nums[0] == k:
            return 1
        else:
            return 0

    else:
        subarraySum = 0
        subarray_index_start = 0

        for i in range(0, len(nums), 1):

            # currentEl = nums[i]

            subarraySum += nums[i]
            print(subarraySum)

            while (subarraySum > k):

                subarraySum -= nums[subarray_index_start]
                subarray_index_start += 1
            
            if subarraySum == k:
                print("sum", subarraySum, "index", i, "start", subarray_index_start)
                subarrayFound +=1

        return subarrayFound

if __name__ == "__main__":
    result = subarraySum([-1, -1, 1], 0)
    print(result)