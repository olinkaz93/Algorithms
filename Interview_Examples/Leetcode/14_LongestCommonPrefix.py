"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.
https://www.youtube.com/watch?v=K1ps6d7YCy4
"""

def longestCommonPrefix(strs):

    if (len(strs)) == 0:
        return ""
    if (len(strs)) == 1:
        return len(strs[0])

    first_prefix = strs[0]
    length_prefix = len(first_prefix)

    for word in strs:
        while word.startswith(first_prefix) != True:
        #while word.find(first_prefix) != 0:

            first_prefix = first_prefix[:-1]
            if (first_prefix) == "":
                return ""

    return first_prefix

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    result = longestCommonPrefix(strs)
    print(result)
