# https://www.youtube.com/watch?v=sFDNL6r5aDM

"""
102. Binary Tree Level Order Traversal
Medium

4610

106

Add to List

Share
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if (root == []):
            return []

        else:

            queue = collections.deque()
            result = []

            queue.append(root)
            #level = 0



            while (len(queue) != 0):
                level_size = len(queue)
                level = []
                #we need to create new empty array for each level, once we start to get thorugh the queue
                #then itarate, add those elements
                for i in range(0, level_size, 1):
                    current = queue.popleft()
                    level.append(current.val)
                    if (current.left != None):
                        queue.append(current.left)
                    if (current.right != None):
                        queue.append(current.right)
                result.append(level)

            return result