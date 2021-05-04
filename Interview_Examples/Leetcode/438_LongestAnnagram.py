"""
438. Find All Anagrams in a String
Medium

4153

203

Add to List

Share
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.


https://www.youtube.com/watch?v=fYgU6Bi2fRg

"""

class Solution(object):
    def findAnagrams(self, s, p):

        """
        We have a SLIDING WINDOW problem

        1) we can use the FIXED window

        2) Let's calculate the numbers in P and then check chunks of them accordingly in the fixed size in the string S

        we will move the left pointer and increase right , check the condition if the values are equal

        """

        if len(p) > len(s):
            return []

        # we create two hash_char lists

        left = 0
        right = 0

        window = len(p)
        char_list_p = [0] * 26
        char_list_s = [0] * 26

        # we create the very first window of chars in the string and p, which will be a base for further adjustments

        while (right < window):
            letterp = p[right]
            letters = s[right]
            char_list_p[ord(letterp) - ord('a')] += 1
            char_list_s[ord(letters) - ord('a')] += 1
            right += 1

        print(char_list_p, char_list_s)

        # we reset the right pointer as the index len(p) - 1
        right = len(p) - 1
        left = 0

        count = 0
        result = []

        while (right < len(s)):

            if char_list_p == char_list_s:
                count += 1
                result.append(left)

            # we slide the window on its right again
            if (right == len(s) - 1):
                break
            right += 1

            letterr = s[right]
            char_list_s[ord(letterr) - ord('a')] += 1

            letterl = s[left]
            char_list_s[ord(letterl) - ord('a')] -= 1
            left += 1

        return result