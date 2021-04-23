"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true


Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""


def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    dictionary_s = {}
    dictionary_t = {}

    for index, el in enumerate(s):
        if el not in dictionary_s:
            dictionary_s[el] = [index]
        else:
            dictionary_s[el].append(index)

    for index, el in enumerate(t):
        if el not in dictionary_t:
            dictionary_t[el] = [index]
        else:
            dictionary_t[el].append(index)

    for value in dictionary_t.values():
        if value not in dictionary_s.values():
            return False

    return True

if __name__ == "__main__":
    print(isIsomorphic("aabb", "ccdd"))
