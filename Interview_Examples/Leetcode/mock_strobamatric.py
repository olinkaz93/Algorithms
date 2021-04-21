"""
Given a string num which represents an integer,
return true if num is a strobogrammatic number.
A strobogrammatic number is a number that
looks the same when rotated 180 degrees (looked at upside down).

Example 1:
Input: num = "69"
Output: true

Example 2:
Input: num = "88"
Output: true

Example 3:
Input: num = "962"
Output: false

Example 4:
Input: num = "1"
Output: true

Constraints:

1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.
"""


def isStrobogrammatic(nums):
    """
    :type num: str
    :rtype: bool
    """

    if len(nums) == 0:
        return False

    if len(nums) == 1 and (nums[0] == "1" or nums[0] == "6" or nums[0] == "9" or nums == "8" or nums == "0"):
        return True
    elif len(nums) == 1:
        return False

    left_pointer = 0
    right_pointer = len(nums) - 1

    while (left_pointer <= right_pointer):

        if (nums[left_pointer] == "8") and (nums[right_pointer] == "8"):
            left_pointer += 1
            right_pointer -= 1
        elif (nums[left_pointer] == "0") and (nums[right_pointer] == "0"):
            left_pointer += 1
            right_pointer -= 1
        elif (nums[left_pointer] == "1") and (nums[right_pointer] == "1"):
            left_pointer += 1
            right_pointer -= 1
        elif (nums[left_pointer] == "6") and (nums[right_pointer] == "9"):
            left_pointer += 1
            right_pointer -= 1
        elif (nums[left_pointer] == "9") and (nums[right_pointer] == "6"):
            left_pointer += 1
            right_pointer -= 1
        else:
            return False
    return True

if __name__ == "__main__":
    print(isStrobogrammatic("0"))
    print(isStrobogrammatic("1"))
    print(isStrobogrammatic("6"))
    print(isStrobogrammatic("9"))
    print(isStrobogrammatic("8"))
    print(isStrobogrammatic("4"))
    print(isStrobogrammatic("88"))
    print(isStrobogrammatic("88888"))

