"""
https://www.youtube.com/watch?v=SJ1QH4jWTNc

https://www.youtube.com/watch?v=1sFL8yjMcwM

Given a string s and an integer k,
return the length of the longest substring
of s that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Constraints:
1 <= s.length <= 5 * 104
0 <= k <= 50
https://www.youtube.com/watch?v=7Q1uylXOatU
"""

"""
def lengthOfLongestSubstringKDistinct(self, s, k):


    string = s
    the_longest_length = 0
    dictionary_of_characters = {}

    right_pointer = 0
    left_pointer = 0

    for right_pointer in range(0, len(string), 1):

        character = string[right_pointer]

        if character not in dictionary_of_characters:
            dictionary_of_characters[character] = 1
        else:
            dictionary_of_characters[character] += 1

        while (len(dictionary_of_characters.keys()) > k):

            current_char = string[left_pointer]

            if dictionary_of_characters[current_char] == 1:
                del dictionary_of_characters[current_char]
            else:
                dictionary_of_characters[current_char] -= 1

            left_pointer += 1

        the_longest_length = max(the_longest_length, right_pointer - left_pointer + 1)

    return the_longest_length

"""


def lengthOfLongestSubstringKDistinct(self, s, k):
    left = 0
    right = 0
    maxx = 0
    # we need to count the letters and return the LENGTH
    # of the LONGEST substring with AT MOST K distinct characters

    # we will expand the window and count the letters and check if they are < k
    count_letters = 0

    char_list = [0] * 128

    for right in range(0, len(s), 1):

        rletter = s[right]
        char_right = ord(s[right]) - ord('a')
        if char_list[char_right] == 0:
            count_letters += 1

        char_list[char_right] += 1
        while (count_letters > k):
            lletter = s[left]
            char_left = ord(s[left]) - ord('a')
            char_list[char_left] -= 1
            if char_list[char_left] == 0:
                count_letters -= 1
            left += 1

        maxx = max(maxx, right - left + 1)

    return maxx

if __name__ == "__main__":
    #d = {}
    #d["key"] = 3
    #d["key"] = 5
    #print(d["key"])
    #print(len(d["list key"]))
    result = lengthOfLongestSubstringKDistinct("eceba", 2)
    print(result)