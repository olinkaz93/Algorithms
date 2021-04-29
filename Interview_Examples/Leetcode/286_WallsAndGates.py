"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.



Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
Example 3:

Input: rooms = [[2147483647]]
Output: [[2147483647]]
Example 4:

Input: rooms = [[0]]
Output: [[0]]


Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
Accepted

"""


class Solution(object):
    def wallsAndGates(self, grid):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        """
        We should find the route for each empty cell

        We need to update -INF

        We make BFS for all possible rooms, we

        1) Identify the rooms, and mark them one by one and increment ,

        Time MxN we visit all of them. And Space complexity is MxN

        """

        if grid == None or grid[0] == None:
            return None

        # 1) Store the grid
        rows = len(grid)
        cols = len(grid[0])

        # 2) Allocate the gates and put into the queue
        # gates = []
        queue = collections.deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    # we use tuple as we do not want values to be changed
                    queue.append((row, col))

        print(queue)

        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # 3) We take the element from the queue, mark it as seen and check neighbours

        while queue:
            current_row, current_col = queue.popleft()
            print(current_row)
            print(current_col)
            for x, y in dirs:
                new_row = current_row + x
                new_col = current_col + y

                if 0 <= new_row and new_row < len(grid) and 0 <= new_col and new_col < len(grid[0]) and grid[new_row][new_row] == 2147483647:
                    grid[new_row][new_col] = grid[current_row][current_col] + 1
                    queue.append((new_row, new_col))




