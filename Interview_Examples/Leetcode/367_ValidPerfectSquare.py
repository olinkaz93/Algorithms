def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """

    # similar to LETTCODE.69

    low = 1
    high = num

    # we perform binary search, to check whether we can find a perfect mid*mid value

    result = False

    while (low <= high):

        mid = low + (high - low) // 2
        if (mid * mid == num):
            return True
        # if element is higher than the target X, we must decreade the HIGH boundry

        elif (mid > num / mid):
            high = mid - 1
        else:
            low = mid + 1

    return result