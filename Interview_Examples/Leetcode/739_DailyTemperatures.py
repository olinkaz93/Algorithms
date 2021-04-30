"""

Given a list of daily temperatures T,
return a list such that, for each day in the input,
tells you how many days you would have to
wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures
T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].

"""


def dailyTemperatures(T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    """
    T = [73, 74, 75, 71, 69, 72, 76, 73]

    output       [1, 1, 4, 2, 1, 1, 0, 0]
    """

    """
    We can use stack
    put every element when we traverse the Temperatures,
    if we find a value higher than current value at the peek, 
    we can remove it, and add differences of the indices at the reuslt


    """

    """
    T = [73, 74, 75, 71, 69, 72, 76, 73]

    output [1, 1, 4, 2, 1, 1, 0, 0]
    """

    # We can treat T[] as a list of temperatures, we will loop trough them
    # and keep track of current MAX temperatures in the stack
    # we will add on top of them the elements, once we find a new MAX, we will
    # append a result o diffference of temeperatures to the result
    # which has the 'i' of the days, so we store t[imax] - t [i]

    if len(T) == 0:
        return []
    if len(T) == 1:
        return [0]

    stack_max = []  # in stack_max we keep the indices of current max T[i]
    result = [0] * len(T)

    for i in range(0, len(T), 1):
        while (stack_max and T[i] > T[stack_max[-1]]):
            current_max = stack_max.pop()
            # we calculate days of difference so for T[0] = 73, T[1] = 74
            result[current_max] = i - current_max
        stack_max.append(i)

    return result