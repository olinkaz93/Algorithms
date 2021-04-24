"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.

"""

def groupAnagrams(strs):
    d = {}
    for w in strs:
        key = tuple(sorted(w))
        if key not in d:
            d[key] = [w]
        else:
            d[key].append(w)
        #d[key] = d.get(key, []) + [w]

    print(d)
    return d.values()

def groupAnnagrams2(strs):
    dictionary = {}

    for word in strs:
        count = [0] * 26 #we have 26 characters

        for char in word:
            current_char = ord(char) - ord("a")
            count[current_char] += 1

        if tuple(count) not in dictionary:
            dictionary[tuple(count)] = [word]
        else:
            dictionary[tuple(count)].append(word)
        #dictionary[tuple(count)].
    return dictionary.values()



if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
    print(groupAnnagrams2(strs))