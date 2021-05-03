# https://www.youtube.com/watch?v=VM1kmLrrN4Y

# MaxConsecutiveSum, k

"""
1)We loop through the array
when we have the very first sum
2) Then we need to go shirnk and adjust the window once we hit the tsum

"""

def maxConsecutiveSum(nums, k):

    if (len(nums)) < k:
        return None

    right_pointer = 0
    left_pointer = 0
    # [5,1,3,7,9,0,3], k = 3
    #  R
    #  L
    summ = 0
    #maxsum = float('-inf')
    for right_pointer in range(0, k):
        summ += nums[right_pointer]
    # [5,1,3,7,9,0,3], k = 3, sum = 9
    #      R
    #  L
    maxsum = summ

    # [5,1,3,7,9,0,3], k = 3
    #      R
    # summ = 5+1+3 = 9
    # maxsum = summ

    right_pointer += 1

    # [5,1,3,7,9,0,3], k = 3
    #  L     R
    # summ = 5+1+3+7-5 = 11
    # maxsum = summ

    print("sum", summ)
    while(right_pointer < len(nums)):
        print("Right", right_pointer)
        print("left", left_pointer)
        summ += nums[right_pointer]
        summ -= nums[left_pointer]
        print("summm", summ)
        if summ > maxsum:
            maxsum = summ
        left_pointer += 1
        right_pointer += 1

    return maxsum


def maxSumCons(nums, k):

    maxsum = float("-inf")
    right = 0
    left = 0
    summ = 0

    #we loop and add right/end value pointers to the sum
    for right in range(len(nums)):
        summ += nums[right]

        #if the length (right - left + 1) is == k ,
        if right - left + 1 == k:
            #we check the maxsum
            max(maxsum, summ)
            #and srhink the value by nums[left] and move it +1
            summ -= nums[left]
            left += 1
    return maxsum


if __name__ == "__main__":
    #print(maxConsecutiveSum([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))
    print(maxSumCons([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))
