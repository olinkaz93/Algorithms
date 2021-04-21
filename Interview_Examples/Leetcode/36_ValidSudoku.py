"""
Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain
the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.


create set that will gather all outputs from each element, after every iteration it will be added do set (unique collection!)
# if element has existed already, we return FALSE
https://www.youtube.com/watch?v=Pl7mMcBm2b8&t=617s

"""

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    num_of_rows = len(board)
    num_of_cols = len(board[0])

    #elements = ["1","2","3","4","5","6","7","8","9","."]
    my_set = set()
    print(my_set)
    for row in range(0, num_of_rows):

        for col in range(0, num_of_cols):

            #print(board[row][col])
            el = board[row][col]
            print("current el", el, "row", row, "col", col)
            if el != ".":
                current_el_in_row = "row: " + str(row) + " el: " + el
                current_el_in_col = "col: " + str(col) + " el: " + el
                current_el_in_box = "box " + str(row//3) + " " + str(col//3) + " el: " + el
                #print("current box", current_el_in_row)
                #print(type(current_el_in_col))
                #print(type(my_set))
                #print("my set", my_set)
                #my_set.add(current_el_in_col)
                #print(my_set)
                #for el in my_set:
                    #print("el", el, "<-")
                if (current_el_in_row in my_set) or (current_el_in_col in my_set) or (current_el_in_box in my_set):
                    return False
                else:
                    my_set.add(current_el_in_row)
                    my_set.add(current_el_in_box)
                    my_set.add(current_el_in_col)
                    print("MY SET", my_set)
    return True


                #el not in set:
                #    set.add()
            #print(type(el))

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

    result = isValidSudoku(board)
    print(result)
