"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""
#we should have the even number of length of string
# ()(){}{[]}
#classic stack problem exercise
#once we see the opening brackets ( { [, these are put to the stack
#whenever we see the closing cracket ) } ], we must see if that is matching the very first element from the stack,
#to remember that STACK is LIFO Last In First Out


def isValid(string):

    if (len(string)%2 != 0):
        return False

    stack_of_paranteses = []

    for char in string:
        if char == "(" or char == "[" or char == "{":
            stack_of_paranteses.append(char)
            print("current", char)
        elif char == ")" or char == "]" or char == "}":
            last_element_in_stack = stack_of_paranteses.pop()
            if char == ")" and last_element_in_stack != "(":
                return False
            if char == "]" and last_element_in_stack != "[":
                return False
            if char == "}" and last_element_in_stack != "{":
                return False

    result = True

    return result

if __name__ == "__main__":

    test = "[]{}(){}[[]]{{}}[({})]"
    result = isValid(test)
    print(result)