"""
Given an integer numRows,
return the first numRows of Pascal's triangle.

In Pascal's triangle,
each number is the sum of
the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
https://www.youtube.com/watch?v=icoql2WKmbA
"""

def pascalTriangle(n):

    triangle = []
    #row = []
    first_row = [1]
    triangle.append(first_row)
    print(triangle[0])
    #first element in row always = 1 , row[0] = 1
    #the last element in row always = 1, row[-1] = 1
    print(triangle)
    for row in range(1, n):
        #print(type(row), "row", row)
        current_row = []
        previous_index = row - 1
        print("prev", previous_index)
        previous_row = triangle[previous_index]
        #print(previous_row)
        current_row.append(1)
        for i in range (1, row, 1):
            current_row.append(previous_row[i-1]+previous_row[i])
        current_row.append(1)
        triangle.append(current_row)

    print(triangle)
    print(n)
    return triangle

if __name__ == "__main__":


    result = pascalTriangle(6)
    print(result)