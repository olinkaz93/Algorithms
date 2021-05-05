"""
94. Binary Tree Inorder Traversal

Add to List

Share
Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100




"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    iNorder Traversal Printing.


    def inorderTraversal(self, root):

        if root is None:
            return

        if root.left != None:
            self.inorderTraversal(root.left)
        print(root.val)
        if root.right != None:
            self.inorderTraversal(root.right)
    """

    def helper(self, root, res):
        if root == None:
            return

        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

    def inorderTraversal(self, root):
        res = []

        self.helper(root, res)

        return res
