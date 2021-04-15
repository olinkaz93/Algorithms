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

def lengthOfLongestSubstringKDistinct(s, k):

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

        if right_pointer - left_pointer + 1 > the_longest_length:
            the_longest_length = right_pointer - left_pointer + 1

    return the_longest_length

if __name__ == "__main__":
    #d = {}
    #d["key"] = 3
    #d["key"] = 5
    #print(d["key"])
    #print(len(d["list key"]))
    result = lengthOfLongestSubstringKDistinct("eceba", 2)
    print(result)