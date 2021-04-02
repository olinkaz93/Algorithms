"""
Given an array of integers nums and an integer k,
return the total number of continuous subarrays whose sum equals to k.
https://leetcode.com/problems/subarray-sum-equals-k/
"""

def findSubarray(nums, k):
    nums = nums
    k = k
    subarray_found = 0

    if (len(nums) == 0):
        return subarray_found

    else:
        #subarray_sum = 0
        length_of_nums = len(nums)

        for i in range (0, length_of_nums, 1):
            subarray_sum = 0
            start_element_of_subarray = nums[i]
            print("first element of the subarray:", start_element_of_subarray)
            #subarray_sum += start_element_of_subarray
            print("subarray from index:", i)
            if start_element_of_subarray == k:
                subarray_found += 1
                continue
            else:
                # min i = 0, max i = 9
                # 10 elements in array/list, last index is 9 (len(list)-1)
                # [ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ]
                while (subarray_sum < k and i <= length_of_nums - 1):
                    element_to_add = nums[i]
                    subarray_sum += element_to_add
                    print("current sum after adding:", subarray_sum)
                    i = i + 1
                    if subarray_sum == k:
                        subarray_found += 1

        return subarray_found


if __name__ == "__main__":

    result = findSubarray([1,0,0,0,1,2], 1)
    print("*****************************************")
    print("*****number of subarrays:", result)

