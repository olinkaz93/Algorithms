"""
Given an input string s,
reverse the order of the words.

A word is defined as a sequence
of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words
in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces
or multiple spaces between two words.
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

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

"""

"""
Convert list to string in python using join() in python.
In python string class provides a function join() i.e. join()
function accepts an iterable sequence like list or tuple etc as an argument
and then joins all items in this iterable sequence
to create a string. In the end it returns the concatenated string
"""

def reverseWords(string):

    splitted_string = string.split()
    print(splitted_string)
    result = []
    #for index in range (len(splitted_string)-1, -1, -1):
    #    result.append(splitted_string[index])
    #print(result)
    #return ' '.join(result)
    for index in range(len(splitted_string) - 1, -1, -1):
        result.append(splitted_string[index]+" ")
        print(result)
    result = str(result)
    #print(result)
    return result


if __name__ == "__main__":
    string = "ala ma kota"
    print(reverseWords(string))