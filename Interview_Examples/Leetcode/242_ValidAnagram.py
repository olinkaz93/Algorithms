"""
242. Valid Anagram

Given two strings s and t,
return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""

def validAnagram(s, t):

    if len(s) != len(t):
        return False

    #Anagram is the word that has the same letters, the same number of them, just different combination

    # 1st solution is getting them sorted, and compare char by char to see if they are the same
    s_list = list(s)
    t_list = list(t)

    s_list.sort()
    t_list.sort()

    for index in range (0 ,len(s_list),1):
        if s_list[index] != t_list[index]:
            return False

    return True

def validAnagram2(s, t):

    if len(s) != len(t):
        return False

    # 2nd solution, making the list of the chars and than compare them el by element
    # each index will be made for the 'letter' and its value will be ++ when the element occurs

    list_s = [0] * 26
    list_t = [0] * 26
    for index in range (0, len(s), 1):
        char_key = ord(s[index]) - ord('a')
        list_s[char_key] += 1
        char_key = ord(t[index]) - ord('a')
        list_t[char_key] += 1

    print(list_t, list_s)

    for index in range(len(list_s)):
        if list_s[index] != list_t[index]:
            return False
    return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    result = validAnagram(s, t)
    print(result)
    print(ord('a')-ord('a'))

    print(validAnagram2(s, t))