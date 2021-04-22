"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.



Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/Easy-python-solution-with-explaination/98769

"""


def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    #len(s) % 2 == 0:

    "we grab siez of substrings, but only up to mid ! index, so we do not exceed the half size!"

    length = len(s)
    medium_index = len(s) // 2
    print("length", length)
    for i in range(medium_index, 0, -1):
        check = ""
        if len(s) % i == 0:
            num_divisions = len(s) // i
            substring = s[:i]
            print(substring)
            for j in range (0, num_divisions, 1):
                print("check")
                check += substring
                print(check)
                if check == s:
                    return True

    return False


    """
    return s in (s+s)[1:-1]
    """

if __name__ == "__main__":
    s = "abababab"
    print(repeatedSubstringPattern(s))




