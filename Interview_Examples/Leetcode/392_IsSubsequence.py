"""
Given two strings s and t, check if s is a subsequence of t.

A subsequence of a string
is a new string that is formed from the original string by deleting some (can be none) of the characters without
disturbing the relative positions
of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

"""


def isSubsequence(s, t):
    if s == "":
        return True

    if len(t) == 0:
        return False

    index_s = 0
    for index_t in range(0, len(t), 1):
        if t[index_t] == s[index_s]:
            index_s += 1

        if index_s >= len(s):
            return True

    return False

if __name__ == "__main__":
    print(isSubsequence("aaa", "bbb"))