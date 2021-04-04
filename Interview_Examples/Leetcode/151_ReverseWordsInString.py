"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"

"""

# Solution 1:
#Input: s = "  Bob    Loves  Alice   "
#Output: "Alice Loves Bob"

#We can use build in functions of python, and take advantage of String properties,
#Strings in python are stored as sequences of letters in memory.
#we can use split(),
#'but life is good!'.split() # ['but', 'life', 'is', 'good!']
#then reverse
#[1,2,5,3].reverse() # None --> Mutates list to [3, 5, 2, 1]
#then join
#' '.join(['Hello','There'])# 'Hello There' --> Joins elements using string as separator.

def reverseString(string):

    #string = string
    #we must save the reversed string
    splitted_string = string.split()
    print("Splitted string into array", splitted_string)

    #reversing the list happens in the same variable, no extra needed
    splitted_string.reverse()
    print("reversed order or (the list) of splitted word from string", splitted_string)

    reversed_string = ' '.join(splitted_string)
    print("Reversed string, after join()", reversed_string)

    return reversed_string

"""
Write a function that reverses a string.
The input string is given as an array of characters s.
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

def reverse_characters(input):

    input.reverse()

    return input


# swap characters in string
def swap(string):
    return string[-1:] + string[1:-1] + string[:1]




if __name__ == "__main__":

    reversed = reverseString("Hello bye")
    print(reversed)

    print(reverse_characters(["h", "e", "y"]))

    string = "hello"
    print(string)
    print(type(string))
    string = list(string)
    print("string as list")
    print(type(string))
    print(len(string))
    string[0], string[len(string)-1] = string[len(string)-1], string[0]
    print(string)

    # take string from user
    """
    str1 = input("Please Enter String : ")
    print(swap(str1))
    print("string", string)
    mid = string[1:len(string) - 1]
    print(mid)
    print(string[1:-1])
    """
