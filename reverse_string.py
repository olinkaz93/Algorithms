"""
Write a function that reverses a string.
The input string is given as an array of characters s.
"""

"""
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

list_of_characters = ["h","e","l","l","o"]

def reverse_string(list):
    #if (len(list) == 0):
    #    return None
    reversed_string = []
    for i in range (len(list)-1, -1, -1):
        reversed_string.append(list[i])

    return reversed_string

result = reverse_string(list_of_characters)
print(result)