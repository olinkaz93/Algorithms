"SLINDING WINDOW ONLY FOR POSITIVE NUMBERS, NEGATIVE CANNOT !"
# https://www.youtube.com/watch?v=pNqL1OX7CSg


"""
 Further, for every sum encountered, we also determine the number of times the sum sum-ksum−k has occurred already, since it will determine the number of times a subarray with sum kk has occurred up to the current index. We increment the countcount by the same amount.

After the complete array has been traversed, the countcount gives the required result.

The animation below depicts the process.

"""


def subarraySum(self, nums, k):
    # two pointers wont work, as we may have negatives!
    # we look for the number of subarrays, which total values, will be number of K

    # 1) First approach, slow, we iterate by every element

    # 2) Keep the HASH MAP, and we will keep the CUMULATIVE SUM
    # We loop thorugh the numbers, and we store the sums in the ditionary
    # THINK ABOUT SUBSTRACTION, of the
    # ongoing sums, frequency and indices
    # have we seen the sum SUM - K before?
    # We create the DICT of sums, with the "SUM" : 'frequency of them'
    # we can have negatives,
    # [3, 1, 1, 1, -1]
    # -so we see sums
    """
    s1 = 3
    s2 = 4
    s3 = 5
    s4 = 6
    s5 = 5, again s5=s3, so we adjust the dict value
    #when we see the sums already we can add

    having the sums stored in the dictionary,
    then we loop from the left and see weather THIS X + Y = SUM

    Hashmap with the sums how many times was seen

    K = Sum1 + Sum2
    so we can iterate and check the sums
    if we have seen the SUM2 before that means we got a subarray

    Sum2 = K - SUM

    """

    # since  K = SUM1 + SUM2
    # we store SUMS1 in the array, and then check whether we have them in dictionary already

    dictionary = {}
    dictionary[0] = 1

    # nums = [1,2,3], k = 3

    result = 0
    summ = 0

    for i in range(0, len(nums), 1):

        summ += nums[i]
        # print(summ)

        if (summ - k) in dictionary:
            result += dictionary[summ - k]
        # print("result", result)
        if summ in dictionary:
            dictionary[summ] += 1
        else:
            dictionary[summ] = 1

        # print(dictionary)
    return result

if __name__ == "__main__":
    numbers = [1]
    print(subarraySum(numbers, 0))