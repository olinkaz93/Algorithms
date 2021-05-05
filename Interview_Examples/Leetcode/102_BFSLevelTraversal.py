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

# https://www.youtube.com/watch?v=sFDNL6r5aDM&t=324s

"""
Solution

Binary Tree Level Order Traversalhttps://leetcode.com/problems/binary-tree-level-order-traversal/

Breadh First Search

Using BFS, at any instant only L1 and L1+1 nodes are in the queue.
When we start the while loop, we have L1 nodes in the queue.
for _ in range(len(q)) allows us to dequeue L1 nodes one by one and add L2 children one by one.
Time complexity: O(N). Space Complexity: O(N)
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return []

        else:

            queue = collections.deque()
            result = []

            queue.append(root)
            level = 0

            while (len(queue) > 0):
                level_size = len(queue)
                level = []
                for i in range(level_size):
                    current = queue.popleft()
                    level.append(current.val)
                    if (current.left != None):
                        queue.append(current.left)
                    if (current.right != None):
                        queue.append(current.right)
                result.append(level)

            return result