"""
Given a string s, return the length
of the longest substring that
contains at most two distinct characters.

Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

Constraints:
1 <= s.length <= 104
s consists of English letters.
https://www.youtube.com/watch?v=6tBEcczNMl8
"""

def lengthOfLongestSubstringTwoDistinct(s):

    right_pointer = 0
    left_pointer = 0
    dictionary_of_characters = {}
    max_length = float('-inf')

    #we need to move the right pointer up to thew point where
    #the are AT most 2 different characters 1<char<=2
    #we will move the left pointer as soon as there are more than
    #2 different chracters (means at least 3)
    #and then we will slide it just after that occurence + update
    #the length of the subbaray and update if necccesary the MAX

    for right_pointer in range(0, len(s), 1):

        current_length = right_pointer - left_pointer
        current_char = s[right_pointer]

        if current_char not in dictionary_of_characters:
            dictionary_of_characters[current_char] = 1
        else:
            dictionary_of_characters[current_char] += 1

        while (len(dictionary_of_characters.keys()) > 2):
            dictionary_of_characters[s[left_pointer]] -= 1
            if dictionary_of_characters[s[left_pointer]] == 0:
                del dictionary_of_characters[s[left_pointer]]
            left_pointer += 1

        if (current_length > max_length):
            max_length = current_length

    return (max_length)

if __name__ == "__main__":
    string = "sssaaaassm"
    result = lengthOfLongestSubstringTwoDistinct(string)
    print(result)