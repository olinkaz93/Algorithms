"SLINDING WINDOW ONLY FOR POSITIVE NUMBERS, NEGATIVE CANNOT !"
# https://www.youtube.com/watch?v=pNqL1OX7CSg

"""


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
                subarrayFound += 1

        return subarrayFound

if __name__ == "__main__":
    numbers = [1]
    print(subarraySum(numbers, 0))