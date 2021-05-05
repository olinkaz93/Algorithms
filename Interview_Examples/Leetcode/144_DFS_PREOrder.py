# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def helperDfs(self, root, result):
        # PREORDER traversal, so we PRINT visit ROOT node and then its left , right child
        if root == None:
            return
        result.append(root.val)
        self.helperDfs(root.left, result)
        self.helperDfs(root.right, result)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.helperDfs(root, output)
        return output