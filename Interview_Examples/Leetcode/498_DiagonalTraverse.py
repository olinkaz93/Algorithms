"""
Given an m x n matrix mat,
return an array of all
the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105

https://www.youtube.com/watch?v=0DnG0Kc9M2E !!!



"""


def findDiagonalOrder(matrix):
    #if not matrix or not matrix[0]:
    #   return []

    num_rows, num_cols = len(matrix), len(matrix[0])
    diagonals = [[] for _ in range(num_rows + num_cols - 1)]

    for i in range(num_rows):
        for j in range(num_cols):
            diagonals[i + j].append(matrix[i][j])

    res = diagonals[0]

    for x in range(1, len(diagonals)):
        if x % 2 == 1:
            res.extend(diagonals[x])
        else:
            res.extend(diagonals[x][::-1])

    return res

if __name__ == "__main__":
    print(findDiagonalOrder([[1,2],[3,4]]))
