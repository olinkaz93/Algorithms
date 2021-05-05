# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def helperDFS(self, root, output):
        if root == None:
            return

        self.helperDFS(root.left, output)
        self.helperDFS(root.right, output)
        output.append(root.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        output = []

        self.helperDFS(root, output)

        return output