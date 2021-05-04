"""
5. Longest Palindromic Substring
Medium

10623

685

Add to List

Share
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),

CHECK WITH 647
647. Palindromic Substrings

"""

def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    """
    Palindrome is the string with the same way to READfrom the left, and from the right

    We can have EVEN palindromes
    or ODD - length Palindromes 

    a aaa ababa

    aa aaaa aabbaa

    for each we get the center and expand the window
    """

    maxx = 0
    result = ""

    for i in range(0, len(s), 1):
        for j in [i, i + 1]:
            left = i
            right = j

            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if right - left + 1 > maxx:
                    maxx = right - left + 1
                    maxl = left
                    maxr = right

                left -= 1
                right += 1

    for i in range(maxl, maxr + 1):
        result += s[i]

    return result