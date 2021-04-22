"""
Given an array of numbers arr.
A sequence of numbers is called an arithmetic
progression if the difference between any two consecutive elements is the same.
Return true if the array can be
rearranged to form an arithmetic progression, otherwise, return false.

Example 1:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

Constraints:

2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6

"""


def canMakeArithmeticProgression(array):
    """
    :type arr: List[int]
    :rtype: bool
    """
    if (len(arr)) < 2:
        return False

    arr.sort()

    # for i in range(len(arr) - 2):
    #	if arr[i + 2] - arr[i + 1] != arr[i + 1] - arr[i]:
    #		return False

    # return True

    # second_pointer = 1
    # first_pointer = 0

    difference = abs(arr[1] - arr[0])

    for index in range(2, len(arr), 1):
        if (abs(arr[index] - arr[index - 1])) != difference:
            return False
    return True

if __name__ == "__main__":
    arr = [1,3,2,-9,4,50]
    print(canMakeArithmeticProgression(arr))

