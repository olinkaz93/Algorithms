"""
Given an integer array nums and an integer k,
return true if nums has a continuous subarray
of size at least two whose elements sum up to a multiple of k, or false otherwise.
An integer x is a multiple of k if there exists
an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false

https://www.youtube.com/watch?v=wsTcByj8QbI
"""


def checkSubarraySum(nums, k):
       
        cumsum, left = 0, -1
        lookup = {cumsum: left}

        for right, val in enumerate(nums):

            cumsum += val

            if k != 0:
                cumsum %= k

            if cumsum in lookup:
                left = lookup[cumsum]
                if right - left >= 2:
                    return True
            else:
                lookup[cumsum] = right

        return False


"""
def checkSubarraySum(nums, k):
    
 
    #we store the modeulo fo the sum, since

    #       |  | S = S1 - S2
    # 0 1 2 3 4

    # S1 = (0+1+2+3+4) = 10

    # S2 = (0 + 1 + 2) = 3

    # S = S1 - S2 | %K
    # S%k = (s1 - s2) %k
    #( 0 ==) S%k = s1%k - s2%k
    # 0 = S1%k - S2%k
    # S1%k = S2%k
    # so wee need to store the dictionary of the mod current sum accordingly to the index position
    # if we find the sum which (S1%k) = (S2%k) - means we have seen the same sum%k before, and if length >= 2
    # we found the True subarray
    # we keep also the extra edge case {0: -1} for the sake if we find the value which sum ups to %k,
    #in the iteration from the very first index ,

    modulo_sum_dictionary = {0: -1}

    for right_pointer in range(0, len(nums), 1):

        curr_sum += nums[right_pointer]
        curr_length = right_pointer - left_pointer + 1
        if (k != 0):
            curr_sum_mod = curr_sum % k
        print(curr_sum, "length", curr_length)
        while (curr_length >= 2):

            if (curr_sum_mod) in modulo_sum_dictionary:
                return True
            else:
                curr_sum = curr_sum - nums[left_pointer]
                curr_sum_mod = curr_sum % k
                curr_length = right_pointer - left_pointer + 1
                print("ooo",curr_sum, curr_sum_mod, curr_length)

        else:
            modulo_sum_dictionary[curr_sum_mod] = right_pointer

                #curr_sum -= nums[left_pointer]
                #curr_length = right_pointer - left_pointer + 1
                #print(curr_sum, "->length", curr_length)
                #left_pointer += 1
    return False

    # return true if nums
    # has a continuous subarray
    # of size at least two whose | curr_length >= 2
    # elements sum up to a multiple of k, or false otherwise.
    
    """


if __name__ == "__main__":
    input = [23,2,0,4,7]
    result = checkSubarraySum(input, 11)
    print(result)