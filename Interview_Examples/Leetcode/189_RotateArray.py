"""
Given an array, rotate the array to the right by k steps, where k is non-negative.


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

"""
input_list = [1,2,3,4,5]
k = 2
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return nums
        if k == 0:
            return nums


        else:
            rotation = k % len(nums)
            print(rotation)
            #[1,2,9,0]
            #[0,1,2,9]
            #[9,0,1,2]
            #[2,9,0,1]
            nums = nums[rotation+3:] + nums[:rotation+1]
            return nums


if __name__ == "__main__":

    solution = Solution()
    result = solution.rotate([1,2,9,0], 3)
    print(result)
