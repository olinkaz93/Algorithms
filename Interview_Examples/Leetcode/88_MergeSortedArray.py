"""
Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1
has a size equal to m + n such that
it has enough space to hold additional elements from nums2.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
"""

def merge(nums1, m, nums2, n):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1_copy = nums1[:m]

        # pointer_of_result = 0
        pointer1 = 0
        pointer2 = 0

        for pointer in range(n + m):
            print(pointer)
            if (nums1_copy[pointer1] < nums2[pointer2] and pointer1 < n) or pointer2 >= m:
                nums1_copy[pointer] = nums1[pointer1]
                print(nums1_copy[pointer], nums1[pointer1])
                pointer1 += 1

            else:
                nums1[pointer] = nums2[pointer2]
                pointer2 += 1



if __name__ == "__main__":

    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 2



