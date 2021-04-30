"""
If you are setting mid = \frac{left + right}{2}mid=
2
left+right
​
 , you have to be very careful. Unless you are using a language that does not overflow such as Python, left + rightleft+right could overflow. One way to fix this is to use left + \frac{right - left}{2}left+
2
right−left
​
  instead.

If you fall into this subtle overflow bug, you are not alone. Even Jon Bentley's own implementation of binary search had this overflow bug and remained undetected for over twenty years.

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.



Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1


Constraints:

1 <= bad <= n <= 231 - 1


"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        # binary search
        low = 1
        high = n
        # X - first bad version
        mid = None

        # 1 , 2 , 3 , 4,  5
        # F   F   F   T   T

        while (low <= high):
            mid = low + (high - low) // 2
            #to avoid over flow!
            # we better use low + (high - low) // 2
            # as we substract and avoid overflow
            # the concept mid = (low + high) // 2 - make cause overflow
            print("mid", mid)
            if isBadVersion(mid) == True and isBadVersion(mid - 1) == False:
                return mid
            elif isBadVersion(mid) == False and isBadVersion(mid - 1) == False:
                low = mid + 1
            elif isBadVersion(mid) == True and isBadVersion(mid + 1) == True:
                high = mid - 1

        return -1


