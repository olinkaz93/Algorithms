"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

============================================
Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""
#Given a string s, find the length of the longest substring without repeating characters.

#having a string for example: "Hello hi"
#can we assume that there is not white spaces, then the input -> "blablablah"

#to check whether there is a SUBSTRING which is the longest, and has no repetitive characters
#we can loop thorugh the input string, and create substrings, where we gonna check the characters
#once the characters will be repeating we will stop to consider this substring and continue looking for another one
#edge case is whether the string is empty
#having the MAX_value_of_unrepeated_characters , for = 0
#then we will update the max _ value, and return it as a solution

#looping thorugh the each charcter will be O(n)
#space complexity, we will need extra hast table to keep our letters, and check their occurence.
#we can have dictionary that will store th emax value, and if we find the max, we will clean it up

#we check the dictionary to see if the letter already exists, the lookup is O(1) time complexity
#we need to loop thorugh the every letter
#then we need do store this current character in the dictionary that we have seen in the substring
#we want to know also the index of the character
#"ale" -> dict { 'a': 0 } . value will be the index of the letter


"""
  #if we have seen the letter already
      #and the index of that seen value is further than the start of the substring
      #we need to update the value of repeated number
      #and assign the start of the substring as the +1 after the OLD location of the repeated letter

  """

def findSubstring(string):

    max_length = 0
    length = 0
    dictionary_of_letters = {}
    index_of_start_substring = 0
    end_of_start_substring = 0

    for index, letter in enumerate(string):
        if letter in dictionary_of_letters and dictionary_of_letters[letter] >= index_of_start_substring:
            index_of_start_substring = dictionary_of_letters[letter] + 1
            #update the length = is equal to the index of the reocurrent element miinu (-) the previous reocurrence of letter
            length = index - dictionary_of_letters[letter]
            dictionary_of_letters[letter] = index
        else:
            dictionary_of_letters[letter] = index
            length +=1
            if (length > max_length):
                max_length = length

    return max_length


class Solution(object):
    def lengthOfLongestSubstring(self, s):

        chars = set()
        longest = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in chars:
                chars.add(s[right])
                longest = max(longest, right - left + 1)
            else:
                # if we have duplicate we remove old characters
                while s[left] != s[right]:
                    chars.remove(s[left])
                    left += 1
                left += 1
        return longest


if __name__ == "__main__":

    example = "bsialala"
    findSubstring(example)
    print(findSubstring((example)))

