"""
Given an m x n matrix, return all elements of the matrix in spiral order.


Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
Accepted


https://www.youtube.com/watch?v=BdQ2AkaTgOA
https://www.youtube.com/watch?v=uYgoo8BdUAAv
"""
"""
         [[1,2,3],
matrix = [4,5,6],
         [7,8,9]]
"""
def spiralMatrix(matrix):

    if len(matrix) == 0 or len(matrix[0]) == 0 or matrix == None:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    # each iteration we need to check the current size of inserted elements
    # so we will loop while len(result) < size_of_matrix

    top = 0
    right = len(matrix[0]) - 1
    bottom = len(matrix) - 1
    left = 0
    size_of_matrix = rows * cols

    # print(size_of_matrix)

    while (len(result) < size_of_matrix):
        if (len(result) < size_of_matrix):
            for i in range(left, right + 1, 1):
                result.append(matrix[top][i])
                print(matrix[top][i])
            top += 1
        if (len(result) < size_of_matrix):
            for i in range(top, bottom + 1, 1):
                result.append(matrix[i][right])
            right -= 1
        if (len(result) < size_of_matrix):
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if (len(result) < size_of_matrix):
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


if __name__ == "__main__":
    print(spiralMatrix([[1,2,3],[4,5,6],[7,8,9]]))