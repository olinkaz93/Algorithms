"""iven an integer array nums and an integer k,
return true if nums has a continuous subarray
of size at least two whose elements sum up to a multiple of k, or false otherwise.
An integer x is a multiple of k if there exists
an integer n such that x = n * k. 0 is always a multiple of k."""

def continuosSubarraySum(nums, k):

    #we look for the subarray which sum % k == 0
    #the size of the subarray must be >= 0

    #so if sum % k == 0
    # (s1-s2)%k == 0
    # s1%k = s2%k
    #so we look for the both sum%k which value is equal
    # we will loop through the array from the very beginning and update it with the sum%k value , according to the pointer
    # [0, 1, 2, 3, 4]
    #        s2
    #               s1
    #           ______ = s
    #we add the {0; -1} value, as if we find the value which is %k == 0 starting from the very beginning

    dictionary_of_mod = {0: -1}
    right_pointer = 0
    current_sum = 0
    #result = None

    for right_pointer in range (0, len(nums), 1):
        print(dictionary_of_mod)
        current_sum += nums[right_pointer]

        if k != 0:
            current_sum_mod = current_sum % k

        if current_sum_mod in dictionary_of_mod:
            if right_pointer - dictionary_of_mod[current_sum_mod] >= 2:
                return True

        else:
            dictionary_of_mod[current_sum_mod] = right_pointer

    return False





if __name__ == "__main__":
    numbers = [0,1,2,3,4,5]
    k = 7
    result = continuosSubarraySum(numbers, k)
    print(result)