"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false

"""


def isHappy(n):
    if n == 0:
        return False
    if n == 1:
        return True

    set_number = set()

    while (n != 1):
        sums = 0
        current_number = n
        while (current_number != 0):
            digit = current_number % 10
            sums += digit * digit
            current_number = current_number // 10

        if sums in set_number:
            return False
        else:
            set_number.add(sums)
            n = sums
    return True

def isHappy2(num):

    if num == 1:
        return True

    current_number = num
    num_set = set ()
    while current_number != 1:
        sum = 0
        current_el = current_number
        while current_el != 0:
            digit = current_el % 10
            sum += digit * digit
            current_el = current_el // 10

        if sum not in num_set:
            num_set.add(sum)
            current_number = sum
        else:
            return False
    return True


if __name__ == "__main__":

    print(isHappy2(1000000001))



