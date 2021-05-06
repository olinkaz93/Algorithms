# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://www.youtube.com/watch?v=12omz-VAyRk

class Solution(object):
    # we got sorted array
    # we convert it into BINARY SEARCH TREE
    # hegight - balanced so we have at most diff of 1 level

    # leftside elements are lower than PARENT
    # rightside elements are higher than PARENT

    # in sorted array, WHEN YOU SEE BINARY SEARCH !!

    # find THE ROOT, MID ELEMENT

    def sortedArrayToBST(self, nums):

        if (len(nums) == 0):
            return None

        return self.constructTree(nums, 0, len(nums) - 1)

    def constructTree(self, nums, low, high):

        if (low > high):
            return None

        mid = low + (high - low) // 2
        # we get the mid value, we make the root
        node = TreeNode(nums[mid])
        node.left = self.constructTree(nums, low, mid - 1)
        node.right = self.constructTree(nums, mid + 1, high)

        return node





