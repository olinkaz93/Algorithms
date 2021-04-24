"""
We can shift a string by shifting each of its letters to its successive letter.
For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.


Example 1:
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:
Input: strings = ["a"]
Output: [["a"]]

Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.

"""

def groupStrings(strings):
    # we need to create dictionary
    # we need to create OWN pattern of keys, so we can group the same words
    # lowercase ascii - we can use ord('letter'), and ude %26 to have the values
    # we should use IMMUTABLE data -> we can use tuple as a key
    # return grouped values

    if len(strings) == 1:
        return [strings]

    dictionary_of_words = {}

    for word in strings:
        key = ()
        for letter in range(0, len(word) - 1, 1):
            key_int = (ord(word[letter + 1]) - ord(word[letter])) % 26
            print(key_int)
            key += (key_int,)
        if key not in dictionary_of_words:
            dictionary_of_words[key] = [word]
        else:
            dictionary_of_words[key].append(word)

    values = dictionary_of_words.values()
    return values


if __name__ == "__main__":
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print(groupStrings(strings))