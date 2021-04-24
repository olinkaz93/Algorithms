"""

Bracket Match
Notice that a string of matching brackets is a string that follows these rules:

the number of '(' and the number of ')' are equal i.e. every open bracket is matched with a closing bracket.
There cannot be a closing bracket before an opening bracket, i.e. in every prefix of the string, the number of '(' is equal or greater than the number of ')'. For example:
the string “(()” is incorrect because there is an extra '(' that isn’t matched with a ')' - it doesn’t follow first rule.
The string “)(“ is incorrect because although it has an equal number of '(' and ')', the prefix “)” of the string has more ')' than '(' - it doesn’t follow the second rule. To check how many brackets we need to add an existing string, we need to keep track of the number of '(' and the number of ')', or more accurately the difference between the number of '(' and the number of ')'. We iterate through the string, and count the difference between the open and close brackets, if at some point there are more ')' than '(', it means that to fix the string, we must add an '(' somewhere before the current position (for example, the beginning of the string). Thus, in our algorithm we’ll add 1 to the answer and also increment the number of '(' by one in our difference counter. This promises the second rule is correct in our string.
To make sure the first rule is correct, we simply take the difference between the '(' and the ')' in the text, and add it to the answer, since at the end of the string if the number isn’t equal, we’ll simply add ')' to the end of the text (or '(' to the beginning).

Pseudocode:

function bracketMatch(text):
    diffCounter = 0
    ans = 0
    n = text.length

    for i from 0 to n-1:
        if ( text[i] == '(' ):
            diffCounter += 1
        else if ( text[i] == ')' ):
            diffCounter -= 1
        if ( diffCounter < 0 ):
            diffCounter += 1
            ans += 1

    return ans + diffCounter
For example, consider running the “()))(“:

i - # of iteration	text[i]	ans	diffCounter	Suggested fix
1	()))(	0	1	()))(
2	()))(	0	0	()))(
3 (a)	()))(	0	-1	()))(
3 (b)	()))(	1	0	(()))(
4 (a)	()))(	1	-1	(()))(
4 (b)	()))(	2	0	((()))(
5 (a)	()))(	2	1	((()))(
5 (b)	()))(	3	1	((()))()
Notes:

Steps that are divided to ‘a’ and ‘b’ are steps where we modify ans and diffCounter.
The suggested fix is not actually in the code, since we only need the number of brackets.
Time Complexity: O(N), where N is the length of text. We go through every character of text and for every character we carry out a constant number of steps.

Space Complexity: O(1) since we only used a constant amount of space throughout the algorithm.

"""

def num_of_paths_to_dest(n):
  pass # your code goes here

number_col = n
number_row = n


# input: n - a positive integer representing the grid size.
# output: number of valid paths from (0,0) to (n-1,n-1).

function numOfPathsToDest(n):
    # allocate a 2D array for memoization
    memo = [][]

    # the memoization array is initialized with -1
    # to indicate uncalculated squares.
    for i from 0 to n-1:
        for j from 0 to n-1:
            memo[i][j] = -1

    return numOfPathsToSquare(n-1, n-1, memo)


# input:
#    i, j - a pair of non-negative integer coordinates
#    memo - a 2D memoization array.
# output:
#    number of paths from (0,0) to the square represented in (i,j),

function numOfPathsToSquare(i, j, memo):
    if (i < 0 OR j < 0):
        return 0
    else if (i < j):
        memo[i][j] = 0
    else if (memo[i][j] != -1):
        return memo[i][j]
    else if (i == 0 AND j == 0):
        memo[i][j] = 1
    else:
        memo[i][j] = numOfPathsToSquare(i, j -1, memo) +
        numOfPathsToSquare(i - 1, j, memo)

    return memo[i][j]

# 6x6
x x x x x 0
x x x x 0 0       N
x x x 0 0 0       |
x x 0 0 0 0     W---E
x 1 0 D 0 0       |
S 1 0 0 0 0       S


S -> (EEEN) (EENE) (ENEE)

# 1x1 => ways = 1
1

# 2x2 => ways = 1
x 1
1 1

# 3x3 => ways = 2
x x 2
x 1 2
1 1 1

# 4x4 =>

x x x 5
x x 2 5
x 1 2 3
1 1 1 1


x x x 0
x x 0 0
x 0 0 0
0 0 0 0

n = 1
x

n = 2
x 1
1 1

n = 3 #every box is a destination itself
x x 2
x 1 2
1 1 1

x x x 0
x x 0 0
x 0 0 0
1 0 0 0






